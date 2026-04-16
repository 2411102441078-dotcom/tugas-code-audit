def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)


def tentukan_grade(rata_rata):
    if rata_rata >= 85:
        return "A"
    elif rata_rata >= 70:
        return "B"
    elif rata_rata >= 60:
        return "C"
    else:
        return "D"


def validasi_nilai(nilai_list):
    for nilai in nilai_list:
        if nilai < 0 or nilai > 100:
            return False
    return True


def tampilkan_hasil(rata_rata, grade):
    print(f"Rata-rata: {rata_rata}")
    print(f"Grade: {grade}")


# Program utama
nilai = [80, 75, 90]

if validasi_nilai(nilai):
    rata = hitung_rata_rata(nilai)
    grade = tentukan_grade(rata)
    tampilkan_hasil(rata, grade)
else:
    print("Nilai tidak valid")  