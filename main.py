from ui import UI
from driver import BrowserDriver

driver = BrowserDriver()
ui = UI(driver)

driver.ui_callback = ui.stock_report_notice
