from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class PDFReport:
    def __init__(self, path="report.pdf"):
        self.path = path
        self.c = canvas.Canvas(self.path, pagesize=A4)
        self.width, self.height = A4
        self.cursor_y = self.height - 50

    def add_title(self, text):
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, self.cursor_y, text)
        self.cursor_y -= 40

    def add_text(self, text):
        self.c.setFont("Helvetica", 11)
        lines = text.split("\n")
        for line in lines:
            if self.cursor_y < 50:
                self.c.showPage()
                self.cursor_y = self.height - 50
                self.c.setFont("Helvetica", 11)
            self.c.drawString(50, self.cursor_y, line)
            self.cursor_y -= 16

    def add_image(self, img_path, width=400):
        if self.cursor_y < 200:
            self.c.showPage()
            self.cursor_y = self.height - 50

        self.c.drawImage(img_path, 50, self.cursor_y - 200, width=width)
        self.cursor_y -= 220

    def save(self):
        self.c.save()
