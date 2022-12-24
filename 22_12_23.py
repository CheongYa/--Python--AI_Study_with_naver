# 자가 진단(5기) 자가 진단 프로그래밍 영역
## 1번
# def solution(price, money, count):
#     a = 0
#     b = 0
#     for i in range(count):
#         a += price
#         b += a
#     answer = b - money

#     if answer > 0:
#         return answer
#     else:
#         return 0

# print(solution(3, 20, 4))

## 2번
# def solution(strings, n):
#     strings.sort()
#     return sorted(strings, key=lambda x:x[n])

# strings = ["sun", "bed", "car"] 
# print(solution(strings, 1))