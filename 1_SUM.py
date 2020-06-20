def Sum(num, target):
    list=[0,0]
    i=0
    j=0
    while(i<len(num)):
        j=0
        while(j<len(num)):
            if num[i]+num[j]==target:
                list[0]=i
                list[1]=j
                break
            else:
                j+=1
        i+=1
    return list
num = [2, 7, 8, 8]
target = 16
a = Sum
a(num, target)
print(a(num, target))




