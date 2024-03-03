# 1)
# from functools import reduce

# def multiply_list(num):
#     return reduce(lambda x, y: x*y, num)

# lst = input("Enter a list of integers separated by space: ")
# num = list(map(int, lst.split()))
# result = multiply_list(num)
# print(result)

# 2)
# def count_upper_lower(string):
#     upcnt = 0
#     lowcnt = 0
#     for char in string:
#         if char.isupper():
#             upcnt += 1
#         elif char.islower():
#             lowcnt += 1
#     return upcnt, lowcnt

# string = str(input())
# upper, lower = count_upper_lower(string)
# print(f"Number of uppercase letters: {upper}")
# print(f"Number of lowercase letters: {lower}")

# 3)
# def is_palindrome(string):
#     return str1 == str1[::-1]

# str1 = str(input())
# if is_palindrome(str1):
#     print(f"{str1} is a palindrome.")
# else:
#     print(f"{str1} is not a palindrome.")

# 4)
# import math
# import time

# def sqrt_after_ms(num, ms):
#     time.sleep(ms/1000)
#     return math.sqrt(num)
  
# num = int(input())
# ms = int(input())
# result = sqrt_after_ms(num, ms)
# print(f"Square root of {num} after {ms} milliseconds is {result}")

# 5)
# def all_true(t):
#     return all(t)

# t1 = (True, True, True)
# t2 = (True, False, True)
# print(all_true(t1))
# print(all_true(t2))
