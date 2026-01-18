import re

def clean_text(raw_text: str) -> str:
    if not raw_text:
        return ""

    text = raw_text

    # 1️⃣ Remove page numbers & "Page X"
    text = re.sub(r'Page\s*\d+','', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+\s*/\s*\d+\b', '', text)  # "2/5"

    # 2️⃣ Remove headers / footers (common patterns)
    text = re.sub(r'^\s*Name:.*$','', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*Date:.*$','', text, flags=re.MULTILINE)

    # 3️⃣ Remove decorative characters
    text = re.sub(r'[-*_=~]{3,}', '', text)

    # 4️⃣ Clean bullet symbols → "-"
    text = re.sub(r'[•●▪◦]', '-', text)

    # 5️⃣ Replace multiple spaces/newlines
    text = re.sub(r'\n{3,}', '\n\n', text)       # limit blank lines
    text = re.sub(r'[ ]{2,}', ' ', text)        # remove extra spaces

    # 6️⃣ Numbering fixes for multi-column like "1. 2. 3."
    text = text.replace('\t', ' ')  # tabs → spaces

    # 7️⃣ Trim whitespace
    text = text.strip()

    return text
