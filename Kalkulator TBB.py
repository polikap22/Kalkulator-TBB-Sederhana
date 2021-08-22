def main():
    print('---------------------------------------------------')
    print('Kalkulator TBB Sederhana Kelompok Banteng Merah    ')
    print('      #BBDD #Golput #PPKM (Kelompok 1) :D          ')
    print('@Razas(Coder), @Irfan(Fixer), @Arga(Formulator),   ')
    print('                @Yusron(Analyzer)                  ')
    print('Masih BETA ya gaess, jadi jangan berharap banyak :D')
    print('---------------------------------------------------')
    trag = input('Mau mencari nilai benda awal, benda kedua, atau nilai X&Y0? (ketik ba, bk, atau xy): ')
    if trag == 'bk':
        trig = input('Silakan pilih opsi benda kedua (ketik kelompok-persegi(kpi), segitiga, setengah-lingkaran(stl): ')
        if trig == 'kelompok-persegi' or 'kpi':
            ppkm = input('Pilih mau persegi, jajar-genjang(jg), atau persegi-panjang(pjj): ')
            if ppkm == 'persegi':
                a = eval(input('Masukkan Alasnya: '))
                b2 = eval(input('Masukkan Tinggi Benda 1: '))
                b = eval(input('Masukkan Tinggi Benda 2: '))
                t = (a*a)
                b3 = b2 + 1/2 * (b)
                a2 = 1/2 * (a)
                print('X2=', a2,'Y2=', b3,'A2=', t)
                main()
            elif ppkm == 'persegi-panjang' or 'pjj':
                a = eval(input('Masukkan Alasnya: '))
                b2 = eval(input('Masukkan Tinggi Benda 1: '))
                b = eval(input('Masukkan Tinggi Benda 2: '))
                t = (a) * (b)
                b3 = b2 + 1 / 2 * (b)
                a2 = 1 / 2 * (a * b)
                print('X2=', a2, 'Y2=', b3, 'A2=', t)
                main()
            elif trig == 'jajar-genjang' or 'jg':
                a = eval(input('Masukkan Alasnya: '))
                b2 = eval(input('Masukkan Tinggi Benda 1: '))
                b = eval(input('Masukkan Tinggi Benda 2: '))
                t = (a) * (b)
                b3 = b2 + 1 / 2 * (b)
                a2 = 1 / 2 * (a * b)
                print('X2=', a2, 'Y2=', b3, 'A2=', t)
                main()
            else:
                print('Serius dongg :D')
                main()

        elif trig == 'segitiga':
            a = eval(input('Masukkan Alasnya: '))
            b2 = eval(input('Masukkan Tinggi Benda 1: '))
            b = eval(input('Masukkan Tinggi Benda 2: '))
            t = ((a)*(b))/2
            b3 = b2 + 1/3 * (b)
            a2 = 1/2 * (a)
            print('X2=', a2, 'Y2=', b3, 'A2=', t)
            main()

        elif trig == 'setengah-lingkaran' or 'stl':
            z = input('Ada Jari-jarinya gak? (ya/tidak): ')
            if z == 'tidak':
                a = eval(input('Masukkan Alasnya: '))
                b1 = eval(input('Masukkan Nilai Diameter: '))
                b2 = eval(input('Masukkan Tinggi Benda 1: '))
                b7 = b1 / 2
                t = 1 / 2 * 3.14 * b7 * b7
                t2 = 1 / 2 * 22/7 * b7 * b7
                b4 = b2 + 4 * b7/(3 * 22/7)
                b5 = b2 + 4 * b7 / (3 * 3.14)
                a2 = 1/2 * a
                print('X2=', a2, 'Y2=', b4, 'A2=', t, '(Dengan nilai 22/7 pada Y2 dan 3.14 pada A2)')
                print('X2=', a2, 'Y2=', b4, 'A2=', t2, '(Dengan nilai 22/7 pada Y2 dan A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t, '(Dengan nilai 3.14 pada Y2 dan A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t2, '(Dengan nilai 3.14 pada Y2 dan 22/7 pada A2 )')
                main()
            elif z == 'ya':
                a = eval(input('Masukkan Alasnya: '))
                b = eval(input('Masukkan Nilai Jari-jari: '))
                b2 = eval(input('Masukkan Tinggi Benda 1: '))
                t = 1 / 2 * 3.14 * b * b
                t2 = 1 / 2 * 22 / 7 * b * b
                b4 = b2 + 4 * b / (3 * 22/7)
                b5 = b2 + 4 * b / (3 * 3.14)
                a2 = 1 / 2 * a
                print('X2=', a2, 'Y2=', b4, 'A2=', t, '(Dengan nilai 22/7 pada Y2 dan 3.14 pada A2)')
                print('X2=', a2, 'Y2=', b4, 'A2=', t2, '(Dengan nilai 22/7 pada Y2 dan A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t, '(Dengan nilai 3.14 pada Y2 dan A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t2, '(Dengan nilai 3.14 pada Y2 dan 22/7 pada A2 )')
                main()
            else:
                print('Serius dongg :D')
                main()
    elif trag == 'ba':
        trig = input('Silakan pilih opsi benda awal (ketik jajar-genjang(jg), persegi, atau persegi-panjang(pjj): ')
        if trig == 'jajar-genjang' or 'jg':
            a = eval(input('Masukkan Alasnya: '))
            b = eval(input('Masukkan Tingginya: '))
            t = a * b
            b3 = 1 / 2 * b
            a2 = 1 / 2 * a
            print('X1=', a2, 'Y1=', b3, 'A1=', t)
            main()

        elif trig == 'persegi':
            a = eval(input('Masukkan Sisinya: '))
            t = a * a
            b3 = 1 / 2 * a
            a2 = 1 / 2 * a
            print('X1=', a2, 'Y1=', b3, 'A1=', t)
            main()

        if trig == 'persegi-panjang' or 'pjj':
            a = eval(input('Masukkan Panjangnya: '))
            b = eval(input('Masukkan Lebarnya: '))
            t = a * b
            b3 = 1 / 2 * b
            a2 = 1 / 2 * a
            print('X1=', a2, 'Y1=', b3, 'A1=', t)
            main()
                
        else:
            print('Serius dongg :D')
            main()

    elif trag == 'xy':
        x = eval(input('Masukkan nilai X1-nya: '))
        x2 = eval(input('Masukkan nilai X2-nya: '))
        y = eval(input('Masukkan nilai Y1-nya: '))
        y2 = eval(input('Masukkan nilai Y2-nya: '))
        au = eval(input('Masukkan nilai A1-nya: '))
        au2 = eval(input('Masukkan nilai A2-nya: '))
        x0 = ((x * au) + (x2 * au2))/(au + au2)
        y0 = ((y * au) + (y2 * au2))/(au + au2)
        print('X0=', x0, 'Y0=', y0)
        main()

    else:
        print('Serius dongg :D')
        main()

main()