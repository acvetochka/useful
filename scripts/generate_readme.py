
from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"

EXCLUDED_DIRS = {
    ".git", ".next", ".venv", "venv",
    "node_modules", "__pycache__", "dist",
    "build", ".turbo"
}


def natural_sort_key(path):
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path.name)
    ]


def get_title(path):
    try:
        content = path.read_text(encoding="utf-8")
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)

        if match:
            return match.group(1).strip()
    except (OSError, UnicodeDecodeError):
        pass

    return path.stem.replace("-", " ").replace("_", " ").title()


def build_tree(directory):
    items = []

    entries = sorted(
        directory.iterdir(),
        key=natural_sort_key
    )

    for entry in entries:
        if entry.is_dir():
            if entry.name in EXCLUDED_DIRS or entry.name.startswith("."):
                continue

            children = build_tree(entry)

            if children:
                items.append(("dir", entry, children))

        elif entry.suffix.lower() == ".md":
            if entry == README:
                continue

            items.append(("file", entry, []))

    return items


def render_tree(items, level=0):
    lines = []
    indent = "  " * level

    for item_type, path, children in items:
        relative = path.relative_to(ROOT).as_posix()

        if item_type == "dir":
            lines.append(f"{indent}- **{path.name}/**")
            lines.extend(render_tree(children, level + 1))

        else:
            url = quote(relative, safe="/")
            title = get_title(path)

            lines.append(
                f"{indent}- [{title}]({url})"
            )

    return lines


def generate():
    tree = build_tree(ROOT)
    navigation = "\n".join(render_tree(tree))

    section = (
        "## Project Documentation\n\n"
        f"{START}\n"
        f"{navigation}\n"
        f"{END}"
    )

    if README.exists():
        content = README.read_text(encoding="utf-8")

        if START in content and END in content:
            pattern = re.compile(
                re.escape(START) + r".*?" + re.escape(END),
                re.DOTALL
            )
            content = pattern.sub(
                f"{START}\n{navigation}\n{END}",
                content
            )
        else:
            content = content.rstrip() + "\n\n" + section + "\n"
    else:
        content = f"# Project\n\n{section}\n"

    README.write_text(content, encoding="utf-8")
    print("README.md successfully generated!")


if __name__ == "__main__":
    generate()
