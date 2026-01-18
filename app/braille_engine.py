import os
import uuid

# Simple Grade-1 style Braille mapping (demo-safe)
BRAILLE_MAP = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽",
    "z": "⠵", " ": " "
}

def text_to_braille(text: str) -> str:
    return "".join(BRAILLE_MAP.get(ch.lower(), ch) for ch in text)

def convert_to_braille(tagged_lines: list, output_dir="outputs") -> str:
    os.makedirs(output_dir, exist_ok=True)

    braille_lines = [text_to_braille(line) for line in tagged_lines]
    braille_text = "\n".join(braille_lines)

    file_name = f"braille_{uuid.uuid4()}.brf"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(braille_text)

    return file_path
