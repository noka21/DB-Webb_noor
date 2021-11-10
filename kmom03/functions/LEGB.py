
"""
LEGB regeln och scopes i Python
"""
x ="Global"
z="Global"

def func1():
    """
    global variable
    """
    print(f"x inside function {x}")
 
def func3():
    """
    here
    """
    y="local"
    print(y)

def func4():
    """
    here
    """
    z="local"
    print("z",z)
def func5():
    """
    here
    """
    global x
    x=x*2
    print(x)

func1()
print(f"x outside function {x}")
func3()
func4()
print("z",z)
func5()
