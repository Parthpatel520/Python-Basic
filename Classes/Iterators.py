a = "parth"

b = iter(a)
print(next(b))
print(next(b))
print(next(b))

class Test:

    def __init__(self):
        self.num = 3   # define num

    def __next__(self):
        if self.num == 0:
            raise StopIteration
        self.num -= 1
        return self.num

t = Test()

print(next(t))
print(next(t))


class Test:

    def __init__(self):
        self.name ="parth"
        self.num = 0

    def __iter__(self):
        return self   # makes object iterable

    def __next__(self):
        if self.num >= len(self.name): # self.name = "parth"  len(self.name) = 5
            raise StopIteration
        value = self.name[self.num]  # value = self.name[0] = "p"
        self.num += 1   
        return value


t = Test()

for value in t:
    print(value)


# next(object) calls this function automatically.