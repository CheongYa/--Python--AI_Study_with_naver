# Python Object Oriented Programming(OOP = 객체지향 프로그래밍) 강의

# class 구현하기 in Python
## 축구 선수 정보를 Class로 구현하기
# class SoccerPlayer(object): # class 예약어, class 이름, 상속받는 객체명(안적어줘도 일어나긴 함)
#     # Attribute 추가하기
#     def __init__(self, name : str, position : str, back_number : int): # __init__ 은 객체 초기화 예약 함수, slef = 생성된 instance 자신
#         # __ 는 특수한 예약 함수나 변수 그리고 함수명 변경(맨글링)으로 사용. ex) __main__, __add__, __str__, __eq__
#         self.name = name # self. 으로 객체의 초기 정보 선언
#         self.position = position
#         self.back_number = back_number

#     def __str__(self):
#         return "Hello, My name is %s. My back number is %d" % \
#             (self.name, self.back_number)

#     def __add__(self, other):
#         return self.name + other.name

#     def change_back_number(self, new_number):
#         print("선수의 등번호를 변경합니다 : From %d to %d" % \
#             (self.back_number, new_number))
#         self.back_number = new_number


# son = SoccerPlayer("son", "FW", 7)
# park = SoccerPlayer("park", "WF", 13)

# print(son)
# son.change_back_number(10)
# print(son)
# print(son+park)


# 구현 가능한 OOP 만들기 - 노트북
# from teamlab_note import Note
# from teamlab_note import NoteBook

# my_notebook = NoteBook("팀랩 강의노트")
# print(my_notebook.title)
# new_note = Note("아 수업 하기 싫다.")
# print(new_note)
# new_note_2 = Note("파이썬 강의")
# print(new_note_2)
# my_notebook.add_note(new_note)
# my_notebook.notes[2] = Note("안녕")
# print(my_notebook.get_number_of_pages())
# print(my_notebook.notes[1])


# OOP characteristics
## 상속 (Inheritance) / 부모클래스로 부터 속성과 Method를 물려받은 자식 클래스를 생성하는 것
# class Person(object):
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def about_me(self):
#         print("저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다.")

#     def __str__(self):
#         return "저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다."

# class Employee(Person):
#     def __init__(self, name, age, gender, salary, hire_date):
#         super().__init__(name, age, gender) # 부모객체 사용
#         self.salary = salary
#         self.hire_date = hire_date
    
#     def do_work(self):
#         print("열심히 일을 합니다.")
    
#     def about_me(self): # 부모 클래스 함수 재정의
#         super().about_me() # 부모 클래스 함수 사용
#         print("제 급여는 ", self.salary, "원 이구요, 제 입사일은 ", self.hire_date, " 입니다.")

# myPerson = Person("Cheong", 23, "Male")
# myPerson.about_me()
# myEmployee = Employee("Choeng", 23, "Male", 300, "2022/12/20")
# myEmployee.about_me()

## 다형성(Polymorphism) / 같은 이름 메소드의 내부 로직을 다르게 작성
# class Aniaml:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Cat(Aniaml):
#     def talk(self):
#         return 'Neow!'

# class Dog(Aniaml):
#     def talk(selk):
#         return "Woof! Woof!"

# animals = [Cat('Missy'), Cat('Mr.Mistoffelees'), Dog('Lassie')]

# for animal in animals:
#     print(animal.name + ': ' + animal.talk())

## 가시성(Visibility) / 객체의 정보를 볼 수 있는 레벨을 조절하는 것. 누구나 객체 안에 모든 변수를 볼 필요가 없음.
### 가시성 설정 안 했을 때
# class Product():
#     pass

# class Inventory():
#     def __init__(self):
#         self.items = []
#         self.test = "abc"
    
#     def add_new_item(self, product):
#         if type(product) == Product:
#             self.items.append(product)
#             print("new item added")
#         else:
#             raise ValueError("Invalid Item")

#     def get_number_of_items(self):
#         return len(self.__items)

# my_inventory = Inventory()
# my_inventory.add_new_item(Product())
# my_inventory.add_new_item(Product())
# my_inventory.items.append("abc") # 프로덕트 외에 외부에서 마음대로 접근 가능
# print(my_inventory.items)

### 설정 했을 때
# class Product():
#     pass

# class Inventory():
#     def __init__(self):
#         self.__items = [] # Private 변수로 선언. 타객체가 접근 못함.
    
#     def add_new_item(self, product):
#         if type(product) == Product:
#             self.__items.append(product)
#             print("new item added")
#         else:
#             raise ValueError("Invalid Item")

#     def get_number_of_items(self):
#         return len(self.__items)

# my_inventory = Inventory()
# my_inventory.add_new_item(Product())
# my_inventory.add_new_item(Product())
# # my_inventory.items.append("abc") # 접근이 되지 않음. 에러 발생
# print(my_inventory.items)

### 접근 허용하게 하는 코드
# class Product():
#     pass

# class Inventory():
#     def __init__(self):
#         self.__items = [] # Private 변수로 선언. 타객체가 접근 못함.
    
#     def add_new_item(self, product):
#         if type(product) == Product:
#             self.__items.append(product)
#             print("new item added")
#         else:
#             raise ValueError("Invalid Item")

#     def get_number_of_items(self):
#         return len(self.__items)

#     @property # 내부에 있는 객체를 접근할 수 있게끔 해줌.
#     def items(self):
#         return self.__items

# my_inventory = Inventory()
# my_inventory.add_new_item(Product())
# my_inventory.add_new_item(Product())
# my_inventory.items.append("abc")
# print(my_inventory.items)


# decorate
## First-class objects
'''
- 일등함수 또는 일급 객체
- 변수나 데이터 구조에 할당이 간능한 객체
- 파라메터로 전달이 가능 + 리턴 값으로 사용
⭐ 파이썬의 함수는 일급함수
'''
# def square(x):
#     return x * x

# def cube(x):
#     return x*x*x

# def formula(method, argument_list):
#     return [method(value) for value in argument_list]

# f = cube # 함수를 변수로 사용
# print(f(5))

## Inner function / 함수 내에 또 다른 함수가 존재
# def print_msg(msg):
#     def printer():
#         print(msg)
#     printer()

# print_msg("Hello, Python")

### closures : inner function을 return 값으로 반환
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer

# another = print_msg("Hello, Python")
# another()

#### closures example
# def tag_func(tag, text):
#     text = text
#     tag = tag

#     def inner_func():
#         return '<{0}>{1}<{0}>'.format(tag, text)
    
#     return inner_func

# h1_func = tag_func('title', "This is Python Class")
# p_func = tag_func('p', "Data Academy")
# print(h1_func())
# print(p_func())

#### closures example 2
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner

# @star
# def printer(msg):
#     print(msg)
# printer("Hello")

#### closures example 3
# def generate_power(exponent):
#     def wrapper(f):
#         def inner(*args):
#             result = f(*args)
#             return exponent**result
#         return inner
#     return wrapper

# @generate_power(2)
# def raise_two(n):
#     return n**2

# print(raise_two(7))

data_list = (1, 2, 3, 4, 5, 6)

def f(x):
    return x ** 5

print([f(value) for value in data_list])