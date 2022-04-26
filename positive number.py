li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Positive numbers in",li,"are: ")
positive_num = [num for num in li if num >= 0]
print(positive_num)
