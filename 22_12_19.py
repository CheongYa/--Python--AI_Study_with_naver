# Python Data Structure 강의

# 스택(Stack) / Last In First Out (LIFO)
# word = input("input a word : ")
# word_list = list(word)
# for _ in range(len(word_list)):
#     print(word_list.pop())
#     print(word_list)


# 큐(Queue) / First In First Out (FIFO)
# a = [1, 2, 3, 4, 5]
# a.append(10)
# a.append(20)
# a.pop(0)
# print(a)


# 튜블(tuple) / 값의 변경이 불가능한 리스트
# t = (1, 2, 3) # 하나일 경우 t = (1, ) 식으로 작성
# print(t + t)
# print(t * 2)
# print(t)
# print(len(t))
# # t[1] = 5 # Error 발생


# 집합(set) / 값을 순서 없이 저장, 중복 불허 자료형 / 수학에서 활용하는 다양한 집합연산 가능
# s = set([1, 2, 3, 1, 2, 3]) # s = {1, 2, 3, 1, 2, 3} 도 가능
# print(s)
# s = {2, 3}
# s.add(1) # 원소 1 추가
# print(s)
# s.remove(1) # 원소 1 삭제
# print(s)
# s.update([1, 4, 5, 6, 7]) # [1, 4, 5, 6, 7] 추가
# print(s)
# s.discard(3) # 3 삭제
# print(s)
# s.clear() # 모든 원소 삭제
# print(s)

# s1 = set([1, 2, 3, 4, 5])
# s2 = set([3, 4, 5, 6, 7])
# print(s1.union(s2)) # s1 과 s2의 합집합, s1 | s2
# print(s1.intersection(s2)) # s1 과 s2의 교집합, s1 & s2
# print(s1.difference(s2)) # s1 과 s2의 차집합, s1 - s2


# 사전(dictionary) / key 값을 활용하여, 데이터 값(Value)를 관리
# country_code = {} # Dict 생성, country_code = dict() 도 가능
# country_code = {"America":1, "Korea":82, "China":86, "Japan":81}
# print(country_code)
# print(country_code.items()) # Dict 데이터 출력
# print(country_code.keys()) # Dict 키 값만 출력
# country_code["German"]=55 # Dict 추가
# print(country_code)
# print(country_code.values()) # Dict Value만 출력
# for k, v in country_code.items():
#     print("Key : ", k)
#     print("Value : ", v)
# print("Korea" in country_code.keys()) # Key값에 "Korea"가 있는지 확인
# print(80 in country_code.values()) # Value값에 80가 있는지 확인


# Command Analyzer
# import csv

# def getKey(item):   # 정렬을 위한 함수
#     return item[1]  # 신경 쓸 필요 없음

# command_data = []   # 파일 읽어오기
# with open("command_data.csv", "r", encoding="utf8") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for row in spamreader:
#         command_data.append(row)

# command_counter = {}    # dict 생성, 아이디를 key값, 입력줄 수를 value값
# for data in command_data:   # list 데이터를 dict로 변경
#     if data[1] in command_counter.keys():   # 아이디가 이미 Key값으로 변경되었을 때
#         command_counter[data[1]] += 1       # 기존 출현한 아이디
#     else:
#         command_counter[data[1]] = 1        # 처음 나온 아이디

# dictlist = []   # dict를 list로 변경
# for key, value in command_counter.items():
#     temp = [key, value]
#     dictlist.append(temp)

# sorted_dict = sorted(dictlist, key=getKey, reverse=True)    # list를 입력 줄 수로 정렬
# print(sorted_dict[:100])    # List의 상위 100개 값만 출력


# collections / List, Tupple, Dict에 대한 Python Built-in 확장 자료 구조(모듈)
# # deque / Stack과 Queue를 지원하는 모듈, List에 비해 효율적인=빠른 자료 저장 방식을 지원함
# from collections import deque

# deque_list = deque()
# for i in range(5):
#     deque_list.append(i)
# print(deque_list)
# deque_list.appendleft(10)
# print(deque_list)
# deque_list.append(100)
# print(deque_list)
# deque_list.rotate(1)
# print(deque_list)
# deque_list.extend([5,6,7])
# print(deque_list)
# deque_list.extendleft([5,6,7]) # 거꾸로 맨 앞에 들어가짐
# print(deque_list)

## OrderedDict / Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함. 그러나 python3.6부터 dict도 입력한 순서를 보장하여 출력.

## defaultdict / Dict type의 값에 기본 값을 지정, 신규값 생성시 사용하는 방법
# def default_value():
#     return 10

# from collections import defaultdict

# d = defaultdict(default_value)
# print(d["first"])

## Counter / Sequence type의 data element들의 갯수를 dict 형태로 반환
# from collections import Counter

# ball_or_strike_list = ["B","S","S","S","S","B","B"]
# c = Counter(ball_or_strike_list)
# print(c)

# c = Counter(cats=4, dogs=8)
# print(list(c.elements()))

# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d) # c - d
# print(c) # c + d, c & d, c | d 이런 식으로 출력도 가능

## namedtuple / Tuple 형태로 Data 구조체를 저장하는 방법
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p)
print(p.x + p.y)