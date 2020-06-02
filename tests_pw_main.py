"""Tests for pw_main.py using the unittest module."""

import unittest
import pw_main as pwm

class TestGetChars(unittest.TestCase):
    """Tests for the get_chars() function."""

    def test_list_of_chars(self):
        """Are all items in the returned list strings? Don't want e.g. other
        lists in the list."""
        returned = pwm.get_chars(upper=True, lower=True, numerals=True,
              specials=True, spaces=True, all_whitespace=True) # set all options to True
        for i in returned:
            self.assertIs(str, type(i))

    def test_letter_counts(self):
        """Are all 26 letters included where intended?"""
        upper = pwm.get_chars(upper=True, lower=False, numerals=False, # uppercase only
              specials=False, spaces=False, all_whitespace=False)
        lower = pwm.get_chars(upper=False, lower=True, numerals=False,  # lowercase only
              specials=False, spaces=False, all_whitespace=False)
        for i in [len(upper), len(lower)]:
            self.assertEqual(i, 26)

    def test_numerals_count(self):
        """Are there 10 elements in the list of numeral-strings?"""
        numerals = pwm.get_chars(upper=False, lower=False, numerals=True, # Numerals only
              specials=False, spaces=False, all_whitespace=False) 
        self.assertEqual(len(numerals), 10)

if __name__ == '__main__':
    unittest.main()
