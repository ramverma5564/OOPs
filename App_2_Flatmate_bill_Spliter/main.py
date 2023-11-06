from flat import Bill, Flatmate
from reports import PdfReport

if __name__ == "__main__":
    bill_amount = round(float(input("Hey user! enter the bill amount : ")), 2)
    time_period = input("Enter the time period : ")

    first_flatmate_name = input("Enter the first flatmate's name : ")
    first_f_no_of_days = int(input("Enter the number of days lived : "))

    second_flatmate_name = input("Enter the second flatmate's name : ")
    second_f_no_of_days = int(input("Enter the number of days lived : "))

    the_bill = Bill(amount=bill_amount, period=time_period)
    flatmate_one = Flatmate(name=first_flatmate_name, days_in_house=first_f_no_of_days)
    flatmate_two = Flatmate(
        name=second_flatmate_name, days_in_house=second_f_no_of_days
    )

    pdf = PdfReport(the_bill.period)
    pdf.generate(flatmate_one, flatmate_two, the_bill)
