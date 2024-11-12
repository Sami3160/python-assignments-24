def HelloWorld(str):
    print(str)


def function(num=10):
    print(num)

def anotherFunction(**kwrgs):
    print(kwrgs)
    pass

def againFunction(n1, n2):
    print(n1)
    pass


againFunction("sa","")


HelloWorld("print")
function()
anotherFunction(name='sami', age=20, pointer=7.5, lang=['py','java','js'])