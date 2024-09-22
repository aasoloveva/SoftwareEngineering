x = float(input())
if x < 0 or x > 10:
    print("Число должно быть от 0 до 10!")
elif 0 <= x <= 3:
    print("x ∈ [0; 3]")
elif 3 < x < 6:
    print("x ∈ (3; 6)")
elif 6 <= x <= 10:
    print("x ∈ [6; 10]")