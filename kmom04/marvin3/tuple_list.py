"""
yes
"""
d={'b':1,'c':22,'a':10}
print(d.items())
temp_list=[]
for k, v in d.items():
    temp_list.append((v,k))
print(temp_list)
temp_list=sorted(temp_list, reverse=True)
print(temp_list)
