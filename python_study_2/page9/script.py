numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    # ketika variable number adalah 777, cetak '777 di temukan, hentikan loop' dan keluar dari loop
    if number==777:
        print('cetak 777 ditemukan, hentikan loop')
        break
    