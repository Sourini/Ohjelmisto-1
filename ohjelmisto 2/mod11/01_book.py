# Implement the following class hierarchy using Python: A publication can be either a book or a magazine.
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes. Create a print_information method to both subclasses
# for printing out all information of the publication in question. In the main program, create publications Donald Duck
# (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both
# publications using the methods you implemented.

class Bookstuff:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f'\n\nPublication name: {self.name}')

class Book(Bookstuff):
    def __init__(self, name, author, pc):
        self.author = author
        self.pc = pc
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f' Author: {self.author}\n Page count: {self.pc}')
class Magazine(Bookstuff):
    def __init__(self, name, ce):
        self.ce = ce
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f' Chief Editor: {self.ce}')

papery_things = []
papery_things.append(Book("Compartment No. 6", "Rosa Liksom", "192"))
papery_things.append(Magazine("Donald Duck", "Aki Hyyppä"))

for p in papery_things:
    p.print_information()