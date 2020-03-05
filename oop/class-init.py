class TestClass:
    param2 = 'param2'

    def print_self(self):
        self.param2 = 'wtf'
        return self.param2

    def print_self2(self):
        # TestClass.param2 = 'hello'
        # return TestClass.param2
        print(self)


class EmptyObject:
    pass


# test1 = TestClass
# test2 = test1()
# print(test2.param2)
# print(test2.print_self2())
new_empty_obj = EmptyObject()
TestClass.print_self2(new_empty_obj)
