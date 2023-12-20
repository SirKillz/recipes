from tkinter import *


class RecipeButton(Button):
    def __init__(self, parent, recipe_key):
        super().__init__(parent)
        self.parent = parent
        self.recipe_key = recipe_key

        self.config(command=lambda: self.parent.add(recipe_key), text=recipe_key)


