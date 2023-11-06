# test.py

from main import *
from reports import PdfReport

bill_amount = 3283
time_period = "March 2023"

first_flatmate_name = "John"
first_f_no_of_days = 45

second_flatmate_name = "Marry"
second_f_no_of_days = 34

the_bill = Bill(amount=bill_amount, period=time_period)
flatmate_one = Flatmate(name=first_flatmate_name, days_in_house=first_f_no_of_days)
flatmate_two = Flatmate(name=second_flatmate_name, days_in_house=second_f_no_of_days)

pdf = PdfReport(the_bill.period)
pdf.generate(flatmate_one, flatmate_two, the_bill)
