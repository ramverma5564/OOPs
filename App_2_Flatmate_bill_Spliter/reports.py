import os.path
import webbrowser

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        c = canvas.Canvas("Files/Reports/"+self.filename, pagesize=A4)
        w, height = A4

        # PDF Title
        title = "Flatmates' Bill"
        c.setTitle(title)

        # PDF Logo
        height = height - 60
        width = 50
        c.drawImage("Files/Logo/house_bill_logo.png", width, height, 40, 40, mask="auto")

        # PDF Heading
        c.setFont("Helvetica", 40)
        font_width = 15
        height = height + 10
        c.drawString((w - len(title) * font_width) / 2, height, title)

        # PDF Content

        # Total Bill
        c.setFont("Helvetica", 18)
        font_width = 7
        height = height - 60
        width = 50
        text = "Total Bill : "
        c.drawString(width, height, text)
        width = width + font_width * len(text)
        c.drawString(width, height, str(bill.amount))

        # Time Period
        c.setFont("Helvetica", 18)
        font_width = 7
        width = 340
        text = "Total Days : "
        c.drawString(width, height, text)
        width = width + font_width * len(text) + 10
        c.drawString(width, height, bill.period)

        # flatmates bills description

        # First Flatmate
        height = height - 40
        width = 50
        text = flatmate1.name + "'s Bill:"
        c.drawString(width, height, text)
        width = width + font_width * len(text) + 10
        text = str(round(flatmate1.pays(bill, flatmate2), 2))
        c.drawString(width, height, text)

        text = flatmate1.name + " stayed : "
        width = 340
        c.drawString(width, height, text)
        width = width + font_width * len(text) + 20
        text = str(flatmate1.days_in_house) + " days"
        c.drawString(width, height, text)

        # Second Flatmate
        height = height - 40
        width = 50
        text = flatmate2.name + "'s Bill:"
        c.drawString(width, height, text)
        width = width + font_width * len(text) + 10
        text = str(round(flatmate2.pays(bill, flatmate1), 2))
        c.drawString(width, height, text)

        text = flatmate2.name + " stayed : "
        width = 340
        c.drawString(width, height, text)
        width = width + font_width * len(text) + 20
        text = str(flatmate2.days_in_house) + " days"
        c.drawString(width, height, text)

        c.showPage()
        c.save()

        # Open pdf file automatically
        webbrowser.open(os.path.realpath("Files/Reports/"+self.filename))
