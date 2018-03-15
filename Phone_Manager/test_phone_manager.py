import unittest
from Labs.Phone_Manager.phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):


    #Test to creat and add a new phone
    def test_create_and_add_new_phone(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [testPhone1, testPhone2]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)

    #Test to check for duplicate id with a phone
    def test_create_and_add_phone_with_duplicate_id(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #ID is 1
        testPhone2 = Phone(1, 'Apple', 'iPhone 5') #ID is also 1

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError): #Should raise exception
            testAssignmentMgr.add_phone(testPhone2)

    #Test to create and add a new employee
    def test_create_and_add_new_employee(self):
        testEmployee1 = Employee(1, "Bob")
        testEmployee2 = Employee(2, "John")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        self.assertIn(testEmployee1, testAssignmentMgr.employees)
        self.assertIn(testEmployee2, testAssignmentMgr.employees)

    #Test to create and add dupliate employees with the same IDS
    def test_create_and_add_employee_with_duplicate_id(self):
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testEmployee1 = Employee(1, "Bob")
        testEmployee2 = Employee(1, "John")

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)

    def test_assign_phone_to_employee(self):
        testEmployee1 = Employee(1, "Bob")
        testEmployee2 = Employee(2, "John")

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, testEmployee1)
        testAssignmentMgr.assign(2, testEmployee2)

        self.assertTrue(testPhone1.employee_id == 1)
        self.assertTrue(testPhone2.employee_id == 2)

    #Tests phone id against the same phone already assigned to an employee
    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        testEmployee1 = Employee(1, "Bob")
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, testEmployee1)

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        testEmployee1 = Employee(1, "Bob")
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(testPhone1.id, testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, testEmployee1)

        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        self.fail()


    def test_un_assign_phone(self):

        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        self.fail()


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

        self.fail()