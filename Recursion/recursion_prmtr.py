def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)

func(4,5)
    
 
# Call 1: func(4, 5)

# x = 4, n = 5 → n != 0 → print(4) (first 4 printed) → call func(4, 4).

# Call 2: func(4, 4)

# x = 4, n = 4 → n != 0 → print(4) (second 4) → call func(4, 3).

# Call 3: func(4, 3)

# x = 4, n = 3 → print(4) (third 4) → call func(4, 2).

# Call 4: func(4, 2)

# x = 4, n = 2 → print(4) (fourth 4) → call func(4, 1).

# Call 5: func(4, 1)

# x = 4, n = 1 → print(4) (fifth 4) → call func(4, 0).

# Call 6: func(4, 0)

# x = 4, n = 0 → base case reached → return immediately (no print).

# Stack unwind: Call 6 returns to Call 5 → Call 5 has nothing left → returns → then Call 4 returns → … → finally all frames pop and program continues.