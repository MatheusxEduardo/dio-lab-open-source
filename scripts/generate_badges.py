import requests

def generate_badge(label, message, color):
    url = f"https://img.shields.io/badge/{label}-{message}-{color}"
    badge_markdown = f"![{label}]({url})"
    return badge_markdown

if __name__ == "__main__":
    badge = generate_badge("Status", "Ativo", "green")
    with open("README.md", "a") as f:
        f.write("\n" + badge)
