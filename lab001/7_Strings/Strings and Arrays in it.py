#ex1 Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

#ex2 You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#ex3 Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

"""Arrays"""
#ex1
a = "Hello, World!"
print(a[1])

#ex2 
for x in "banana":
  print(x)

#ex3
  a = "Hello, World!"
print(len(a))

#ex4 
txt = "The best things in life are free!"
print("free" in txt)

#ex5
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#ex6 
txt = "The best things in life are free!"
print("expensive" not in txt)

#ex7
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
