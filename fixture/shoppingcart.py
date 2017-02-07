import re


class ShopPage:

    def __init__(self, app):
        self.wd = app.wd

    def find_global_affid_in_url(self):
        target_url = self.wd.current_url
        result = re.search('x-globalAffid=123123123', target_url).group()
        return result

    def get_total_price_check_out_page(self):
        return self.wd.find_element_by_id('cbp_ID0ENA_ID0EAAABAAIABAAOA').text

    def discount_check_on_check_out_page(self):
        if len(self.wd.find_elements_by_id('cbp_ID0EAKNA_ID0EAACMAAABADBAAOA')) > 0:
            return True
        else:
            return False

    def get_full_price_check_out_page(self):
        if self.discount_check_on_check_out_page():
            return self.wd.find_element_by_id('cbp_ID0EAKNA_ID0EAACMAAABADBAAOA').text
