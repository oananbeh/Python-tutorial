months=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
"Aug", "Sep", "Oct", "Nov", "Dec")
print(months[1])
print(months[-1])
print(months[-3])
print(months[0:4])
example1=(1,3,5,7,9)
example2=(True,False,True)

example3=("Jon",24,True)
print(len(months))
if "Sep" in months:
    print("Yes")
for month in months:
    print(month)

i=0
while i<len(months):
    print(months[i])
    i+=1
t1=("o","h","t","z")
t2=(10,20,30,50,80)
t3=t1+t2
print(t3)
numbers = (1, 3, 3, 8, 7, 5, 3, 6, 8, 3)
print(numbers.count(8))
names=("Alin","Jon","Alin","Omar","Jon","Alin")
print(names.count("Jon"))