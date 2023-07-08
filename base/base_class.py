import random


class Base:

    def __init__(self, driver):
        driver1 = driver
        self.driver = driver1

    """Method assert word"""

    def assert_text(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Correct value word")

    def generate_random_number(self, start, end):
        if start < 30 or end > 205 or start > end:
            random.randint(start, end)

        return random.randint(start, end)

    def assertions(self, value_1, value_2):
        assert value_1 == value_2
        print('Values are the same')

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Correct URL")
