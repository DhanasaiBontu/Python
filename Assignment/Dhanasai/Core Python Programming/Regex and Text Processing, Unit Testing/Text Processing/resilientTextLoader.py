import unicodedata
def load_and_clean_text(file_path):
    try:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(file_path, "r", encoding="latin-1") as f:
                lines = f.readlines()
        cleaned_lines = []
        for line in lines:
            normalized = unicodedata.normalize("NFKD", line)
            cleaned = normalized.encode("ASCII", "ignore").decode("ASCII")
            cleaned_lines.append(cleaned.strip())
        return f"Cleaned Lines: {cleaned_lines}"
    except (FileNotFoundError, IOError) as e:
        return f"Error: {e}"
print(load_and_clean_text("Text Processing/resilientTextLoader.txt"))