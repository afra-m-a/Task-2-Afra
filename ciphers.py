import string
from typing import Union


class CaesarCipher:

    @staticmethod
    def _shift_char(ch: str, shift: int) -> str:
        
        if ch.isupper():
            base = ord('A')
            return chr((ord(ch) - base + shift) % 26 + base)
        if ch.islower():
            base = ord('a')
            return chr((ord(ch) - base + shift) % 26 + base)
        return ch  # digits, punctuation, spaces remain as is

    @staticmethod
    def encrypt(text: str, key: int) -> str:
      
        shift = key % 26
        return ''.join(CaesarCipher._shift_char(ch, shift) for ch in text)

    @staticmethod
    def decrypt(text: str, key: int) -> str:
        
        shift = (-key) % 26
        return ''.join(CaesarCipher._shift_char(ch, shift) for ch in text)


class VigenereCipher:

    @staticmethod
    def _normalize_key(key: str) -> str:
        return ''.join(ch for ch in key if ch.isalpha()).lower()

    @staticmethod
    def _shift_char(ch: str, shift: int) -> str:
        if ch.isupper():
            base = ord('A')
            return chr((ord(ch) - base + shift) % 26 + base)
        if ch.islower():
            base = ord('a')
            return chr((ord(ch) - base + shift) % 26 + base)
        return ch

    @classmethod
    def encrypt(cls, text: str, key: str) -> str:
       
        normalized_key = cls._normalize_key(key)
        if not normalized_key:
            raise ValueError("Vigenère key must contain at least one alphabetic character.")
        result = []
        key_idx = 0
        for ch in text:
            if ch.isalpha():
                shift = ord(normalized_key[key_idx % len(normalized_key)]) - ord('a')
                result.append(cls._shift_char(ch, shift))
                key_idx += 1
            else:
                result.append(ch)
        return ''.join(result)

    @classmethod
    def decrypt(cls, text: str, key: str) -> str:
       
        normalized_key = cls._normalize_key(key)
        if not normalized_key:
            raise ValueError("Vigenère key must contain at least one alphabetic character.")
        result = []
        key_idx = 0
        for ch in text:
            if ch.isalpha():
                shift = ord(normalized_key[key_idx % len(normalized_key)]) - ord('a')
                result.append(cls._shift_char(ch, -shift))
                key_idx += 1
            else:
                result.append(ch)
        return ''.join(result)