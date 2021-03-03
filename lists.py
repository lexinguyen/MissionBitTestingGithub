# mylist[start:end-1:]skip(optional)??
#for i in range(start, end-1, skip{optional}):
    #x += i -> adds x to i, i increases by one each time according to range

#x = 0
#for i in range(1,5):
    #x += 2
    #print("count:", i, " x =", x )
# will print: coubnt1 x2, c2x4, c3x6, c4x8
# 1st: x is 0, i is one(first count/time it will do smth)
#   adds 2 to x, which will be 2
#2nd: x is now 2, i is 2, 2 is added to x

#print(list[x]) = prints index in list, can add to string

#for i in range(4):
    #print("hi")
list = ["dog", 'cat', 'bird', 'mouse', 'fish', 'rat', 'finch']
print(list[:7:3])


