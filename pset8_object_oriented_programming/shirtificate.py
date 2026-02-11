from fpdf import FPDF

class CS50(FPDF):

    def __init__(self, orientation = "portrait", unit = "mm", format = "A4", font_cache_dir = "DEPRECATED"):
        super().__init__(orientation, unit, format, font_cache_dir)

    def shirt(self, name):
        self.add_page()
        self.image("shirtificate.png", x=0, y=60, w=210)
        self.set_font("Helvetica", size= 50)
        self.cell(0, 40, "CS50 Shirtificate", align= "C")
        self.set_font("Helvetica", size= 25)
        self.set_text_color(255, 255, 255)
        self.cell(-185, 250, f"{name} took CS50", align= "C")
        self.output("shirtificate.pdf")

x = input("Name: ")
cs50 = CS50()
cs50.shirt(x)