d = {}
elements = int(input("number of elements:"))
for i in range(elements):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
print("dict=", d)
