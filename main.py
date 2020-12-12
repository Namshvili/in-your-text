import functions

print("PROGRAM MENGHITUNG KATA DAN KALIMAT")
print("===================================")

word = input("Masukkan Teks: ")

# Cari huruf
jumlahHuruf = functions.getHuruf(word)

# Cari Kata
jumlahKata = word.split(" ")

# Cari Kalimat
p = ['.', '!', '?']
jumlahKalimat = functions.getKalimat(word, p)

# Cari Spasi
blankSpace = " "
jumlahSpasi = functions.getTandaBaca(word, blankSpace)

# Cari Jumlah Titik
titik = "."
jumlahTitik = functions.getTandaBaca(word, titik)

# Cari Tanda tanya
tandaTanya = "?"
jumlahTandaTanya = functions.getTandaBaca(word, tandaTanya)
    
# Cari Tanda seru
tandaSeru = "!"
jumlahTandaSeru = functions.getTandaBaca(word, tandaSeru)

# Output Hasil
print("===================================")
print("Jumlah Huruf: ", len(jumlahHuruf), "Huruf")
print("Jumlah Kata: ", len(jumlahKata), "Kata")
print("Jumlah Spasi: ", len(jumlahSpasi), "Spasi")
print("Jumlah Kalimat: ", len(jumlahKalimat), "Kalimat")
print("Jumlah Titik (.) : ", len(jumlahTitik), "Titik")
print("Jumlah Tanda Tanya (?) : ", len(jumlahTandaTanya), "Tanda Tanya")
print("Jumlah Tanda Seru (!) : ", len(jumlahTandaSeru), "Tanda Seru")