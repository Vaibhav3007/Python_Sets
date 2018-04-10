str1 = input("Enter string 1- ")
str2 = input("Enter string 2- ")

print("All letters",set(str1).union(set(str2)))

print("Common letters",set(str1).intersection(set(str2)))
