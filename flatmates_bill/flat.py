
class Bill:
    """Object that contains data about the bill, such as the total amount
    and period"""

    def __init__(self, amount, period):

        self.amount = amount
        self.period = period


class Flatmate:

    """
    Creates a flatmate instance representing a person
    who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, days_total):

        owed = self.days_in_house / days_total
        to_pay = owed * bill.amount

        return round(to_pay, 2)

