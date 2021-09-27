userName=["Jon","Alin","Smith"]
list1=[1,3,4,6,7]
list2=[True,False]
list3=["obieda",33,True]
list4=[]

fruit=["apple","banana","orange"]
print (fruit[1]) #will print banana

print(fruit[-1])
#print(fruit[5])
fruit2=["apple","banana","orange","kiwi","limon"]
print(fruit2[0:2])
print(fruit2[:4])
print(fruit2[1:])
print(fruit2[-4:-1])

listName=[]
listName.append("obie")
listName.append("mark")
listName.append("jon")
listName.insert(0,"alin")
listName.insert(2,"smith")
print(listName)

fruit2=["apple","banana","orange","kiwi","limon","banana"]
fruit2.remove("banana")
fruit2.remove("banana")
print(fruit2)

fruit2.pop(1)
print(fruit2)
#['apple', 'kiwi', 'limon']
fruit2.pop()
print(fruit2)
#['apple', 'kiwi']
del fruit2[1]
print(fruit2)

fruit1 = ["apple", "banana", "cherry"]
fruit2 = ["mango", "pineapple", "papaya"]
fruit1.extend(fruit2)

print(fruit1)

fruit1.clear()
print(fruit1)

fruit = ["apple", "banana", "cherry"]
if "appl" in fruit:
    print("Yes")
else:
    print("No")

listAge=[15,19,25,28,38]
print(len(listAge))
fruit2=["apple","banana","orange","kiwi","limon","banana"]
for item in fruit2:
    print(item)

print("While Loooooop")
count=0
while count<len(fruit2):
    print(fruit2[count])
    count=count+1

fruit = ["orange", "mango", "kiwi", "pineapple"]
fruit.sort()
print (fruit)

listNumber=[25,80,99,60,3]
listNumber.sort()
print (listNumber)

fruit = ["orange", "mango", "kiwi", "pineapple"]
fruit.sort(reverse=True)
print (fruit)

listNumber=[25,80,99,60,3]
listNumber.sort(reverse=True)
print (listNumber)
