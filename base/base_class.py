class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method assert word"""
    def assert_text(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Correct value word")