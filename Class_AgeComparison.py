class Person:
    def __init__(self,initialAge):
        #Initialize the age
        if initialAge < 0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0")
        else:
            self.initialAge = initialAge

    def amIOld(self):
        #Check the person's age
        if self.initialAge < 13:
            print("You are young")
        elif self.initialAge in range(13, 19):
            print("You are a teenager")
        else:
            print("You are old")

    def yearPasses(self):
        #Increment age by 1 if a year passes
        self.initialAge = self.initialAge + 1

person1 = Person(20)
person1.amIOld()
person1.yearPasses()
