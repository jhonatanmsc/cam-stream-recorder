import re


def extract_ip_port(text):
    pattern = r'(\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b)'
    text = text.strip()
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None