# 1)
# import re
# a = input()
# regx = "^a(b)*$"
# if re.search(regx, a):
#     print('True')
# else:
#     print("False")

# 2)
# import re
# a = input()
# b = re.findall(r"ab{2,3}", a)
# if b:
#     print("YES")
# else:
#     print("NO")

# 3)
# import re
# a = input("Enter a string: ")
# valid = r'[a-z]+_[a-z]+'
# matches = re.findall(valid, a)
# print("Matches found:")
# for match in matches:
#     print(match)

# 4)
# import re
# a = input("Enter text: ")
# matches = re.findall(r'[A-Z][a-z]+', a)
# print(matches)

# 5)
# import re
# a = input()
# matches = re.findall("a.+b$", a)
# print(matches)

# 6)
# import re
# v = input()
# q = re.sub( "[ ,.]", ":" , v )
# print(q)

# 7)
# import re
# a = input()
# def snake_to_camel(l):
#     v = re.findall("[a-z]+", a)
#     h = ""
#     for i in v:
#         h += i[0].upper() + i[1 : len(i)]
#     return h
# print(snake_to_camel(a))

# 8)
# import re
# a = input()
# b = re.findall('[A-Z][^A-Z]*', a)
# print(b)

# 9)
# import re
# def spaces(a):
#     valid = r'(?<!^)(?=[A-Z])'
#     a = re.sub(valid, ' ', a)
#     return a
# a = input()
# a = spaces(a)
# print(a)

# 10)
# import re
# def camel_to_snake(a):
#     b = re.sub('([A-Z])', r'_\1', a)
#     b = b.lower()
#     b = re.sub('_+', '_', b)
#     if b.startswith('_'):
#         b = b[1:]
#     return b
# a =  input()
# b = camel_to_snake(a)
# print(b)