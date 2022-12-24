# Conditionals and Loops

# if-else 문
# print("Tell me your age?")
# myage = int(input())
# if myage < 30:
#     print("Welcome to the Club")
# else:
#     print("Oh! No. You are not accepted")

# 논리 키워드 : and, or, not
# a = True
# b = True
# c = False
# print(a and b)
# print(a and c)
# print(a or c)

# boolean_list = [True, False, True, False, True]
# print(all(boolean_list)) # and
# print(any(boolean_list)) # or

# 삼항 연산자(Ternary operators) / 조건문을 사용하여 참일 경우와 거짓을 경우의 결과를 한줄에 표현
# value = 12
# is_envn = True if value % 2 == 0 else False # value 를 2로 나눈 값의 나머지가 0 이라면 Frue 아니라면 False 출력
# print(is_envn)

# 조건 판단 연습
# score = int(input())
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print(grade)

# [연습] 무슨 학교 다니세요? / 태어난 연도를 계산하여 학교 종류를 맞추는 프로그램
# a = int(input("당신이 태어난 년도를 입력하세요: "))
# b = 2022 - a + 1
# if 26 >= b and b >= 20:
#     print("대학생")
# elif 20 > b and b >= 17:
#     print("고등학생")
# elif 17 > b and b >= 14:
#     print("중학생")
# elif 14 > b and b >= 8:
#     print("초등학생")
# else:
#     print("학생이 아닙니다")

# 반복문 / 정해진 동작을 반복적으로 수행하게 하는 명령문
# for문
# for looper in [1, 2, 3, 4, 5]:
#     print(f"{looper} : Hello")

# for looper in range(0, 5):
#     print("Hi")

# print(list(range(5)))

# for looper in range(0, 5):
#     print(f"{looper} : Hello")

# for i in range(10, 1, -1):
#     print(i)

# while문 / 조건이 만족하는 동안 반복 명령문을 수행
# i = 0
# while i < 10:
#     print(f"{i} : Hello")
#     i += 1

# 반복의 제어 - break, continue
# for i in range(10):
#     if i == 5:
#         break  # i가 5라면 반복문을 빠져나감
#     print(i)
# print("EOP")

# for i in range(10):
#     if i == 5:
#         continue  # i가 5라면 반복문으로 돌아감
#     print(i)
# print("EOP")

# [연습] 구구단 계산기
# print("구구단 몇단을 계산할까요?")
# dan = input()
# print("구구단 " + str(dan) + "단을 계산합니다.")
# # print(f"구구단 {dan}단을 계산합니다.")
# dan = int(dan)
# for i in range(1, 10):
#     print(dan, "X", i, "=", dan*i)
#     # print(f"{dan} X {i} = {dan*i}")

# loop review
##
# sentence = "I love you"
# reverse_sen = ""

# for char in sentence:
#     print("REVERSE #1 ", reverse_sen)
#     reverse_sen = char + reverse_sen
#     print("REVERSE #2 ", reverse_sen)

##
# decimal = int(input("십진수를 입력해주세요 : "))
# result = ""

# while decimal > 0:
#     remainder = decimal % 2 # 나머지
#     decimal = decimal // 2 # 몫
#     result = str(remainder) + result
#     print(f"decimal value : {decimal}")
# print(result)

# loop&control lab
## [연습] 숫자 찾기 게임
# import random

# true_value = random.randint(1, 100)

# print("숫자를 맞춰보세요 (1~100)")
# while True:
#     call = int(input())
#     if true_value == call:
#         print(f"정답입니다. 입력한 숫자는 {call}입니다")
#         break
#     elif true_value >= call:
#         print("숫자가 너무 작습니다")
#     else:
#         print("숫자가 너무 큽니다")

## [연습] 연속적인 구구단 입력
# while True: # while true 는 그렇게 좋은 방식이 아님. 무한반복이 될 수 있기 때문. 어쩔 수 없을 때만 쓸 것.
#     print("구구단 몇 단을 계산할까요(1~9)?")
#     dan = int(input())
#     if dan >= 1 and dan <= 9:
#         print(f"구구단 {dan}단을 계산합니다.")
#         for i in range(1, 10):
#             print(f"{dan} X {i} = {dan*i}")
#     elif dan == 0:
#         print("구구단 게임을 종료합니다.")
#         break
#     else:
#         print("잘못 입력하셨습니다.")

## [연습] 이차원 리스트 처리하기
# kor_score = [49, 79, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
# midterm_score = [kor_score, math_score, eng_score]

# student_score = [0, 0, 0, 0, 0]
# i = 0

