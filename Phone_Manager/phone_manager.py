# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        #Raises an exception if 2 or more employees are have this ID
        for emp in self.employees:
             if employee.id == emp.id:
                raise PhoneError('A different employee already has this ID')

        self.employees.append(employee)


    def add_phone(self, phone):
        #Raises an exception if 2 or more phone have this ID

        for p in self.phones:
            if phone.id == p.id:
                raise PhoneError('A different phone already has this ID')

        self.phones.append(phone)


    def assign(self, phone_id, employee):
        for phone in self.phones:
            if phone.id == phone_id:

                if phone.employee_id is None:
                    phone.assign(employee.id)
                    return
                if phone.employee_id == employee.id: #Raises an exception if this phone is already assigned to the employee
                    raise PhoneError("This phone is already assigned to this employee")
                if phone.employee_id is not None:  # Raises an exception if a phone is already assigned to an employee
                    raise PhoneError("A phone is already assigned to this employee")


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        if self.employees.__contains__(employee):
            for phone in self.phones:
                if phone.employee_id == employee.id:
                    return phone
                else:
                    return None
        else:
            raise PhoneError("Employee does not exist")

        return None


class PhoneError(Exception):
    pass
