from reportlab.pdfgen import canvas


def generate():

    c = canvas.Canvas("report.pdf")

    c.drawString(100,750,"Border Defence Report")

    c.save()