# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
        pass


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    the_bill = Bill(amount=120, period="March 2021")
    john = Flatmate(name="John", days_in_house=20)
    marry = Flatmate(name="Marry", days_in_house=25)

    print("John pays", john.pays(bill=the_bill, flatmate=marry))
    print("Marry pays", marry.pays(bill=the_bill, flatmate=john))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
