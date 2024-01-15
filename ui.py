import tkinter.messagebox
from tkinter import *
from buttons import RecipeButton
from tkinter import messagebox


class UI(Tk):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

        self.out_of_stock = []

        # Button Creation
        chili_button = RecipeButton(self, "chili")
        chili_button.pack()

        chicken_asparagus_button = RecipeButton(self, 'chickenAsparagusPesto')
        chicken_asparagus_button.pack()

        chicken_wildrice_button = RecipeButton(self, 'chickenWildriceSoup')
        chicken_wildrice_button.pack()

        notice_button = Button(text="Test", command=self.stock_report_notice)
        notice_button.pack()


        self.mainloop()

    def stock_report_notice(self, oos_list):
        if len(oos_list) == 0:
            notice = "All items were in stock, and there were no substitutes."
        else:
            stock_string = "\n".join(oos_list)
            notice = f"Out of Stock:\n{stock_string}"
            tkinter.messagebox.showinfo(title="Stock Report", message=notice)


    def append_stock_report(self, item_name):
        with open("stock_report.txt", mode="a") as file:
            file.write(f"\n\n{item_name} is Out of Stock")
