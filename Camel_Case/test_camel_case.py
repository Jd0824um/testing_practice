from unittest import TestCase
from Labs.Camel_Case.camel_case import alternate_case


'''python -m unittest test.py from command prompt'''


class TestFunctions(TestCase):

    #Tests for correct alternate case
    def test_alternate_case(self):
        self.assertEqual('hElLo', alternate_case('hello'))
        self.assertEqual('mY NaMe iS JoHn.', alternate_case('My naMe iS JOHN.'))

    #Tests for special characters still being added to the string and not effecting
    #the camel case
    def test_special_characters(self):
        self.assertEqual('aSdFaWsDfAn!@$aSfGmDbAdFeAs', alternate_case('asdfawSDFAn!@$ASFGMDBADfeas'))

    #Tests for an empty string
    def test_empty_string(self):
        self.assertTrue(' ', alternate_case(' '))
    #Tests string for numbers
    def test_numbers(self):
        self.assertEqual('t00L Sh0p', alternate_case('t00l sh0P'))

