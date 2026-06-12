import tkinter as tk
from tkinter import ttk, messagebox

from database import (
    create_database,
    add_employee,
    get_all_employees,
    delete_employee
)

from employee import Employee
from payroll import calculate_salary, generate_payslip
from login import authenticate


class PayrollApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Central Govt Payroll System")
        self.root.geometry("1000x600")

        title = tk.Label(
            root,
            text="Central Govt Payroll System",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        form_frame = tk.Frame(root)
        form_frame.pack(pady=10)

        # Name
        tk.Label(form_frame, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1)

        # Department
        tk.Label(form_frame, text="Department").grid(row=0, column=2)
        self.department_entry = tk.Entry(form_frame)
        self.department_entry.grid(row=0, column=3)

        # Designation
        tk.Label(form_frame, text="Designation").grid(row=1, column=0)
        self.designation_entry = tk.Entry(form_frame)
        self.designation_entry.grid(row=1, column=1)

        # Pay Level
        tk.Label(form_frame, text="Pay Level").grid(row=1, column=2)
        self.pay_level_entry = tk.Entry(form_frame)
        self.pay_level_entry.grid(row=1, column=3)

        # Basic Pay
        tk.Label(form_frame, text="Basic Pay").grid(row=2, column=0)
        self.basic_pay_entry = tk.Entry(form_frame)
        self.basic_pay_entry.grid(row=2, column=1)

        # HRA
        tk.Label(form_frame, text="HRA").grid(row=2, column=2)
        self.hra_entry = tk.Entry(form_frame)
        self.hra_entry.grid(row=2, column=3)

        # TA
        tk.Label(form_frame, text="TA").grid(row=3, column=0)
        self.ta_entry = tk.Entry(form_frame)
        self.ta_entry.grid(row=3, column=1)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Employee",
            command=self.add_employee_gui
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Refresh",
            command=self.load_employees
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete Employee",
            command=self.delete_employee_gui
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Generate Payslip",
            command=self.generate_payslip_gui
        ).grid(row=0, column=3, padx=5)

        # Table
        self.tree = ttk.Treeview(
            root,
            columns=(
                "ID",
                "Name",
                "Department",
                "Designation",
                "PayLevel",
                "Basic",
                "HRA",
                "TA"
            ),
            show="headings"
        )

        headings = [
            "ID",
            "Name",
            "Department",
            "Designation",
            "PayLevel",
            "Basic",
            "HRA",
            "TA"
        ]

        for heading in headings:
            self.tree.heading(heading, text=heading)
            self.tree.column(heading, width=120)

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_employees()

    def clear_fields(self):

        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.designation_entry.delete(0, tk.END)
        self.pay_level_entry.delete(0, tk.END)
        self.basic_pay_entry.delete(0, tk.END)
        self.hra_entry.delete(0, tk.END)
        self.ta_entry.delete(0, tk.END)

    def add_employee_gui(self):

        if (
            not self.name_entry.get().strip()
            or not self.department_entry.get().strip()
            or not self.designation_entry.get().strip()
            or not self.pay_level_entry.get().strip()
            or not self.basic_pay_entry.get().strip()
            or not self.hra_entry.get().strip()
            or not self.ta_entry.get().strip()
        ):
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        try:

            add_employee(
                self.name_entry.get(),
                self.department_entry.get(),
                self.designation_entry.get(),
                int(self.pay_level_entry.get()),
                float(self.basic_pay_entry.get()),
                float(self.hra_entry.get()),
                float(self.ta_entry.get())
            )

            messagebox.showinfo(
                "Success",
                "Employee Added Successfully"
            )

            self.clear_fields()
            self.load_employees()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Pay Level, Basic Pay, HRA and TA must be numeric."
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_employees(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        employees = get_all_employees()

        for emp in employees:
            self.tree.insert("", tk.END, values=emp)

    def delete_employee_gui(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select an Employee"
            )
            return

        emp_id = self.tree.item(selected[0])["values"][0]

        delete_employee(emp_id)

        messagebox.showinfo(
            "Deleted",
            "Employee Deleted"
        )

        self.load_employees()

    def generate_payslip_gui(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select an Employee"
            )
            return

        data = self.tree.item(selected[0])["values"]

        try:

            emp = Employee(
                emp_id=int(data[0]),
                name=str(data[1]),
                department=str(data[2]),
                designation=str(data[3]),
                pay_level=int(data[4]),
                basic_pay=float(data[5]),
                hra=float(data[6]),
                ta=float(data[7])
            )

            salary = calculate_salary(emp)

            filepath = generate_payslip(emp)

            messagebox.showinfo(
                "Payslip Generated",
                f"Gross Salary: ₹{salary['gross_salary']:,.2f}\n\n"
                f"Net Salary: ₹{salary['net_salary']:,.2f}\n\n"
                f"Saved:\n{filepath}"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to generate payslip.\n\n{str(e)}"
            )


def main():

    create_database()

    if not authenticate():
        return

    root = tk.Tk()

    PayrollApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
