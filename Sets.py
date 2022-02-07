mySet={"jon","Adam","Smith"}
print(mySet)

mySet={"Jon",23,True}
print(mySet)
mySet = {"apple","cherry","banana"}
print(len(mySet))

mySet = {"Jon", "Adam", "Alin"}
#print(mySet{0})
for name in mySet:
    print(name)
mySet = {"Jon", "Adam", "Alin"}
#print(mySet{0})
if "smith" in mySet:
    print("Yes")

mySet = {"Jon", "Adam", "Alin"}
mySet.add("Smmith")
print(mySet)

mySet1 = {"apple", "banana", "cherry"}
mySet2 = {"pineapple", "mango", "papaya"}

mySet1.update(mySet2)
print(mySet1)

set1 = {"apple", "banana", "cherry"}
list1 = ["pineapple", "mango", "papaya"]
set1.update(list1)
print(set1)
mySet = {"Jon", "Adam", "Alin"}
mySet.remove("Alin")
print(mySet)
mySet = {"Jon", "Adam", "Alin"}
mySet.discard("Adam")
print(mySet)
mySet = {"Jon", "Adam", "Alin"}
mySet.pop()
print(mySet)
mySet = {"Jon", "Adam", "Alin"}
mySet.clear()
print(mySet)
mySet = {"Jon", "Adam", "Alin"}
del(mySet)
print(mySet)
mySet = {"Jon", "Adam", "Alin"}
for name in mySet:
    print(name)
mySet1 = {"apple", "banana", "cherry"}
mySet2 = {"pineapple", "mango","apple", "papaya"}
newSet=mySet1.union(mySet2)

print(newSet)
mySet1 = {"apple", "banana", "cherry"}
mySet2 = {"pineapple", "mango","apple", "papaya"}

mySet1.update(mySet2)

print(mySet1)
 
mySet1 = {"apple", "banana", "cherry"}
mySet2 = {"pineapple", "mango","apple", "papaya"}
mySet1.intersection_update(mySet2)
print(mySet1)
newSet=mySet1.intersection(mySet2)
print(mySet1)
 
mySet1 = {"apple", "banana", "cherry"}
mySet2 = ["pineapple", "banana", "papaya", "cherry"]
newset=mySet1.symmetric_difference(mySet2)
print(newset)