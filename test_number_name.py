import unittest
from numbername import number_name


class TestParameter(unittest.TestCase):
    def test_if_parameter_is_integer(self):
        assert number_name("8") == {8: "oito"}

    def test_if_parameter_is_string(self):
        assert number_name("error") == "You must provide a integer number."

    def test_if_parameter_is_float(self):
        assert number_name("8.5") == "You must provide a integer number."

    def test_if_in_range(self):
        assert number_name("8") == {8: "oito"}

    def test_out_of_range(self):
        assert number_name("800000") == "This number is out of range [-99999, 99999]"


if __name__ == '__main__':
    unittest.main()