# for subject_score in midterm_score:
#     for personal_score in subject_score:
#         student_score[i] += personal_score
#         i += 1
#     i = 0

# i = 0
# for value in student_score:
#     print(f"{i}번째 사람의 평균점수는 {(value/3):.2f}점입니다.")
#     i += 1


# String and advanced function concept 강의
## String
# f = open("youarenotalone.txt", "r")
# youarenotalone_jack = ""
# while True:
#     line = f.readline()
#     if not line:
#         break
#     youarenotalone_jack = youarenotalone_jack + line.strip() + "\n"
# f.close()
# print(youarenotalone_jack)

# n_of_alone = youarenotalone_jack.upper().count("ALONE") # 대소문자 구분 제거
# print("Number of a Word 'alone'", n_of_alone)

## function II
### call by object reference
'''
함수에서 parameter를 전달하는 방식
1. 값에 의한 호출(Call by Value)
함수에 인자를 넘길 때 값만 넘김.
함수 내에 인자 값 변경 시, 호출자에게 영향을 주지 않음.
2. 참조의 의한 호출(Call by Reference)
함수에 인자를 넘길 때 메모리 주소를 넘김.
함수 내에 인자 값 변경 시, 호출자의 값도 변경됨.
3. 객체 참조에 의한 호출(Call by Object Reference)
객체의 주소가 함수로 전달되는 방식.
전달된 객체를 참조하여 변경 시 호출자에게 영향을 주나, 새로운 객체를 만들 경우 호출자에게 영향을 주지 않음.
'''
# def spam(eggs):
#     eggs.append(1) # 기존 객체의 주소값에 [1] 추가
#     eggs = [2, 3] # 새로운 객체 생성
#     print(eggs)

# ham = [0]
# spam(ham)
# print(ham)

## swap
# def swap_value(x, y):
#     temp = x
#     x = y
#     y = temp

# def swap_offset(offset_x, offset_y):
#     temp = a[offset_x]
#     a[offset_x] = a[offset_y]
#     a[offset_y] = temp

# def swap_reference(list, offset_x, offset_y):
#     temp_list = list[:] # 리스트의 값을 복사를 시작하는게 많이 중요함.
#     temp = list[offset_x]
#     list[offset_x] = list[offset_y]
#     list[offset_y] = temp

# a = [1, 2, 3, 4, 5]
# swap_value(a[0], a[1]) # 변경이 일어나지 않음.
# print(a)

# swap_offset(0, 1) # 변경이 됨. 단, 함수 밖의 값을 불러와 쓰는 것.
# print(a)

# swap_reference(a, 2, 3) # 변경이 됨. 유동적으로 바꿔가며 원하는 함수를 불러와 쓸 수 있음.
# print(a)

## scoping rule / 변수의 범위. 지역변수(함수내에서만), 전역변수(프로그램 전체에서)로 나누어짐.
###
# def test(t):
#     print(x)
#     t = 20 # 지역변수
#     print("In Function : ", t)

# x = 10 # 전역변수
# test(x)
# # print(t) # 지역변수를 호출하려 하기에 오류 발생.

###
# def f():
#     s = "Hello" # 같은 변수가 존재해도 새로운 지역 변수로 판단하여 오류 X.
#     print(s)

# s = "Hi"
# f()
# print(s)

###
# def f():
#     global s # global 로 선언해 주어 전역변수로 만듬.
#     s = "Hello"
#     print(s)

# s = "Hi"
# f()
# print(s)

###
# def calculate(x, y):
#     total = x + y # 새로운 값이 할당되어 함수 내 total은 지역변수가 됨
#     print ("In Function")
#     print ("a:", str(a), "b:", str(b), "a+b:", str(a+b), "total :", str(total))
#     return total

# a = 5 # a와 b는 전역변수
# b = 7
# total = 0 # 전역변수 total
# print ("In Program - 1")
# print ("a:", str(a), "b:", str(b), "a+b:", str(a+b))

# sum = calculate (a,b)
# print ("After Calculation")
# print ("Total :", str(total), " Sum:", str(sum)) # 지역변수는 전역변수에 영향 X

## 재귀함수 (recursive Function) / 자기자신을 호출하는 함수
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Input Number for Factorial Calculation: "))))

## function type hints
'''
type hints 장점
1. 사용자에게 인터페이스를 명확히 알려줄 수 있음.
2. 함수의 문서화시 parameter에 대한 정보를 명확히 알 수 있음.
3. mypy 또는 IDE, linter 등을 통해 코드의 발생 가능한 오류를 사전에 확인 가능.
4. 시스템 전체적인 안정성을 확보할 수 있음.

def insert(self, index: int, module: Module) -> None 형식 처럼 사용
'''

