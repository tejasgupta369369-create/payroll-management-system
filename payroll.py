import os
from datetime import datetime

# Current DA rate (change when govt revises it)
DA_PERCENT = 55

# NPS employee contribution
NPS_PERCENT = 10


def calculate_salary(employee):
    """
    Calculate Central Govt salary components.
    """

    basic_pay = employee.basic_pay

    da = (basic_pay * DA_PERCENT) / 100

    hra = employee.hra
    ta = employee.ta

    gross_salary = basic_pay + da + hra + ta

    nps = (basic_pay * NPS_PERCENT) / 100

    net_salary = gross_salary - nps

    return {
        "basic_pay": basic_pay,
        "da": round(da, 2),
        "hra": round(hra, 2),
        "ta": round(ta, 2),
        "gross_salary": round(gross_salary, 2),
        "nps": round(nps, 2),
        "net_salary": round(net_salary, 2)
    }


def print_salary(employee):
    """
    Print salary details on screen.
    """

    salary = calculate_salary(employee)

    print("\n")
    print("=" * 50)
    print("         CENTRAL GOVT PAYSLIP")
    print("=" * 50)

    print(f"Employee ID : {employee.emp_id}")
    print(f"Name        : {employee.name}")
    print(f"Department  : {employee.department}")
    print(f"Designation : {employee.designation}")

    print("-" * 50)

    print(f"Basic Pay   : ₹{salary['basic_pay']:,.2f}")
    print(f"DA ({DA_PERCENT}%)   : ₹{salary['da']:,.2f}")
    print(f"HRA         : ₹{salary['hra']:,.2f}")
    print(f"TA          : ₹{salary['ta']:,.2f}")

    print("-" * 50)

    print(f"Gross Salary: ₹{salary['gross_salary']:,.2f}")
    print(f"NPS ({NPS_PERCENT}%): ₹{salary['nps']:,.2f}")

    print("-" * 50)

    print(f"Net Salary  : ₹{salary['net_salary']:,.2f}")

    print("=" * 50)


def generate_payslip(employee):
    """
    Generate payslip text file.
    """

    salary = calculate_salary(employee)

    if not os.path.exists("payslips"):
        os.makedirs("payslips")

    date_str = datetime.now().strftime("%Y_%m_%d")

    filename = (
        f"payslips/"
        f"Payslip_{employee.emp_id}_{date_str}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("          CENTRAL GOVERNMENT PAYSLIP\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Employee ID : {employee.emp_id}\n")
        file.write(f"Name        : {employee.name}\n")
        file.write(f"Department  : {employee.department}\n")
        file.write(f"Designation : {employee.designation}\n")
        file.write(f"Pay Level   : {employee.pay_level}\n\n")

        file.write("-" * 60 + "\n")

        file.write(
            f"Basic Pay        : ₹{salary['basic_pay']:,.2f}\n"
        )
        file.write(
            f"Dearness Allowance ({DA_PERCENT}%): "
            f"₹{salary['da']:,.2f}\n"
        )
        file.write(
            f"HRA              : ₹{salary['hra']:,.2f}\n"
        )
        file.write(
            f"TA               : ₹{salary['ta']:,.2f}\n"
        )

        file.write("-" * 60 + "\n")

        file.write(
            f"Gross Salary     : ₹{salary['gross_salary']:,.2f}\n"
        )

        file.write(
            f"NPS Deduction    : ₹{salary['nps']:,.2f}\n"
        )

        file.write("-" * 60 + "\n")

        file.write(
            f"Net Salary       : ₹{salary['net_salary']:,.2f}\n"
        )

        file.write("=" * 60 + "\n")

    return filename