def main():
    import math
    print('Kalkulator Torsi (Bonus) Kelompok Banteng Merah (Kelompok 1) :D')
    r = eval(input('Masukkan Nilai Vektor Radius (r): '))
    l = eval(input('Masukkan Nilai Vektor Gaya (F): '))
    s = eval(input('Masukkan Nilai Sin: '))
    t = math.sin(math.radians(s))
    z = r * l * t
    print('Hasil:', z)

main()