import random


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method assert word"""

    def assert_text(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Correct value word")

    def generate_random_number(self, start, end):
        if start < 30 or end > 205 or start > end:
            random.randint(start, end)

        return random.randint(start, end)
