employee = {
  "name": "Jon",
  "department": "sales",
  "empID": 1658,
  "empID": 1658
  
}

print(employee)
employee = {
  "name": "Jon",
  "department": "sales",
  "empID": 1658
  
}

#print(len(employee))
employee={
    "name": "Jon",
    "age":28,
    "Active":True,
    "groups":['a','b','c']
}
print(employee)

employee = {
  "name": "Jon",
  "department": "sales",
  "empID": 1658
}
print(employee["department"])
print(employee.get("name"))
print(employee.values())
print(employee.items())
if "fall" in employee:
    print("yes")
employee = {
  "name": "Jon",
  "department": "sales",
  "empID": 1658
}

employee["name"]="Jon Smith"
print(employee)

employee = {
  "name": "Jon",
  "department": "sales",
  "empID": 1658
}
employee.update({ "department": "IT",})
print(employee)
employee["status"]="Active"

print(employee)
employee.pop("empID")
employee["status"]="Active"
print(employee)
employee.popitem()
print(employee)
del employee["name"]
print(employee)
employee.clear()

print(employee)
employee = {
  "name": "Jon",
  "department": "sales",
  "empID": 1658,
  "location": "USA"
}
for emp in employee:
    print(emp)
for emp in employee:
    print(employee[emp])
for emp in employee.values():
    print (emp)
for emp in employee.keys():
    print (emp)
for x in employee.items():
    print(x)
newemployee=employee.copy()

print(newemployee)
employees = {
  "employee1" : {
        "name" : "Jon",
		"department": "sales",
		"empID": 1648,
		"location": "USA"
  },
  "employee2" : {
        "name" : "Alin",
		"department": "Operation",
		"empID": 1653,
		"location": "USA"
  },
  "employee3" : {
        "name" : "Smith",
		"department": "IT",
		"empID": 1652,
		"location": "USA"
  }
}

print(employees["employee2"])