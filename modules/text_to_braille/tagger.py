def apply_tags(classified_list: list) -> list:
    """
    Takes classified output and applies Braille-ready structure tags.
    Returns a list of tagged lines.
    """

    tagged_output = []
    q_count = 0

    for item in classified_list:
        text = item["content"]
        t = item["type"]

        if t == "heading":
            tagged_output.append(f"#H1: {text}")

        elif t == "question":
            q_count += 1
            tagged_output.append(f"#Q{q_count}: {text}")

        elif t == "option":
            tagged_output.append(text)

        elif t == "equation":
            tagged_output.append(f"#EQ: {text}")

        elif t == "table":
            tagged_output.append(f"#TB: {text}")

        elif t == "text":
            tagged_output.append(f"#T: {text}")

        else:
            tagged_output.append(text)

    return tagged_output
