from unittest import TestCase
from Labs.lab_4 import alternate_case


'''python -m unittest test.py from command prompt'''


class TestFunctions(TestCase):

    def test_alternate_case(self):
        self.assertEqual('hElLo', alternate_case('hello'))
        self.assertEqual('mY NaMe iS JoHn.', alternate_case('My naMe iS JOHN.'))

    def test_special_characters(self):
        self.assertEqual('aSdFaWsDfAn!@$aSfGmDbAdFeAs', alternate_case('asdfawSDFAn!@$ASFGMDBADfeas'))

    def test_empty_string(self):
        self.assertTrue(' ', alternate_case(' '))

