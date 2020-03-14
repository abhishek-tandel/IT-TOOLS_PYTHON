# Method overloading  with multiple classes(using super)


class overloading_sum:

    def area(self, a, b):
        print ('Area of box = ', a * b)


class derived_sum(overloading_sum):

    def area(self, a, b, c, ):
        super(derived_sum, self).area(10, 20)
        print ('Volume of box = ', a * b * c)


derived_sum_obj = derived_sum()

# derived_sum_obj.area(10, 20)  //won't work

derived_sum_obj.area(10, 20, 30)
