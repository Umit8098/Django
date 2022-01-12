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

# # 1. kısım

# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"

# class Employee(Person):
    
#     def __init__(self, name, age, path):
#         self.name = name
#         self.age = age
#         self.path = path
    
#     # bu class'ın içinde __str__ diye bir method yok ama inheritance kalıtım kapsamında yukarıdan geliyor.

# emp1 = Employee('Barry', 44, 'FS')
# print(emp1)





# # 2. kısım
# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"

# class Employee(Person):
    
#     def __init__(self, name, age, path):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         # super().__init__(name, age) ile; sen kimden türetildi isen git onun init fonksiyonunu çalıştır. Ancak yukarıdaki init ihtiyacımızı karşılamıyorsa kendimiz de baştan init yazabiliriz.
#         self.path = path
    
# emp1 = Employee('Barry', 44, 'FS')
# print(emp1)





## 4.polymorphism : (evet ben seni yukarıdan inherit etttim ama yukarıdaki buradaki örnekte __str__ artık benim işime yaramıyor, benim seni override edip yeniden yazabiliyor olmam lazım buna da polymorphisim denir, yukarıdaki methodu değiştirebilme yeniden tanımlayabilme polymorphisim oluyor. ) İnherit ettiğimiz methodları kullanmayıp istediğimiz biçimde değiştiriyoruz.


# # 1.kısım
# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"
    
#     def details(self):
#         print(f"Name: {self.name}    Age: {self.age}")

# class Employee(Person):
    
#     def __init__(self, name, age, path):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         self.path = path
        
#     # override yapıyoruz (Yukarıdaki str'ı ezdik.) Gerçi __str__ special method olduğu için anlaşılmıyor o yüzden alttaki details kısmını incele! 
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}   Path: {self.path}"
    
#      # override (Yukarıdaki details methodu işimize yaramıyor (path'i de ilave etmek istiyoruz ama yukarıda path yok), biz de override ediyoruz, değiştiriyoruz.)
#     def details(self):
#         print(f"Name: {self.name}   Age: {self.age}   Path: {self.path}")
    
# emp1 = Employee('Barry', 44, 'FS')
# # print(emp1)
# emp1.details()




# 2.kısım
# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"
    
#     def details(self):
#         print(f"Name: {self.name}\nAge: {self.age}")

# class Employee(Person):
    
#     def __init__(self, name, age, path):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         self.path = path

#     # override
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}   Path: {self.path}"
    
#     # override (Bu 2. kısımda da yukarıdan inherit ettiğimiz kısımlara ilave yapmak istiyorsak super ile yukarıyı alıp ona ilave edeceklerimizi override edebiliyoruz.)
#     def details(self):
#         super().details()
#         print(f"Path: {self.path}")
    
# emp1 = Employee('Barry', 44, 'FS')
# # print(emp1)
# emp1.details()

# # mro() bize soy ağacını çıkarıyor.
# print(Employee.mro())







# # Multiple Inheritance (bir class' ı iki farkı class tan türetebiliyoruz. Bir class iki farklı class tan inherite edebilir. Birden fazla class'ı alıp o classlardan yeni bir class türetebiliyoruz.)
# class Person:
#     company = "Clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}"
    
#     def details(self):
#         print(f"Name: {self.name}\nAge: {self.age}")

# class Lang:
#     def __init__(self, langs):
#         self.langs = langs

# class Employee(Person, Lang):
    
#     def __init__(self, name, age, path):
#         super().__init__(name, age)
#         Lang.__init__(self, ["Python", "Js"])
#         self.path = path

#     # override
#     def __str__(self):
#         return f"Name: {self.name}   Age: {self.age}   Path: {self.path}"
    
#     # override 
#     def details(self):
#         super().details()
#         print(f"Path: {self.path}")
#         print(f"Langs: {self.langs}")
    
# emp1 = Employee('Barry', 44, 'FS')
# emp1.details()

# # mro() bize soy ağacını çıkarıyor.
# print(Employee.mro())







# # inner class (class içinde class ve bunun ismi hep Meta olacaktır djangoda standarrttır.)

# from django.db import models

# class Article(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
    
#     class Meta:
#         ordering = ["last_name"]






# örnek
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__id = 1234
        self.movements = []
        
    def __str__(self):
        return f"Name : {self.name}  id : {self.__id}"
    
    def add_movement(self, amount, date, explain):
        self.movements.append({"amount": amount, "date": date, "explain": explain})
    
    def all_movements(self):
        for i in self.movements:
            print(i["date"], i["amount"], i["explain"])
    
    def balance(self):
        # total = 0
        # for i in self.movements:
        #     total += i["amount"]
        # print(total)
        return sum(i["amount"] for i in self.movements)

custom = Customer("barry", 44)
print(custom)
custom.add_movement(5000, "15.10.2021", "Salary")
custom.add_movement(-1000, "16.10.2021", "Rent")
custom.add_movement(-500, "16.10.2021", "Bills")
custom.add_movement(-2000, "16.10.2021", "Credite Card")
custom.all_movements()
# custom.balance()
print(custom.balance())




