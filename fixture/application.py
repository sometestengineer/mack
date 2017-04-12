from selenium import webdriver
from fixture.buynowabel import BuyPage
from fixture.shoppingcart import ShopPage
import urllib


class Application:

    def __init__(self, browser):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)

        self.wd.implicitly_wait(5)  # needed when page loads dynamically, when element appear on page later
        self.buy = BuyPage(self)
        self.shop = ShopPage(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_buy_now_page(self):
        self.wd.get('http://mackeeper.com/buy-now-abel')

    def open_buy_now_page_with_params(self):
        params = {
            "lang": "en",
            "affid": "123123123",
            "couponcode": "lam4ik_test",
            "printOfDiscount": "discount5"
        }
        get_params = urllib.urlencode(params)
        self.wd.get('http://mackeeper.com/buy-now-abel?%s' % get_params)

    def destroy(self):
        self.wd.quit()
