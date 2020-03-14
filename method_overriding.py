# Method overriding


class Employee:

    def add(self, salary, incentive):
        print ('Total salary in base class = ', salary + incentive)


class Department(Employee):

    temp = 'I am member of department class. '

    def add(self, salary, incentive):
        print self.temp
        print ('Total salary in derived class = ', salary + incentive)
        super(Department, self).add(salary, incentive)


dept = Department()
