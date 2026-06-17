found = False
sol_count=1

for A in range(1, 21): 
    for B in range(1, 21):
        for C in range(1, 21):
            if (A + B + C == 25) and (A * B - C == 64) and (A > B >= C):
                print(f"Solution {sol_count}:")
                print("A =", A)
                print("B =", B)
                print("C =", C)
                found=True
                sol_count+=1
if not found:
    print("No solution found.")