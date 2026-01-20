import re

def classify_text(cleaned_text: str) -> list:
    """
    Takes cleaned text and classifies each line into categories:
    heading, question, option, equation, table, or other.
    Returns a list of dictionaries with classification.
    """

    lines = cleaned_text.split("\n")
    classified = []

    for line in lines:
        l = line.strip()

        if not l:
            continue  # skip empty lines

        # === RULES FOR DETECTION ===

        # 1️⃣ Detect Headings (Section, Part, etc.)
        if re.match(r'^(SECTION|PART|UNIT)\b', l, re.IGNORECASE):
            classified.append({"type": "heading", "content": l})
        
        # 2️⃣ Detect Questions: "1.", "Q1", "Question 1"
        elif re.match(r'^(Q?\d+[\).])', l, re.IGNORECASE) or l.lower().startswith("question"):
            classified.append({"type": "question", "content": l})

        # 3️⃣ Detect MCQ Options: A / B / C patterns
        elif re.match(r'^[\(\[]?[A-Da-d][\)\]].*', l):  # (A), A), A.
            classified.append({"type": "option", "content": l})

        # 4️⃣ Detect equations (simple pattern: digits + symbols)
        elif re.search(r'[0-9]+[\+\-\*/=][0-9]+', l):
            classified.append({"type": "equation", "content": l})

        # 5️⃣ Detect Table-like structures
        elif re.search(r'\|', l) or re.search(r'\t', l):
            classified.append({"type": "table", "content": l})

        # 6️⃣ Everything else = normal text
        else:
            classified.append({"type": "text", "content": l})

    return classified
