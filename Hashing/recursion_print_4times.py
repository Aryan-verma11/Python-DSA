
def greet(count=0):
    if count==4:
        return #yah return function stack me se function ko bahar nikal dega
    print("aryan")
    greet(count+1)
greet()

#recursion me function sirf 987 baar call hoga oskyn baad python khud samajh jayega ki ye infinite function hai aur oosky baad run nhi krega 
# aur baaki languages me ye infinite loop tak chalta jayega 
#recursion me function call hoty rhty hai aur memory stack me bharty rhty hai 