"""
here
"""
dict_={}
user_input=input("Enter 'name, sho': ")
while True:
    if user_input== "done":
        break
    name, size=user_input.split(", ")
    dict_[name]=int(size)

    if user_input.isalpha:
        dict_[0][0]=user_input
    if user_input.isdigit:
        dict_[0][1]=user_input

print(sorted(dict_))
