class Even_Numbers:

    def __init__(self, start, end):
        self.start = start
        if self.start % 2 == 0:
            self.start += 2
            self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
                    raise StopIteration
        else:
            current = self.start
            self.start +=2
            return current
for i in Even_Numbers(10,25):
    print(i)
