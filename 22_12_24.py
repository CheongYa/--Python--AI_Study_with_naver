# Module and Project 강의

# 모듈
## 모듈 만들기
# import fah_converter

# if __name__ == "__main__":
#     print("Enter a celcius value : ")
#     celcius = float(input())

#     fah = fah_converter.convert_c_to_f(celcius)
#     print("That's {0} degreees Fahrenheit".format(fah))

## namespace example
'''
1. Alias 설정하기 - 모듈명을 별칭으로 써서 (기본적으로 선호)
import fah_converter as fah
print(fah.convert_c_to_f(41.6))
2. 모듈에서 특정 함수 또는 클래스만 호출하기
from fah_converter import covert_c_to_f
print(covert_c_to_f(41.6))
3. 모듈에서 모든 함수 또는 클래스를 호출하기 
from fah_converter import *
print(covert_c_to_f(41.6))
'''

## Built-in Module
# '''
# - 파이썬이 기본 제공하는 라이브러리
# - 문자처리, 웹, 수학 등 다양한 모듈이 제공됨
# - 별다른 조치없이 import 문으로 활용 가능
# '''
# ### 난수
# import random
# print (random.randint (0,100)) # 0~100사이의 정수 난수를 생성
# print (random.random()) # 일반적인 난수 생성
# ### 시간
# import time
# print(time.localtime()) # 현재 시간 출력
# ### 웹
# import urllib.request
# response = urllib.request.urlopen("http://thetemlab.io")
# print(response.read())

# 패키지
## package overview
### game 폴더 생성 후 공부.


# File / Exception / Log Handling
# Exception Handling
'''
-try ~ except 문법
try:
    예외 발생 가능 코드
except <Exception Type>:
    예외 발생 시 대응하는 코드
'''
## 0으로 숫자를 나눌 때 예외처리 하기
# a = [1, 2, 3, 4, 5]
# for i in range(10):
#     try:
#         print(10 / i)
#         print(a[i])
#     except ZeroDivisionError: # 빌트인 에러
#         print("Not divided by 0")
#     except IndexError as e:
#         print(e)
'''
IndexError - List의 Index 범위를 넘어갈 때
NameError - 존재하지 않은 변수를 호출 할 때
ZeroDivisionError - 0으로 숫자를 나눌 때
ValueError - 변환할 수 없는 문자/숫자를 변환할 때
FileNotFoundError - 존재하지 않는 파일을 호출할 때
'''
## try ~ except ~ finally
# try:
#     for i in range(1, 10):
#         result = 10 // i
#         print(result)
# except ZeroDivisionError:
#     print("Not divided by 0")
# finally:
#     print("종료되었습니다.") # 예외와 상관 없이 실행.

## raise 구문
# while True:
#     value = input("변환할 정수 값을 입력해주세요")
#     for digit in value:
#         if digit not in "0123456789":
#             raise ValueError("숫자값을 입력하지 않으셨습니다") # 필요에 따라 강제로 Exception을 발생
#     print("정수값으로 변환된 숫자 -", int(value))

## assert 구문
# def get_binary_number(decimal_number):
#     assert isinstance(decimal_number, int) # 특정 조건에 만족하지 않을 경우 예외 발생
#     return bin(decimal_number)

# print(get_binary_number(10.0))

# File handling
'''
<Text 파일>
- 인간도 이해할 수 있는 형태인 문자열 형식으로 저장된 파일
- 메모장으로 열면 내용 확인 가능
- 메모장에 저장된 파일, HTML 파일, 파이썬 코드 파일 등
<Binary 파일>
- 컴퓨터만 이해할 수 있는 형태인 이진(법)형식 으로 저장된 파일
- 일반적으로 메모장으로 열면 내용이 깨져 보임
- 엑펠파일, 워드 파일 등등
'''
## File Read
### 실행 시 마다 한 줄 씩 읽어오기
# with open("i_have.txt", "r") as my_file:
#     i = 0
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print(str(i) + " === " + line.replace("\n","")) # 한줄씩 값 출력
#         i = i + 1

### 단어 통계 정보 산출
# with open("i_have.txt", "r") as my_file:
#     contents = my_file.read()
#     word_list = contents.split(" ") # 빈칸 기준으로 단어를 분리 리스트
#     line_list = contents.split("\n") # 한줄 씩 분리하여 리스트

# print("Total Number of Characters : ", len(contents))
# print("Total Number of Words : ", len(word_list))
# print("Total Number of Lines : ", len(line_list))

