a = input("Enter the name of 1st Movie:")
b = input("Enter the name of 2nd Movie:")
c = input("Enter the name of 3rd Movie:")
list = [a, b, c]
print(list)

list1 = ['rar','srs','trt','rrs','sst','txt']
l = len(list1)
for i in range(l):
    if list1[i] == list1[i][::-1]:
        print(list1[i], "is a palindrome")

grades = ('c','d','a','a','b','b','a')
count = grades.count('a')
print("The count of a is:", count)

sort = sorted(grades)
print("The sorted grades are:", sort)

dict = {"name":"Ayushman Kar","Age":20,"Course":"B.Tech"}
print(dict)