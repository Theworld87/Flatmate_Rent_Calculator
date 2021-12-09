class Rent:
    """
    Object that contains data about rent, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        # Rent constructor.
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Create a person who lives in the flat and pays share of the rent.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, rent, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = rent.amount * weight
        return to_pay
