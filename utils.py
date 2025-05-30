import re
from pathlib import Path


def is_youtube_link(text: str) -> bool:
    return bool(re.search(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+', text))


def format_bytes(size: int) -> str:
    # 1024 bytes = 1 KB
    power = 1024
    n = 0
    units = ["B", "KB", "MB", "GB", "TB", "PB"]

    while size >= power and n < len(units) - 1:
        size /= power
        n += 1

    return f"{size:.2f} {units[n]}"

def format_number(number: int | str) -> str:
    if isinstance(number, str):
        if not number.isdigit():
            return number
        number = int(number)

    if number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}Md"
    elif number >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.2f}K"
    else:
        return str(number)



def get_static_files_path() -> str:
    static_path = Path("./static").absolute()
    static_path.mkdir(parents=True, exist_ok=True)
    return str(static_path)
