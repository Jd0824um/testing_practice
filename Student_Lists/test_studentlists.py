'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

from Labs.Student_Lists.studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    #Tests adding a student
    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    #Tests if a studen is already in a list
    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    #Tests removing a student
    def test_add_remove_student(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    #Tests tying to remove a student not in the list
    def test_remove_student_not_in_list(self):
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student('Test Student')

    #Tests if a student is enrolled
    def test_enrollment_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    #Tests if the list is empty if there are no students enrolled
    def test_enrollment_empty_list(self):
        test_class = ClassList(2)
        self.assertEqual(len(test_class.class_list), 0)

    #Tests if a student who isnt present is enrolled
    def test_enrollment_when_student_not_present(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertFalse(test_class.is_enrolled('Sean Bean'))
        self.assertFalse(test_class.is_enrolled('Martha Stewart'))

    #Tests string of multiple students are enrolled
    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', test_class.__str__())

    #Tests the string of an empty list
    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', test_class.__str__())

    #Tests the index of students present
    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertIsNotNone(test_class.index_of_student('Harry'))

    #Tests if the class is full
    def test_is_class_full(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')

        self.assertTrue(test_class.is_class_full())

        test_class.remove_student('Taylor Swift')

        self.assertFalse(test_class.is_class_full())

    #Tests if a student is not in a list
    def test_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')

        self.assertIsNone(test_class.index_of_student('Jim Beam'))
