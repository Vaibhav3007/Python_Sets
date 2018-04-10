my_strng = "The quick brown fox jumped over lazy dogs"
vow = set("aeiou")
count = 0
for i in range(len(my_strng)):
    if my_strng[i] in vow:
        count += 1

print(count)
