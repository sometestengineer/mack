# test_1 checking if affid on checkout page appear as x-globalAffid
def test_affid(app):
    app.open_buy_now_page_with_params()
    app.buy.scroll_page_down()
    app.buy.push_instant_activation_button()
    result = app.shop.find_global_affid_in_url()
    assert result == 'x-globalAffid=123123123'


# test_2 checking if discount applying on checkout page
def test_discount_checkout(app):
    app.open_buy_now_page()
    app.buy.scroll_page_down()
    before_discount_price = app.buy.get_total_price_buy_page()
    app.open_buy_now_page_with_params()
    app.buy.scroll_page_down()
    app.buy.push_instant_activation_button()
    total_price = app.shop.get_total_price_check_out_page()
    assert float(before_discount_price) > float(total_price[1:])


# test_3 checking if discount delivered by url works on buy now page
def test_discount_buy_now_page(app):
    app.open_buy_now_page_with_params()
    app.buy.scroll_page_down()
    app.buy.push_instant_activation_button()
    discount = app.shop.discount_check_on_check_out_page()
    assert discount == True


# test_4 checking if discount coupon passed through discount field works on buy now page
def test_discount_coupon_buy_now_page(app):
    app.open_buy_now_page()
    app.buy.scroll_page_down()
    app.buy.fill_discount_field_buy_page()
    app.buy.push_instant_activation_button()
    full_price = app.shop.get_full_price_check_out_page()
    total_price = app.shop.get_total_price_check_out_page()
    assert (float(full_price[1:])) > float(total_price[1:])


# test_5 checking if "print of discount" is on buy now page, passing printOfDiscount in url
def test_print_of_discount_buy_now_page(app):
    app.open_buy_now_page_with_params()
    app.buy.click_print_of_discount_on_buy_page()
    app.buy.scroll_page_up()
    print_of_discount = app.buy.check_if_print_of_discount_on_buy_page()
    assert print_of_discount == True


# test_6 change currency on buy now page and check if it works on checkout page
def test_change_currency_checkout_page(app):
    app.buy.add_cookie_on_buy_page()
    app.open_buy_now_page()
    app.buy.scroll_page_down()
    app.buy.push_instant_activation_button()
    currency_sign = app.shop.get_total_price_check_out_page()
    assert currency_sign[:1] != u'\u20ac'  # euro

