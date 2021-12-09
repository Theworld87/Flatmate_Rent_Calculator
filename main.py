"""
Description: An app that gets the input the amount of a rent for a particular period
and the days that each of the flatmates stayed in the house, for that period.
and returns how much each flatmate has to pay. It also generates a PDF report
stating the names of the flatmates, the period, and how much each of them had to pay.
"""
from flat import Rent, Flatmate
from pdf_report import PdfReport

total_amount = float(input('please enter the rent amount: '))
period = input('What is the rent period? Example ("December 2021"): ')

flatmate1 = input('What is the name of the first flatmate?: ')
days_in_flat1 = int(input(f'How many days did {flatmate1} stay in the flat during the rent period?: '))

flatmate2 = input('What is the name of the second flatmate?: ')
days_in_flat2 = int(input(f'How many days did {flatmate2} stay in the flat during the rent period?: '))

the_bill = Rent(total_amount, period)
tenant1 = Flatmate(flatmate1, days_in_flat1)
tenant2 = Flatmate(flatmate2, days_in_flat2)

print(f"{flatmate1} pays:", tenant1.pays(the_bill, tenant2))
print(f"{flatmate2} pays:", tenant2.pays(the_bill, tenant1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(tenant1, tenant2, the_bill)
