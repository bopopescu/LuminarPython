class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return book(self.pages+other.pages)

    def __sub__(self, other):
        return(self.pages-other.pages)

    def __str__(self):
        return str(self.pages)

    def __sub__(self):
        return book(self.pages-other.pages)

b=book(100)
b1=book(200)
b2=book(300)
print(b+b1+b2)
print(b-b1)