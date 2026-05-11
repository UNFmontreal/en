"""
One-shot script: translate all .md files from ~/git/fr to ~/git/en.
Run once, then delete.

Usage:
    ANTHROPIC_API_KEY=sk-... python translate_all.py
"""

import os
import pathlib
import anthropic

FR_ROOT = pathlib.Path("/home/pbellec/git/fr")
EN_ROOT = pathlib.Path("/home/pbellec/git/en")

# Files to skip (not content, handled separately or not needed)
SKIP = {"CLAUDE.md", "README.md", "migrate.py"}

SYSTEM_PROMPT = """You are a technical translator. Translate MyST Markdown documents from French to English.

Rules:
- Translate only human-readable French text (headings, paragraphs, table cells, link text, card titles/descriptions).
- Preserve ALL MyST directives exactly: :::, {image}, {grid}, {grid-item}, {grid-item-card}, {note}, etc.
- Preserve ALL YAML frontmatter keys (only translate values if they are human-readable text like title/description).
- Preserve ALL links, image paths, email addresses, URLs, and file references unchanged.
- Preserve ALL markdown formatting: bold, italic, tables, bullet lists, code blocks.
- Preserve ALL inline HTML exactly (iframes, etc.).
- Do NOT add or remove blank lines beyond what is necessary.
- Output ONLY the translated markdown. No preamble, no explanation."""


def translate_file(client: anthropic.Anthropic, content: str, filename: str) -> str:
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Translate this file ({filename}) from French to English:\n\n{content}",
            }
        ],
    )
    return message.content[0].text


def main():
    client = anthropic.Anthropic()

    md_files = sorted(FR_ROOT.rglob("*.md"))
    to_translate = [f for f in md_files if f.name not in SKIP]

    print(f"Translating {len(to_translate)} files...")

    for fr_path in to_translate:
        rel = fr_path.relative_to(FR_ROOT)
        en_path = EN_ROOT / rel

        en_path.parent.mkdir(parents=True, exist_ok=True)

        content = fr_path.read_text(encoding="utf-8")
        print(f"  {rel} ... ", end="", flush=True)

        translated = translate_file(client, content, str(rel))
        en_path.write_text(translated, encoding="utf-8")
        print("done")

    print("\nAll files translated.")


if __name__ == "__main__":
    main()
