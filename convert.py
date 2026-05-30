from pathlib import Path
from markitdown import MarkItDown

BASE_DIR = Path(__file__).parent

BOOKS_DIR = BASE_DIR / "books"
MARKDOWNS_DIR = BASE_DIR / "markdowns"

MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)

md = MarkItDown()

for subject_dir in BOOKS_DIR.iterdir():
    if not subject_dir.is_dir():
        continue

    output_subject_dir = MARKDOWNS_DIR / subject_dir.name
    output_subject_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nProcessing folder: {subject_dir.name}")

    for pdf_file in subject_dir.glob("*.pdf"):
        try:
            print(f"    Converting {pdf_file.name}")

            result = md.convert(str(pdf_file))

            output_file = (
                output_subject_dir /
                f"{pdf_file.stem}.md"
            )

            output_file.write_text(
                result.text_content,
                encoding="utf-8"
            )

            print(f"    ✓ Saved {output_file.name}")

        except Exception as e:
            print(f"    ✗ Failed {pdf_file.name}")
            print(f"      {e}")

print("\nDone!")