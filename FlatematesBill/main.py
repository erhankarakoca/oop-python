from flat import Bill, Flatmate
from report import PdfReport

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    amount = float(input("Enter the bill amount: "))
    period = input("Enter the period (e.g. December 2020): ")
    # print(type(period))

    name1 = input("What is your name ? ")
    days_in_house_flatmate1 = int(input(f"How many days did {name1} stayed at home during the bill period? "))

    name2 = input("What is your flatmates name ? ")
    days_in_house_flatmate2 = int(input(f"How many days did {name2} stayed at home during the bill period? "))

    the_bill = Bill(amount=amount, period=period)

    flatmate1 = Flatmate(name=name1, days_in_house=days_in_house_flatmate1)
    flatmate2 = Flatmate(name=name2, days_in_house=days_in_house_flatmate2)

    print(f"{flatmate1.name} pays", flatmate1.pays(bill=the_bill, flatmate=flatmate2))
    print(f"{flatmate2.name} pays", flatmate2.pays(bill=the_bill, flatmate=flatmate1))

    pdf_report = PdfReport(filename=period.replace(" ", "_")+".pdf")
    pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
