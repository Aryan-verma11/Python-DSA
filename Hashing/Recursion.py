#recursion matlab hota hai ki function ke andar function ko call krna

def greet():
    print("Aryan")
    greet()  #yaha par jab hum func ko call krengy tab ye infinite loop ban jayega 

greet() #ek baar func ko call krny ke baad ye run hony lgega infinitye time ky liye 