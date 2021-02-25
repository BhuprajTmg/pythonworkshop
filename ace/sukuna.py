#N students take K apples and distribute them among each other evenly.
#the remaining part remains in the basket. how many apples will each single student get?
#how many apples will remain in the basket?
#the program reads the number N and K.
#it should print the two answer for the question above.
N = int(input("enter number of students:"))
K = int(input("enter number of apples:"))
N_S=K//N
print(f"each student will get{N_S}")
N_R=K%N
print(f"ramaining apples{N_R}")
