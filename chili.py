from item import RecipeItem

ground_turkey = RecipeItem(url="https://www.meijer.com/shopping/product/jennie-o-turkey-store-lean-ground-turkey-93-lean-16-oz/4222230200.html",
                           add_xpath='//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button/span',
                           in_cart_xpath='//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/select')

black_beans = RecipeItem(url="https://www.meijer.com/shopping/product/meijer-black-beans-15-25-oz/4125096392.html",
                         add_xpath='//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button',
                         in_cart_xpath='//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/select')

chicken = RecipeItem(url="https://www.meijer.com/shopping/product/meijer-thick-sliced-hardwood-smoked-bacon-16-oz/71928383460.html",
                     add_xpath='//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button/span',
                     in_cart_xpath='//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/select')


chili = [ground_turkey, black_beans, chicken]