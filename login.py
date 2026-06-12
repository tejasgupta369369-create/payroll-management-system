import tkinter as tk
from tkinter import messagebox


class LoginWindow:
    """
    Simple Admin Login Window
    """

    def __init__(self, root):

        self.root = root
        self.root.title("Central Govt Payroll System - Login")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Default Admin Credentials
        self.admin_username = "admin"
        self.admin_password = "admin123"

        # Title
        title = tk.Label(
            root,
            text="Central Govt Payroll System",
            font=("Arial", 14, "bold")
        )
        title.pack(pady=15)

        # Username
        tk.Label(root, text="Username").pack()

        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.pack(pady=5)

        # Password
        tk.Label(root, text="Password").pack()

        self.password_entry = tk.Entry(
            root,
            width=30,
            show="*"
        )
        self.password_entry.pack(pady=5)

        # Login Button
        login_btn = tk.Button(
            root,
            text="Login",
            width=15,
            command=self.login
        )
        login_btn.pack(pady=15)

        self.logged_in = False

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if (
            username == self.admin_username
            and password == self.admin_password
        ):

            self.logged_in = True

            messagebox.showinfo(
                "Success",
                "Login Successful!"
            )

            self.root.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )


def authenticate():

    root = tk.Tk()

    app = LoginWindow(root)

    root.mainloop()

    return app.logged_in


if __name__ == "__main__":

    success = authenticate()

    if success:
        print("Access Granted")
    else:
        print("Access Denied")