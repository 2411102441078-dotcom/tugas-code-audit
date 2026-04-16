# Versi clean code (perbaikan)

def hitung(n1, n2, n3):
    r = (n1 + n2 + n3) / 3
    if r >= 85:
        h = "A"
    elif r >= 70:
        h = "B"
    elif r >= 60:
        h = "C"
    else:
        h = "D"
    print("Rata:", r)
    print("Grade:", h)

hitung(80, 75, 90)