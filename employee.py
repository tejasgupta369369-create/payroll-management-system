class Employee:
    """
    Employee Model
    """

    def __init__(
        self,
        emp_id,
        name,
        department,
        designation,
        pay_level,
        basic_pay,
        hra,
        ta
    ):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.pay_level = pay_level
        self.basic_pay = basic_pay
        self.hra = hra
        self.ta = ta

    def display(self):
        print("\nEmployee Details")
        print("-" * 40)
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Designation : {self.designation}")
        print(f"Pay Level   : {self.pay_level}")
        print(f"Basic Pay   : ₹{self.basic_pay:,.2f}")
        print(f"HRA         : ₹{self.hra:,.2f}")
        print(f"TA          : ₹{self.ta:,.2f}")

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "pay_level": self.pay_level,
            "basic_pay": self.basic_pay,
            "hra": self.hra,
            "ta": self.ta
        }

    @classmethod
    def from_database_row(cls, row):
        """
        Convert SQLite row into Employee object
        """
        return cls(
            emp_id=row[0],
            name=row[1],
            department=row[2],
            designation=row[3],
            pay_level=row[4],
            basic_pay=row[5],
            hra=row[6],
            ta=row[7]
        )


if __name__ == "__main__":

    emp = Employee(
        emp_id=1,
        name="Tejas Gupta",
        department="IT",
        designation="Software Engineer",
        pay_level=7,
        basic_pay=44900,
        hra=12000,
        ta=3600
    )

    emp.display()