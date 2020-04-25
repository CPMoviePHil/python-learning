
class MyGenerator:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            self.current = self.current + 1
            return self.current
        raise StopIteration


test1 = MyGenerator(1, 100)
for i in test1:
    print(i)
