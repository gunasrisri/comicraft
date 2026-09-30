from fpdf import FPDF
from pathlib import Path


def save_pdf(layout):
    output_dir = Path("static/exports")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = output_dir / "comic.pdf"

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for panel in layout:
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Panel {panel['panel']} - {panel['title']}", ln=True)

        if Path(panel["image_path"]).exists():
            pdf.image(panel["image_path"], x=10, y=30, w=190)

        pdf.ln(110)

        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, str(panel["caption"]))

    pdf.output(str(pdf_path))

    return str(pdf_path)