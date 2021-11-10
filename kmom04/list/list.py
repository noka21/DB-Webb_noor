"""
here
"""
shopping = ["köttfärs", "krossade tomater", "grädde", "gul lök", 'röd lök']
print(shopping)
print(len(shopping))
print(shopping[4])
tempItem = shopping[0]
shopping[0] = shopping[2]
shopping[2] = tempItem
print(shopping)
print(shopping[-1])
print(shopping[-3])
print(shopping[-5])
shopping.insert(2, "köttfärs")
shopping.append("gul lök")
shopping.remove("röd lök")
