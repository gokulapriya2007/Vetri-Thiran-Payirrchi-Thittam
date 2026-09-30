from fpdf import FPDF

from .config import (
    EXPORTS_DIR,
    BASE_DIR
)


# --------------------------------------------------
# PDF-safe text
# --------------------------------------------------

def pdf_safe(text):

    if not text:
        return ""

    return (
        text
        .encode(
            "latin-1",
            "replace"
        )
        .decode(
            "latin-1"
        )
    )


# --------------------------------------------------
# Save comic PDF
# --------------------------------------------------

def save_pdf(
    title,
    layout
):

    safe_title = "".join(
        character
        if character.isalnum()
        else "_"
        for character in title
    )

    safe_title = safe_title[:50]

    if not safe_title:

        safe_title = "comic"

    pdf_path = (
        EXPORTS_DIR /
        f"{safe_title}.pdf"
    )

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    for panel in layout:

        pdf.add_page()

        # Title
        pdf.set_font(
            "Arial",
            "B",
            18
        )

        pdf.cell(
            0,
            12,
            pdf_safe(
                f"Panel {panel.panel_number}: "
                f"{panel.title}"
            ),
            ln=True
        )

        pdf.ln(3)

        # Image
        image_file = (
            BASE_DIR /
            panel.image_url.lstrip("/")
        )

        if image_file.exists():

            pdf.image(
                str(image_file),
                x=15,
                y=32,
                w=180
            )

            pdf.ln(118)

        # Scene
        pdf.set_font(
            "Arial",
            "I",
            11
        )

        pdf.multi_cell(
            0,
            7,
            pdf_safe(
                panel.scene_description
            )
        )

        pdf.ln(2)

        # Caption
        if panel.caption:

            pdf.set_font(
                "Arial",
                "B",
                11
            )

            pdf.multi_cell(
                0,
                7,
                pdf_safe(
                    panel.caption
                )
            )

        # Narration
        if panel.narration:

            pdf.set_font(
                "Arial",
                "",
                11
            )

            pdf.multi_cell(
                0,
                7,
                pdf_safe(
                    panel.narration
                )
            )

        # Dialogue
        if panel.dialogue:

            pdf.ln(2)

            pdf.set_font(
                "Arial",
                "B",
                11
            )

            pdf.multi_cell(
                0,
                7,
                pdf_safe(
                    panel.dialogue
                )
            )

    pdf.output(
        str(pdf_path)
    )

    return (
        f"/static/exports/"
        f"{pdf_path.name}"
    )