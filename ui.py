from tkinter import *
from buttons import RecipeButton


class UI(Tk):
    def __init__(self, driver):
        super().__init__()
        self.stock_report()
        self.driver = driver
        # self.login()

        # Button Creation
        chili_button = RecipeButton(self, "chili")
        chili_button.pack()

        chicken_asparagus_button = RecipeButton(self, 'chickenAsparagusPesto')
        chicken_asparagus_button.pack()

        chicken_wildrice_button = RecipeButton(self, 'chickenWildriceSoup')
        chicken_wildrice_button.pack()

        self.mainloop()

    def stock_report(self):
        with open("stock_report.txt", mode="w") as file:
            file.write("Automated Stock Report")

    def append_stock_report(self, item_name):
        with open("stock_report.txt", mode="a") as file:
            file.write(f"\n\n{item_name} is Out of Stock")
