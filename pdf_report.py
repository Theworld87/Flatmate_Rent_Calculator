import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates,
    such as their names, their rent due and the period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_one, flatmate_two, rent):
        """
        w = width
        h = height
        txt = text used
        border = border around content, if you want.
        align = where the content is displayed.
        ln = The next cell will be on a new line.
        """

        flatmate_pay = str(round(flatmate_one.pays(rent, flatmate_two), 2))
        flatmate2_pay = str(round(flatmate_two.pays(rent, flatmate_one), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        # ^^ PDF object in portrait mode, points size, and A4 size.
        pdf.add_page()

        # Add Image Icon
        pdf.image("files/house.png", w=40, h=40)

        # Add some text and the title.
        pdf.set_font(family='Times', size=24, style='B' + 'U')
        pdf.cell(w=0, h=80, txt="Flatmates Rent", border=0, align="C", ln=1)
        # A cell is like a line/rectangle space on the pdf.

        # Insert period label and value.
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=150, h=40, txt='Period:', border=0)
        pdf.cell(w=200, h=40, txt=rent.period, border=0, ln=1)

        # Insert name and the amount due of first flatmate
        pdf.set_font(family="times", size=12, style='')
        pdf.cell(w=150, h=25, txt=flatmate_one.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_pay, border=0, ln=1)

        # Insert name and the amount due of second flatmate
        pdf.cell(w=150, h=25, txt=flatmate_two.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)
        pdf.cell(w=0, h=40, txt='This is a test PDF file made with Python', border=0, align="C")

        # Changes directory to files folder, create and open PDF.
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
