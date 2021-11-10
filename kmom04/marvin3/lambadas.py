"""
here
"""
d={'b':1,'c':22,'a':10}
print(sorted( [(v,k) for k,v in d.items() ]  ))
print(sorted( [ (v,k) for k,v in d.items()    ] , reverse=True  ))
