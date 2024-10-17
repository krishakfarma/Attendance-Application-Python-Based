import tkinter as tk
import util


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        # Add login button
        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)

        # Add logout button
        self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)
        self.logout_button_main_window.place(x=750, y=300)

    def login(self):
        # Placeholder for login functionality
        print("Login button clicked")
        util.msg_box("Login", "Login button pressed!")

    def logout(self):
        # Placeholder for logout functionality
        print("Logout button clicked")
        util.msg_box("Logout", "Logout button pressed!")

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
