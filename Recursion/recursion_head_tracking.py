def func(i,x):
    if (i>x):
        return
    print(i)
    func(i+1,x)

func(1,5)

# Step 1: Starting point

# Program yahan se start hota hai:

# func(1, 5)
# Yani i = 1 aur x = 5.
# Ab function chalu ho gaya.
# HEAD -> func(i=1, x=5)


# Step 2: func(1,5)

# Condition check hoti hai if (i > x) → 1 > 5 ❌ False

# Iska matlab return nahi hoga, function continue karega.

# Ab print(i) chalega → print karega 1

# Output: 1

# Ab next line pe func(i+1, x) chalega → matlab func(2, 5)

# Is call ke liye ek naya frame stack pe chadh jaata hai.

# HEAD -> func(i=2, x=5)
#          func(i=1, x=5)


# step 3 func(2,5)

# 2 > 5 ❌ False

# Print karega 2

# Output: 1 2

# Call karega func(3,5)

# Step 4: func(3,5)

# 3 > 5 ❌ False

# Print karega 3

# Output: 1 2 3

# Call karega func(4,5)

# step 5 func(4,5)

# 4 > 5 ❌ False

# Print karega 4

# Output: 1 2 3 4

# Call karega func(5,5)

# Step 6: func(5,5)

# 5 > 5 ❌ False (equal hai, greater nahi)

# Print karega 5

# Output: 1 2 3 4 5

# Ab call karega func(6,5)

# Step 7: func(6,5)

# Ab i = 6, x = 5

# Condition check if (6 > 5) ✅ True

# To ye return kar deta hai — matlab recursion yahan ruk jaata hai.

# Is function ka kaam khatam, stack se ye frame pop ho jaata hai (nikal jaata hai).


# Step 8: Unwinding (wapas aana)

# Ab har ek function jise call kiya gaya tha, apna kaam complete kar chuka hai.
# Koi aur line nahi bachi, to sab ek ek karke return kar dete hain, aur stack empty ho jaata hai.