class University:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def display_details(self):
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            department.display_details()


class Department(University):
    def __init__(self, name, head_of_department):
        super().__init__(name, None)  
        self._head_of_department = head_of_department
        self._courses_offered = []

    def add_course(self, course):
        self._courses_offered.append(course)

    def display_details(self):
        print(f"Department Name: {self._name}")
        print(f"Head of Department: {self._head_of_department}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f"  - {course}")

university = University("Tribhuvan University", "Kathmandu")
dept1 = Department("Computer Science", "Prof. X")
dept1.add_course("Object Oriented Programming")
dept1.add_course("Data Structures")
dept2 = Department("Civil Engineering", "Prof. Y")
dept2.add_course("Structural Engineering")
dept2.add_course("Hydropower")

university.add_department(dept1)
university.add_department(dept2)

university.display_details()
dept1.display_details()
