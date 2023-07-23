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