## File Write / mode는 "w", encoding = "utf8" / mode는 "a"는 추가모드
# f = open("count_log.txt", "w", encoding="utf8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
# f.close()

# with open("count_log.txt", "a", encoding="utf8") as f:
#     for i in range(11, 21):
#         data = "%d번째 줄입니다. \n" % i
#         f.write(data)

## OS module
# import os
# try:
#     os.mkdir("Cheong") # 폴더를 만들어냄
# except FileExistsError as e: # 이미 있으면 오류 발생
#     print("Already created")

# os.path.exists("Cheong") # 폴더가 있는지 확인, Boolen 으로 출력

# import shutil # 파일을 특정 폴더로 옮길 때

# source = "count_log.txt"
# dest = os.path.join("Cheong", "count_log.txt")
# shutil.copy(source, dest)

## pathlib
# import pathlib # 파일이 어디있는지 확인

# cwd = pathlib.Path.cwd()
# print(cwd)
# print(cwd.parent) # pareent = 부모 클래스까지만 보여줌

## Log 파일 생성하기
# import os
# if not os.path.isdir("log"):
#     os.mkdir("log")
# if not os.path.exists("log/count_log.txt"):
#     f = open("log/count_log.txt", "w", encoding="utf8")
#     f.write("기록이 시작됩니다.\n")
#     f.close()

# with open("log/count_log.txt", "a", encoding="utf8") as f:
#     import random, datetime
#     for i in range(1, 11):
#         stamp = str(datetime.datatime.now())
#         value = random.random() * 1000000
#         log_line = stamp + "\t" + str(value) + "값이 생성되었습니다." + "\n"
#         f.write(log_line)

## Pickle
'''
- 파이썬의 객체를 영속화(persistence) 하는 built-in 객체
- 데이터, object 등 실행중 정보를 저장 -> 불러와서 사용
- 저장해야하는 정보, 계산 결과(모델) 등 활용이 많음
'''
# import pickle
# f = open("list.pickle", "wb") # 적용시킴
# test = [1, 2, 3, 4, 5]
# pickle.dump(test, f)
# f.close

## del test # 지움

# f = open("list.pickle", "rb") # 불러옴
# test_pickle = pickle.load(f)
# test_pickle
# f.close()

# import pickle
# class Mutltiply(object):
#     def __init__(self, multiplier):
#         self.multiplier = multiplier

#     def multiply(self, number):
#         return number * self.multiplier

# muliply = Mutltiply(5)
# muliply.multiply(10)

# f = open("multiply_object.pickle", "wb")
# pickle.dump(muliply, f)
# f.close()

# f = open("multiply_object.pickle", "rb")
# multiply_pickle = pickle.load(f)
# multiply_pickle.multiply(5)

## Logging
'''
- 프로그램이 실행되는 동안 일어나는 정보 기록을 남기기
- 유저의 접근, 프로그램의 Exception, 특정 함수의 사용
- Console 화면에 출력, 파일에 남기기, DB에 남기기 등등
- 기록된 로그를 분석하여 의미있는 결과를 도출 할 수 있음
- 실행시점에서 남겨야 하는 기록, 개발시점에서 남겨야하는 기록
'''
# import logging

# if __name__ == "__main__":
#     logger = logging.getLogger("main")
#     logging.basicConfig(level=logging.DEBUG) # 작성하지 않을 시 warning을 기본값으로 잡기.
#     logger.setLevel(logging.INFO) # INFO 부터 출력

#     steam_handler = logging.FileHandler(
#         "my.log", mode="w", encoding="utf8")
#     logger.addHandler(steam_handler)

#     logger.debug("틀렸어!")
#     logger.info("확인해!")
#     logger.warning("조심해!")
#     logger.error("에러났어!")
#     logger.critical("망했다!")

### configparser
# import configparser
# config = configparser.ConfigParser()

# config.read("example.cfg")
# print(config.sections())

# for key in config['SectionTwo']:
#     value = config["SectionTwo"][key]
#     print("{0} : {1}".format(key, value))

### argparser
# import argparse

# parser = argparse.ArgumentParser(
#     description="Sum two integers."
# )

# parser.add_argument(
#     "-a", "--a_value",
#     dest="a", help="A integers", type=int,
#     required=True
# )
# parser.add_argument(
#     '-b', "--b_value",
#     dest="b", help="B integers", type=int,
#     required=True
# )

# args = parser.parse_args()
# print(args)
# print(args.a)
# print(args.b)
# print(args.a + args.b)