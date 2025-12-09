import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFError


def create_pdf(output_path, text_blocks, image_paths):

  
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..'))

  
    font_path = os.path.join(project_root, "fonts", "Paperlogy-4Regular.ttf")

  
    folder = os.path.dirname(output_path)
    if folder:
        os.makedirs(folder, exist_ok=True)

  
    if not os.path.exists(font_path):
        raise TTFError(
            f"Font file not found: {font_path}\n"
            f"Please ensure 'Paperlogy-4Regular.ttf' exists inside the fonts folder."
        )

    try:
        pdfmetrics.registerFont(TTFont("Paperlogy", font_path))
    except Exception as e:
        raise TTFError(f"Failed to register Paperlogy font: {e}")

  
    doc = SimpleDocTemplate(output_path, pagesize=A4)

    styles = getSampleStyleSheet()
    styles["Normal"].fontName = "Paperlogy"
    styles["Title"].fontName = "Paperlogy"

    story = []

    for text in text_blocks:
        story.append(Paragraph(text, styles["Normal"]))
        story.append(Spacer(1, 12))

  
    for img in image_paths:
        try:
            story.append(Image(img, width=400, height=250))
            story.append(Spacer(1, 12))
        except Exception as e:
            print(f"이미지 로드 실패: {img} - {e}")

  
    doc.build(story)
