from selenium.webdriver.common.keys import Keys


class BuyPage:

    def __init__(self, app):
        self.wd = app.wd

    def push_instant_activation_button(self):
        self.wd.find_element_by_css_selector('button.btn').click()

    def scroll_page_down(self):
        elm = self.wd.find_element_by_tag_name('button')
        elm.send_keys(Keys.PAGE_DOWN)

    def get_total_price_buy_page(self):
        return self.wd.find_element_by_css_selector('span.js-total_price.js-price_eur').text

    def fill_discount_field_buy_page(self):
        self.wd.find_element_by_css_selector('p.coupon__have-coupon.js-coupon_link').click()
        self.wd.find_element_by_id('coupon').click()
        self.wd.find_element_by_id('coupon').clear()
        self.wd.find_element_by_id('coupon').send_keys('lam4ik_test')

    def check_if_print_of_discount_on_buy_page(self):
        if len(self.wd.find_elements_by_css_selector('p.type')) > 0:
            return True
        else:
            return False

    def click_print_of_discount_on_buy_page(self):
        self.wd.find_element_by_css_selector('p.type').click()

    def scroll_page_up(self):
        elm = self.wd.find_element_by_tag_name('html')
        elm.send_keys(Keys.HOME)

    def add_cookie_on_buy_page(self):
        self.wd.get('http://.mackeeper.com')
        self.wd.delete_cookie('priceCode')
        self.wd.add_cookie({'name': 'priceCode', 'value': 'USD',
                       'domain': '.mackeeper.com', 'path': '/'})