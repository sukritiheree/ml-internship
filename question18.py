s1= input("enter string 1:")
s2= input("enter string 2:")
l1 = list(s1)
l2 = list(s2)
l1.sort()
l2.sort()
str1 = " ".join(l1)
str2 = " ".join(l2)
if str1 == str2:
    print("anagram")
else:
    print("not anagram")