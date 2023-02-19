# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who live in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        """
        Method of flatmate. Each flatmate pays the
        bill respect to the days being in home
        :return:
        """
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates PDF file that contains data about
    flatmates : their names, their due dates and
    the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("files\house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=0, align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the flatmate 1
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the flatmate 2
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        # webbrowser.open('file://' +os.path.realpath(self.filename) -> linux or macos
        webbrowser.open(self.filename)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    the_bill = Bill(amount=120, period="April 2021")
    john = Flatmate(name="John", days_in_house=20)
    marry = Flatmate(name="Marry", days_in_house=25)

    print("John pays", john.pays(bill=the_bill, flatmate=marry))
    print("Marry pays", marry.pays(bill=the_bill, flatmate=john))

    pdf_report = PdfReport(filename="Report1.pdf")
    pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
