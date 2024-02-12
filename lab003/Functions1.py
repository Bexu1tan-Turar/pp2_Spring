# 1)
# def conversion(grams):
#   ounces = 28.3495231 * grams
#   print(ounces)
# conversion(float(input()))

# 2)
# def conversion1(F):
#   C = (5 / 9) * (F - 32)
#   print(C)
# conversion1(float(input()))

# 3)
# def solve(numheads,numlegs):
#   rabbits = numlegs // 4
#   chicken = numheads - rabbits
#   print ("Rabbits: " + str(rabbits) + " Chicken: " + str(chicken))
# solve(int(input()),int(input()))

# 4)
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def filter_prime(lst):
#     return [x for x in lst if is_prime(x)]
# line = input("Enter a list of numbers separated by spaces: ")
# words = line.split(' ')
# numbers = [int(i) for i in words]
# print(filter_prime(numbers))

# 5)
# def permutations(string):
#     if len(string) == 0:
#         return ['']
#     prev_list = permutations(string[1:len(string)])
#     next_list = []
#     for i in range(len(prev_list)):
#         for j in range(len(string)):
#             new_string = prev_list[i][0: j] + string[0] + prev_list[i][j: len(string) - 1]
#             if new_string not in next_list:
#                 next_list.append(new_string)
#     return next_list

# string = input("Enter a string: ")
# print("All permutations of given string are: ")
# result = permutations(string)
# for s in result:
#     print(s)

# 6)
# def reverse_words(string):
#     s = string.split()[::-1]
#     l = []
#     for i in s:
#         l.append(i)
#     return " ".join(l)

# string = input("Enter a string: ")
# print(reverse_words(string))

# 7)
# def has_33(nums):
#     for i in range(len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# nums = [1, 3, 3, 1]
# print(has_33(nums))

# 8)
# def spy_game(nums):
#     code = [0,0,7,'x']
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)
#     return len(code) == 1

# nums = [1,0,2,0,3,7]
# print(spy_game(nums))

# 9)
# def volume_of_sphere(r):
#     V=4/3*3.14*(r**3)
#     return V
# V=volume_of_sphere(float(input()))
# print(V)
# r=int(input())
# V=lambda r:r**3
# V=4/3*3.14*(r**3)
# print(V)

# 10)
# def duplicates(mylist):
#     mylist = list(dict.fromkeys(mylist))
#     print(mylist)
# line=input()
# words=line.split(' ')
# numbers=[str(i) for i in words]
# duplicates(numbers)

# 11)def palindrome(a):
#     txt= a[::-1]
#     if txt==txt[::-1]:
#         print('Yes')
#     else:
#         print('No')
# palindrome(str(input()))

# 12)
# def list(n):
#     for i in n:
#         print('* '*i)
# line = input()
# words = line.split(' ')
# numbers = [int(i) for i in words]
# list(numbers)

# 13)
# import random
# name = input("Hello! What is your name? ")
# number = random.randint(1, 20)
# attempts = 0
# print(f'Well, {name}, I am thinking of a number between 1 and 20.')
# while True:
#     guess = int(input("Take a guess\n"))
#     attempts += 1
#     if guess == number:
#         print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#         break
#     elif guess < number:
#         print('Your guess is too low')
#     else:
#         print('Your guess is too high')