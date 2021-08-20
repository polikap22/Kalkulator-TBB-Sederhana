def main():
    print('Kalkulator TBB Sederhana Kelompok Banteng Merah (Kelompok 1) :D')
    trag = input('Mau mencari nilai benda awal, benda kedua, atau nilai X&Y0? (ketik ba, bk, atau xy): ')
    if trag == 'bk':
        trig = input('Silakan pilih opsi benda kedua (ketik jajar-genjang, segitiga, atau lingkaran): ')
        if trig == 'jajar-genjang':
            a = eval(input('Masukkan dulu Alasnya: '))
            b2 = eval(input('Masukkan dulu Tinggi benda 2: '))
            b = eval(input('Masukkan dulu Tinggi benda 1: '))
            t = a * b2
            b3 = b2 + 1/2 * (b)
            a2 = 1/2 * a
            print('X2=', a2,'Y2=', b3,'A2=', t)
            main()

        elif trig == 'segitiga':
            a = eval(input('Masukkan dulu Alasnya: '))
            b2 = eval(input('Masukkan dulu Tinggi benda 2: '))
            b = eval(input('Masukkan dulu Tinggi benda 1: '))
            t = (a*(b))/2
            b3 = b2 + 1/3 * (b)
            a2 = 1/2 * a
            print('X2=', a2, 'Y2=', b3, 'A2=', t)
            main()

        elif trig == 'lingkaran':
            z = input('Ada jari-jarinya gak? (ya/tidak): ')
            if z == 'tidak':
                a = eval(input('Masukkan dulu Alasnya: '))
                b1 = eval(input('Masukkan dulu nilai Diameter: '))
                b2 = eval(input('Masukkan dulu Tinggi benda 1: '))
                b7 = b1 / 2
                t = 1 / 2 * 3.14 * b7 * b7
                t2 = 1 / 2 * 22/7 * b7 * b7
                b4 = b2 + 4 * b7/(3 * 22/7)
                b5 = b2 + 4 * b7 / (3 * 3.14)
                a2 = 1/2 * a
                print('X2=', a2, 'Y2=', b4, 'A2=', t , '(Dengan nilai 3.14 pada A2 dan 22/7 pada Y2)')
                print('X2=', a2, 'Y2=', b4, 'A2=', t2, '(Dengan nilai 22/7 pada Y2 dan 3.14 pada A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t, '(Dengan nilai 3.14 pada Y2 dan A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t2, '(Dengan nilai 3.14 pada Y2 dan 22/7 pada A2 )')
                main()
            elif z == 'ya':
                a = eval(input('Masukkan dulu Alasnya: '))
                b = eval(input('Masukkan dulu nilai Jari-jari: '))
                b2 = eval(input('Masukkan dulu Tinggi benda 1: '))
                t = 1 / 2 * 3.14 * b * b
                t2 = 1 / 2 * 22 / 7 * b * b
                b4 = b2 + 4 * b / (3 * 22 / 7)
                b5 = b2 + 4 * b / (3 * 3.14)
                a2 = 1 / 2 * a
                print('X2=', a2, 'Y2=', b4, 'A2=', t, '(Dengan nilai 3.14 pada A2 dan 22/7 pada Y2)')
                print('X2=', a2, 'Y2=', b4, 'A2=', t2, '(Dengan nilai 22/7 pada Y2 dan 3.14 pada A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t, '(Dengan nilai 3.14 pada Y2 dan A2)')
                print('X2=', a2, 'Y2=', b5, 'A2=', t2, '(Dengan nilai 3.14 pada Y2 dan 22/7 pada A2 )')
                main()
            else:
                print('Serius dongg :D')
                main()

    elif trag == 'ba':
        trig = input('Silakan pilih opsi benda awal (ketik jajar-genjang atau persegi): ')
        if trig == 'jajar-genjang':
            a = eval(input('Masukkan dulu Alasnya: '))
            b = eval(input('Masukkan dulu Tingginya: '))
            t = a * b
            b3 = 1 / 2 * b
            a2 = 1 / 2 * a
            print('X1=', a2, 'Y1=', b3, 'A1=', t)
            main()

        elif trig == 'persegi':
            a = eval(input('Masukkan dulu Alasnya: '))
            t = a * a
            b3 = 1 / 2 * a
            a2 = 1 / 2 * a
            print('X1=', a2, 'Y1=', b3, 'A1=', t)
            main()
                
        else:
            print('Serius dongg :D')
            main()

    elif trag == 'xy':
        x = eval(input('Masukkan dulu nilai X1 nya: '))
        x2 = eval(input('Masukkan dulu nilai X2 nya: '))
        y = eval(input('Masukkan dulu nilai Y1 nya: '))
        y2 = eval(input('Masukkan dulu nilai Y2 nya: '))
        au = eval(input('Masukkan dulu nilai A1 nya: '))
        au2 = eval(input('Masukkan dulu nilai A2 nya: '))
        x0 = ((x * au) + (x2 * au2))/(au + au2)
        y0 = ((y * au) + (y2 * au2))/(au + au2)
        print('X0=', x0, 'Y0=', y0)
        main()

    else:
        print('Serius dongg :D')
        main()

main()