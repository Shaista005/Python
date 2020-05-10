class Person:
    def __init__(self, firstname, lastname, health, status):
        " initialize attributes to be used in/available for all\ class method in this class, and for class objects created by this class."

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def status_change(self):
        if self.health >= 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 76:
            print("{} is feeling little tired".format(self.firstname))
        elif self.health >= 50:
            print("{} is feeling unwell".format(self.firstname))
        elif self.health >= 25:
            print("{} goes to Doc".format(self.firstname))
        else:
            print("{} is unconsious".format(self.firstname))


Marian = Person("Marian", "Ted", 89, status=True)
Peter = Person("Peter", "Parker", 0 , status=False)

print("{} is my friend {}".format(Marian.firstname, Marian.status))
print("{} health score is {}".format(Marian.firstname, Marian.health))

Marian.introduce()
Peter.introduce()
Marian.status_change()
Peter.status_change()
