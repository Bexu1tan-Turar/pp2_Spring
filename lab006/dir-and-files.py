# 1)
# import os
# path = input("Enter path: ")
# directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
# print("Directories in path:")
# print(directories)
# files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
# print("Files in path:")
# print(files)
# all = os.listdir(path)
# print("All contents in path:")
# print(all)

# 2)
# import os
# path = input("Enter path to checking: ")
# if os.path.exists(path):
#     print(f"{path} exist")
#     if os.access(path, os.R_OK):
#         print(f"{path} readable")
#     else:
#         print(f"{path} not readable")
#     if os.access(path, os.W_OK):
#         print(f"{path} writable")
#     else:
#         print(f"{path} not writable")
#     if os.access(path, os.X_OK):
#         print(f"{path} executable")
#     else:
#         print(f"{path} not executable")
# else:
#     print(f"{path} doesn't exist!")

# 3)
# import os
# path = input("Enter path: ")
# if os.path.exists(path):
#     print("Path to directory:", os.path.dirname(path))
#     print("Directory name:", os.path.basename(path))
# else:
#     print("Path does not exist!")

# 4)
# f = "test.txt"
# cnt = 0
# with open(f, "r") as file:
#     for line in file:
#         cnt += 1
# print("Number of lines in", f, ":", cnt)

# 5)
# l = input().split()
# with open("testing.txt", "w") as file:
#     for i in l:
#         file.write(i + "\n")

# 6)
# import string
# l = list(string.ascii_uppercase)
# for letter in l:
#     n = letter + ".txt"
#     with open(n, "w") as file:
#         file.write("This is file " + n)

# 7)
# path1 = input("Enter first path: ")
# path2 = input("Enter second path: ")
# with open(path1, "r") as s, open(path2, "w") as d:
#     contents = s.read()
#     d.write(contents)
# print("File copied successfully!")

# 8)
# import os
# path = input("Enter path: ")
# if os.path.exists(path):
#     if os.access(path, os.W_OK):
#         os.remove(path)
#         print("File deleted successfully")
#     else:
#         print("You don't have permission to delete the file")
# else:
#     print("File does not exist!")