import re
from typing import Tuple, List
from ciphers import CaesarCipher   


class CaesarCracker:
   

    COMMON_WORDS = {
        'the', 'and', 'ing', 'tion', 'is', 'to', 'of', 'a', 'in', 'for',
        'that', 'with', 'be', 'this', 'have', 'are', 'it', 'as', 'was', 'on'
    }

    @classmethod
    def _score_text(cls, text: str) -> int:
       
        words = re.findall(r'\b[a-z]+\b', text.lower())
        score = sum(1 for w in words if w in cls.COMMON_WORDS)
        return score

    @classmethod
    def crack(cls, ciphertext: str) -> Tuple[str, int]:
    
        best_score = -1
        best_text = ""
        best_key = 0

        for shift in range(1, 26):  # shift 0 is trivial, skip
            decrypted = CaesarCipher.decrypt(ciphertext, shift)
            score = cls._score_text(decrypted)
            if score > best_score:
                best_score = score
                best_text = decrypted
                best_key = shift

        return best_text, best_key

    @classmethod
    def crack_all(cls, ciphertext: str) -> List[Tuple[int, str, int]]:
      
        results = []
        for shift in range(1, 26):
            decrypted = CaesarCipher.decrypt(ciphertext, shift)
            score = cls._score_text(decrypted)
            results.append((shift, decrypted, score))
        results.sort(key=lambda x: x[2], reverse=True)
        return results