from base.base_functions import BaseFunctions


class LeverPage(BaseFunctions):
    URL = "lever.co"

    def __init__(self, driver):
        super().__init__(driver)

    def is_lever_page_opened(self):
        return self.URL in self.get_url()

    def switch_lever_tab(self):
        self.switch_tab()
