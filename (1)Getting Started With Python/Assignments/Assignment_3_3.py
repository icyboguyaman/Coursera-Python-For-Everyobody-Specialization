score = input("Enter Score:")
scorefloat = float(score)
if scorefloat > 1 or scorefloat < 0 :
    print("Out of range, pidor")
elif scorefloat >= 0.9 :
    print("A")
elif scorefloat >= 0.8 :
    print("B")
elif scorefloat >= 0.7 :
    print("C")
elif scorefloat >= 0.6 :
    print("D")
elif scorefloat < 0.6 :
    print("F")
