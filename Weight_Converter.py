weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "L":
    weightk = float(weight)/2.205
    print("Your weight in Kg: " + str(weightk))
elif unit.upper() == "K":
    weightl = float(weight)*2.205
    print("Your weight in Lb " + str(weightl))