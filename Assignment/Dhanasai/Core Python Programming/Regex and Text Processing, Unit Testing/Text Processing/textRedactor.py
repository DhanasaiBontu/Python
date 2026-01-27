import re
def redact_text(text, sensitive_terms):
    try:
        if not isinstance(text, str) or not isinstance(sensitive_terms, list):
            raise ValueError("Invalid input type")
        redacted_text = text
        for term in sensitive_terms:
            pattern = re.escape(term)
            redacted_text = re.sub(
                pattern,
                "[REDACTED]",
                redacted_text,
                flags=re.IGNORECASE
            )
        return redacted_text
    except Exception as e:
        return f"Error: {e}"
text = "Contact Alex at alex@corp.com"
sensitive = ["Alex", "alex@corp.com"]
print(redact_text(text, sensitive))