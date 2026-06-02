
import customtkinter as ctk
from tkinter import messagebox
from ciphers import CaesarCipher, VigenereCipher
from analyzer import CaesarCracker


ctk.set_appearance_mode("dark")         
ctk.set_default_color_theme("dark-blue") 

BG_DARK = "#0D0D0E"      
SIDEBAR_COLOR = "#090909"
CARD_COLOR = "#141B2B"
ACCENT_COLOR = "#C41A1A"  
TEXT_COLOR = "#E0E0E0"
BUTTON_HOVER = "#E41429"


class ModernCryptoApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Master Cipher Suite — Advanced Encryption Toolkit")
        self.geometry("1000x700")
        self.minsize(900, 600)
        self.configure(fg_color=BG_DARK)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=SIDEBAR_COLOR)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)  

        logo_label = ctk.CTkLabel(
            self.sidebar,
            text="🔐 Cipher Suite",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=ACCENT_COLOR
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))

        self.btn_encrypt = ctk.CTkButton(
            self.sidebar,
            text="🔒 Encrypt / Decrypt",
            command=self.show_encrypt_frame,
            fg_color="transparent",
            text_color=TEXT_COLOR,
            hover_color=ACCENT_COLOR,
            anchor="w",
            font=ctk.CTkFont(size=14)
        )
        self.btn_encrypt.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_crack = ctk.CTkButton(
            self.sidebar,
            text="🔓 Cryptoanalysis",
            command=self.show_crack_frame,
            fg_color="transparent",
            text_color=TEXT_COLOR,
            hover_color=ACCENT_COLOR,
            anchor="w",
            font=ctk.CTkFont(size=14)
        )
        self.btn_crack.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        footer_label = ctk.CTkLabel(
            self.sidebar,
            text="Advanced Cipher Toolkit\nv2.0",
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        footer_label.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="s")

        self.main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color=CARD_COLOR)
        self.main_frame.grid(row=0, column=1, padx=25, pady=25, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.encrypt_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.crack_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")

        self._build_encrypt_ui()
        self._build_crack_ui()

        self.show_encrypt_frame()

    def _build_encrypt_ui(self):
        title = ctk.CTkLabel(
            self.encrypt_frame,
            text="⚡ Encryption & Decryption Hub",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=ACCENT_COLOR
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        subtitle = ctk.CTkLabel(
            self.encrypt_frame,
            text="Choose cipher, mode, and key — then execute.",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        subtitle.pack(anchor="w", padx=20, pady=(0, 20))

        row_frame = ctk.CTkFrame(self.encrypt_frame, fg_color="transparent")
        row_frame.pack(fill="x", padx=20, pady=5)

        cipher_card = ctk.CTkFrame(row_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        cipher_card.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=5)
        ctk.CTkLabel(cipher_card, text="Cipher Type", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        self.cipher_var = ctk.StringVar(value="Caesar")
        caesar_radio = ctk.CTkRadioButton(cipher_card, text="Caesar", variable=self.cipher_var, value="Caesar")
        caesar_radio.pack(anchor="w", padx=15, pady=5)
        vig_radio = ctk.CTkRadioButton(cipher_card, text="Vigenère", variable=self.cipher_var, value="Vigenère")
        vig_radio.pack(anchor="w", padx=15, pady=5)

        mode_card = ctk.CTkFrame(row_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        mode_card.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=5)
        ctk.CTkLabel(mode_card, text="Operation Mode", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        self.mode_var = ctk.StringVar(value="Encrypt")
        enc_radio = ctk.CTkRadioButton(mode_card, text="Encrypt", variable=self.mode_var, value="Encrypt")
        enc_radio.pack(anchor="w", padx=15, pady=5)
        dec_radio = ctk.CTkRadioButton(mode_card, text="Decrypt", variable=self.mode_var, value="Decrypt")
        dec_radio.pack(anchor="w", padx=15, pady=5)

        input_card = ctk.CTkFrame(self.encrypt_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        input_card.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(input_card, text="📄 Input Text", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        self.input_text = ctk.CTkTextbox(input_card, height=120, wrap="word", corner_radius=10)
        self.input_text.pack(fill="x", padx=15, pady=(5, 10))

        key_card = ctk.CTkFrame(self.encrypt_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        key_card.pack(fill="x", padx=20, pady=10)
        self.key_label = ctk.CTkLabel(key_card, text="🔑 Key (shift integer):", font=ctk.CTkFont(size=12, weight="bold"))
        self.key_label.pack(anchor="w", padx=15, pady=(10, 0))
        self.key_entry = ctk.CTkEntry(key_card, placeholder_text="e.g., 3  or  keyword", corner_radius=10)
        self.key_entry.pack(fill="x", padx=15, pady=(5, 10))

        self.execute_btn = ctk.CTkButton(
            self.encrypt_frame,
            text="▶ EXECUTE",
            command=self._execute_cipher,
            fg_color=ACCENT_COLOR,
            hover_color=BUTTON_HOVER,
            font=ctk.CTkFont(size=14, weight="bold"),
            corner_radius=12,
            height=40
        )
        self.execute_btn.pack(pady=15, padx=20, fill="x")

        output_card = ctk.CTkFrame(self.encrypt_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        output_card.pack(fill="x", padx=20, pady=10, expand=True)
        ctk.CTkLabel(output_card, text="📋 Result", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        self.output_text = ctk.CTkTextbox(output_card, height=120, wrap="word", corner_radius=10)
        self.output_text.pack(fill="both", padx=15, pady=(5, 10), expand=True)

        copy_btn = ctk.CTkButton(
            self.encrypt_frame,
            text="📋 Copy to Clipboard",
            command=self._copy_output,
            fg_color="transparent",
            border_width=2,
            border_color=ACCENT_COLOR,
            text_color=ACCENT_COLOR,
            hover_color=ACCENT_COLOR,
            corner_radius=12
        )
        copy_btn.pack(pady=(0, 20), padx=20, fill="x")

        def update_key_label(*args):
            if self.cipher_var.get() == "Caesar":
                self.key_label.configure(text="🔑 Key (shift integer):")
                self.key_entry.configure(placeholder_text="e.g., 3")
            else:
                self.key_label.configure(text="🔑 Key (alphabetic word):")
                self.key_entry.configure(placeholder_text="e.g., secret")
        self.cipher_var.trace_add("write", update_key_label)
        update_key_label()

    def _build_crack_ui(self):
        title = ctk.CTkLabel(
            self.crack_frame,
            text="🔍 Caesar Cipher Cracker",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=ACCENT_COLOR
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        subtitle = ctk.CTkLabel(
            self.crack_frame,
            text="Paste Caesar‑ciphered text",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        subtitle.pack(anchor="w", padx=20, pady=(0, 20))

        input_card = ctk.CTkFrame(self.crack_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        input_card.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(input_card, text="📝 Ciphertext", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        self.crack_input = ctk.CTkTextbox(input_card, height=120, wrap="word", corner_radius=10)
        self.crack_input.pack(fill="x", padx=15, pady=(5, 10))

        crack_btn = ctk.CTkButton(
            self.crack_frame,
            text="🔓 CRACK MESSAGE",
            command=self._crack_caesar,
            fg_color=ACCENT_COLOR,
            hover_color=BUTTON_HOVER,
            font=ctk.CTkFont(size=14, weight="bold"),
            corner_radius=12,
            height=40
        )
        crack_btn.pack(pady=15, padx=20, fill="x")

        output_card = ctk.CTkFrame(self.crack_frame, corner_radius=15, fg_color=SIDEBAR_COLOR)
        output_card.pack(fill="both", padx=20, pady=10, expand=True)
        ctk.CTkLabel(output_card, text="📊 Analysis Result", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        self.crack_output = ctk.CTkTextbox(output_card, wrap="word", corner_radius=10)
        self.crack_output.pack(fill="both", padx=15, pady=(5, 10), expand=True)

        copy_crack_btn = ctk.CTkButton(
            self.crack_frame,
            text="📋 Copy to Clipboard",
            command=self._copy_crack_output,
            fg_color="transparent",
            border_width=2,
            border_color=ACCENT_COLOR,
            text_color=ACCENT_COLOR,
            hover_color=ACCENT_COLOR,
            corner_radius=12
        )
        copy_crack_btn.pack(pady=(0, 20), padx=20, fill="x")

    def show_encrypt_frame(self):
        self.encrypt_frame.pack(fill="both", expand=True)
        self.crack_frame.pack_forget()
        self._update_sidebar_style(self.btn_encrypt)

    def show_crack_frame(self):
        self.crack_frame.pack(fill="both", expand=True)
        self.encrypt_frame.pack_forget()
        self._update_sidebar_style(self.btn_crack)

    def _update_sidebar_style(self, active_button):
        """Reset sidebar buttons to normal and highlight the active one."""
        for btn in [self.btn_encrypt, self.btn_crack]:
            btn.configure(fg_color="transparent", text_color=TEXT_COLOR)
        active_button.configure(fg_color=ACCENT_COLOR, text_color=BG_DARK)

    def _execute_cipher(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please enter some text.")
            return

        mode = self.mode_var.get()
        cipher_type = self.cipher_var.get()
        key_raw = self.key_entry.get().strip()

        try:
            if cipher_type == "Caesar":
                try:
                    key = int(key_raw)
                except ValueError:
                    messagebox.showerror("Invalid Key", "Caesar key must be an integer (e.g., 3).")
                    return
                if mode == "Encrypt":
                    result = CaesarCipher.encrypt(text, key)
                else:
                    result = CaesarCipher.decrypt(text, key)
            else:  # Vigenère
                if not key_raw:
                    messagebox.showerror("Missing Key", "Vigenère key cannot be empty.")
                    return
                if mode == "Encrypt":
                    result = VigenereCipher.encrypt(text, key_raw)
                else:
                    result = VigenereCipher.decrypt(text, key_raw)

            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _copy_output(self):
        text = self.output_text.get("1.0", "end-1c").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("Copied", "Output copied to clipboard.")
        else:
            messagebox.showwarning("Nothing to copy", "Output is empty.")

    def _crack_caesar(self):
        ciphertext = self.crack_input.get("1.0", "end-1c").strip()
        if not ciphertext:
            messagebox.showwarning("Empty Input", "Please paste some ciphertext.")
            return
        try:
            plaintext, key = CaesarCracker.crack(ciphertext)
            output = f"🔑 Most likely key: {key}\n\n📜 Decrypted text:\n{plaintext}"
            self.crack_output.delete("1.0", "end")
            self.crack_output.insert("1.0", output)
        except Exception as e:
            messagebox.showerror("Cracking failed", str(e))

    def _copy_crack_output(self):
        text = self.crack_output.get("1.0", "end-1c").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("Copied", "Analysis result copied.")
        else:
            messagebox.showwarning("Nothing to copy", "No result to copy.")


def run_gui():
    app = ModernCryptoApp()
    app.mainloop()