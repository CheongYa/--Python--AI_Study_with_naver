# Function and Console I/O

# 함수의 개요 / 어떤 일을 수행하는 코드의 덩어리
'''
- 반복적인 수행을 1회만 적성 후 호출
- 코드를 논리적인 단위로 분리
- 캡슐화 : 인터페이스만 알면 타인의 코드 사용
'''
##
# def calculate_rectangle_area(x, y): # def 함수 이름(parameter(input값), ..., ...)
#     return x * y

# rectangle_x = 10 # 수행문 
# rectangle_y = 20
# print("사각형 x의 길의 : ", rectangle_x) # 반환값
# print("사각형 y의 길의 : ", rectangle_y)
# print("사각형의 넓이 : ", calculate_rectangle_area(rectangle_x, rectangle_y))

##
# def f(x): # x 의 위치 = parameter
#     return 2 * x + 7

# def g(x):
#     return x ** 2

# x = 2
# print(f(x) + g(x) + f(g(x)) + g(f(x))) # X 의 위치 = argument: 실제 parameter에 대입된 값

##
# def a_calculateRectangleArea(): # parameter 없고, 반환 값 없을 때 = 함수 내의 수행문만 수행
#     print(5 * 7)

# def b_calculateRectangleArea(x, y): # parameter 있고, 반환 값 없을 때 = parameter를 사용, 수행문만수행
#     print(x * y)

# def c_calculateRectangleArea(): # parameter 없고, 반환 값 있을 때 = parameter없이, 수행문 수행 후 결과값 반환
#     return 5 * 7

# def d_calculateRectangleArea(x, y): # parameter 있고, 반환 값 있을 때 = parameter를 사용하여 수행문 수행 후 결과값 반환
#     return x * y

# a_calculateRectangleArea()
# b_calculateRectangleArea(5, 7)
# print(c_calculateRectangleArea())
# print(d_calculateRectangleArea(5, 7))


# old-school formatting
# print('%s %s' %('one', 'two'))  # %-format = "%ddatatype" % (variable) 형태
# print('{1} {0}'.format('one', 'two')) # "~~~{datatype}~~~".format(argument) 형태
# print("%d %d" % (1, 2))
# print("{} {}".format(1, 2))

# padding / 여유 공간을 지정하여 글자배열 + 소수점 자수를 맞추기
# print("Product: %5s, Price per unit: %.5f." % ("Apple", 5.243))
# print("Product: {0:5s}, Price per unit: {1:.5f}.".format("Apple", 5.243))
# print("Product: %10s, Price per unit: %10.3f." % ("Apple", 5.243))
# print("Product: {0:>10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))

# f-string
# name = "CheongYa"
# age = 23
# print(f"Hello, {name}. You are {age}.")
# print(f'{name:20}') # 20칸
# print(f'{name:>20}') # 20칸이며 오른쪽에 name 출력
# print(f'{name:*<20}') # 20칸이며 왼쪽에 name, 오른쪽에 * 출력
# print(f'{name:*>20}') # 20칸이며 오른쪽에 name, 왼쪽에 * 출력
# print(f'{name:*^20}') # 20칸이며 중앙에 name, 양 옆에 * 출력

# number = 3.141592653589793
# print(f'{number:.2f}')

a = float(input())
b = ((9/5) * a) + 32
print(f"섭씨 온도 : {a:.2f}")
print(f"화씨 온도 : {b:.2f}")