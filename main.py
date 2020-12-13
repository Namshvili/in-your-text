def getHuruf(word):
    result = []

    for element in word:
        if element.isalpha():
            result.append(element)
    
    return result

def getKalimat(word, p):
    result = []

    for item in word:
        if item == p[0] or item == p[1] or item == p[2]:
            index = word.find(item)
            data = word[:index+1]
            result.append(data)
    
    return result
    
def getTandaBaca(word, tandaBaca):
    result = []

    for element in word:
        if element == tandaBaca:
            result.append(element)
    
    return result
i=0
lagi = 'y'
while lagi == 'y' or 'Y':
    print("====================================================================================================================")
    print("                                        PROGRAM MENGHITUNG ELEMEN PADA TEKS")
    print("====================================================================================================================")
    print("")

    word = input("Masukkan Teks: ")

    # Cari huruf
    jumlahHuruf = getHuruf(word)

    # Cari Kata
    jumlahKata = word.split(" ")

    # Cari Kalimat
    p = ['.', '!', '?']
    jumlahKalimat = getKalimat(word, p)

    # Cari Spasi
    blankSpace = " "
    jumlahSpasi = getTandaBaca(word, blankSpace)

    # Cari Jumlah Titik
    titik = "."
    jumlahTitik = getTandaBaca(word, titik)

    # Cari Tanda tanya
    tandaTanya = "?"
    jumlahTandaTanya = getTandaBaca(word, tandaTanya)

    # Cari Tanda seru
    tandaSeru = "!"
    jumlahTandaSeru = getTandaBaca(word, tandaSeru)

    # Output Hasil
    print("")
    print("====================================================================================================================")
    print("                                                      Hasil")
    print("====================================================================================================================")
    print("")
    print("Jumlah Huruf: ", len(jumlahHuruf), "Huruf")
    print("Jumlah Kata: ", len(jumlahKata), "Kata")
    print("Jumlah Spasi: ", len(jumlahSpasi), "Spasi")
    print("Jumlah Kalimat: ", len(jumlahKalimat), "Kalimat")
    print("Jumlah Titik (.) : ", len(jumlahTitik), "Titik")
    print("Jumlah Tanda Tanya (?) : ", len(jumlahTandaTanya), "Tanda Tanya")
    print("Jumlah Tanda Seru (!) : ", len(jumlahTandaSeru), "Tanda Seru")
    print("")
    print("====================================================================================================================")
    lagi = input('Ingin menghitung lagi? [Y/T]: ')
    if lagi == 't' or 'T':
        print("====================================================================================================================")
        print('                                                    Goodbye!')
        print("====================================================================================================================")
        break
i=i+1 
