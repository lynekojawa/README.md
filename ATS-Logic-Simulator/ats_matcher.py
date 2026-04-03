def sanitize_text(raw_text):
    lower_raw_text = raw_text.lower()
    clean_buffer = ""
    for character in lower_raw_text:
        if character.isalnum() or character == " ":
            clean_buffer += character
        else:
            pass
    word_list = clean_buffer.split()
    return set(word_list)

if __name__ == "__main__":
    user_jd = input("Paste your Job Description here:")


    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)
    else:
        print("Error")

    full_jd = " ".join(lines)
    result_set =sanitize_text(full_jd)
    STOP_WORDS = {"the", "and", "is", "of", "to", "in", "this", "on", "you"}
    signal = result_set - STOP_WORDS

    print("\n----- Sanitized Keyword Set ---")
    print(f"Total Unique Keywords: {len(signal)}")
    print(f"keywords: {signal}")
