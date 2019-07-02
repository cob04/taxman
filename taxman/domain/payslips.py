"""Payslips module."""


class Payslip:

    def __init__(self, code, fullname, income, nationality):
        self.code = code
        self.fullname = fullname
        self.income = income
        self.nationality = nationality
        self.processed = False
