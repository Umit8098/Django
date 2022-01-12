import os
os.system('cls' if os.name == 'nt' else 'clear')


# def printtype(data):
#     for i in data:
#         print(i, type(i))

# test = [123, "Barry", [1, 2, 3], (1,2,3), {1, 2, 3}, True, lambda x: x, {"name": 'harry', "age": 38}]

# # printtype(test)


# ## Defining Classes:

# class Person:
#     name = 'Barry'
#     age = 44

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)   

# Person.job = 'teacher'
# print(person1.job)
# print(person2.job)   


## Class attributes ve instance attributes

# Person.name = 'Rafe'
# person1.name = 'Henry'
# print(person1.name)
# print(person2.name)   



## SELF Keyword

# class Person:
#     name = 'Barry'
#     age = 44
    
#     def test(self):
#         print("test")
        
#     def get_details(self):
#         print('name:', self.name, ' age:', self.age, ' location:', self.location)
    
#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location


# person1 = Person()
# person1.test()
# Person.test(person1)
# person1.set_details('Henry', 38, 'Ankara')
# person1.get_details()









# class Person:
#     name = 'Barry'
#     age = 44
            
#     def get_details(self):
#         print('name:', self.name, ' age:', self.age, ' location:', self.location)
    
#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
    
#     @staticmethod
#     def salute():
#         print('Hi There!', Person.name)


# Person.salute()
# person1 = Person()
# person1.set_details('Rafe', 39, 'Istanbul')
# person1.salute()




# //////////////////////////////////////////////////////////




## Special Methods : >>>>>

## constracture fonksiyon __init__


# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    

# person1 = Person('Barry', 44)
# print(person1.name, person1.age)

# person2 = Person('Rafe', 39)
# print(person2.name, person2.age)





## constracture fonksiyon __str__

# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"

# person1 = Person('Barry', 44)


# list = [1, 2, 3]
# print(list)
# print(person1)





## constracture fonksiyon __len__

# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"
    
#     def __len__(self):
#         return self.age

# person1 = Person('Barry', 44)


# list = [1, 2, 3]
# print(len(list))
# print(len(person1))
# print(person1.__len__())



# //////////////////////////////////////////////////////////


## Bir kodun Object oriented olabilmesi için 4 özelliğinin olması lazım:

## 1.abstraction and 2.encapsulation : >>>>>>>

## abstraction : sort() metodu bunu nasıl yapıyor bilmiyoruz, buna abstraction diyoruz.

# list = [3, 2, 5, 9, 1]
# list.sort()
# print(list)



## encapsulation : 
## _id = 5000   değiştirebilirsin ama değiştirmesen iyi olur.
## __id = 4000   değiştirmemalisin.
## __id = 4000   değiştirmesen iyi olur. ama illa değiştireceklerse de şunu yapmaları gerekir. >>>>     person1._Person__id1 = 2000
#                           print(person1._Person__id1)




# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id1 = 4000
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"

# person1 = Person("Rafe", 39)
# print(person1._id)
# person1._id = 3000
# print(person1._id)


# person1._id1 = 3000
# print(person1.__id1)


## person1 = Person("Rafe", 39)
## person1._Person__id1 = 2000
## print(person1._Person__id1)





## 3.inheritance and 4.polymorphism : >>>>>>>
##    kalıtım: bir classtan yeni classlar türetilmesi

class Person:
    company = "Clarusway"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}   Age: {self.age}    Path: {self.path}"

class Employee(Person):
    
    def __init__(self, name, age, path):
        self.name = name
        self.age = age
        self.path = path
    
    # bu class'ın içinde __str__ diye bir method yok ama inheritance kalıtım kapsamında yukarıdan geliyor.


emp1 = Employee('Barry', 44, 'FS')
print(emp1)

