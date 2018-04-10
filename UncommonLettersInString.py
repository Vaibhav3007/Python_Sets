strng1 = "Vaibhav"
strng2 = "Rai"
strng_set = set(strng2)
print(strng1)
print(strng2)

for i in range(len(strng1)):
    if strng1[i] not in strng_set:
        print(strng1[i])
