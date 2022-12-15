# Praktikum 8

print("===================================")
print("Nama : Liskania Aprilia")
print("NIM  : 312210383")
print("===================================")

data = {}
class Data():
    def __init__(self, nama, nim, tugas, uts, uas, nilaiakhir):
        while True:

            print("\33[34m")
            print("|1| Lihat Data")
            print("|2| Tambah Data")
            print("|3| Ubah Data")
            print("|4| Hapus Data")
            print("|5| Keluar")

            x = input(">> PILIH MENU : ")

            if x == '1':
                self.tampilkan()
            elif x == '2':
                self.tambah()
            elif x == '3':
                self.ubah()
            elif x == '4':
                self.hapus()
            else:
                exit()

    def tambah(self):
        print()
        print("Tambah Data")
        self.nama = input("Nama        : ")
        self.nim = input("NIM         : ")
        self.tugas = int(input("Nilai Tugas : "))
        self.uts = int(input("Nilai UTS   : "))
        self.uas = int(input("Nilai UAS   : "))
        self.nilaiakhir = (self.tugas * 30 / 100) + (self.uts * 35 / 100) + (self.uas * 35 / 100)
        data[self.nama] = [self.nim, self.tugas, self.uts, self.uas, self.nilaiakhir]
        print("\33[32m\nDATA BERHASIL DI TAMBAHKAN!")

class mahasiswa(Data):

    def tampilkan(self):
        if data.items():
            print()
            print("Daftar Nilai")
            print()
            print("=============================================================================================")
            print("|  No  |       NAMA       |      NIM      |   TUGAS   |    UTS    |    UAS    | Nilai Akhir |")
            print("=============================================================================================")
            i = 0
            for a in data.items():
                i += 1
                print("|  {no:2d}  |   {0:12s}   |  {1:11s}  |  {2:7d}  |  {3:7d}  |  {4:7d}  |   {5:6.2f}    |"
                      .format(a[0][: 14], a[1][0], a[1][1], a[1][2], a[1][3], a[1][4], no=i))
            print("=============================================================================================")

        else:
            print()
            print("Daftar Nilai")
            print()
            print("=============================================================================================")
            print("|  No  |       NAMA       |      NIM      |   TUGAS   |    UTS    |    UAS    | Nilai Akhir |")
            print("=============================================================================================")
            print("|                                       TIDAK ADA DATA                                      |")
            print("=============================================================================================")

    def ubah(self):
        print()
        print("Ubah Data Mahasiswa")
        self.nama = input("Nama        : ")
        if self.nama in data.keys():
            self.nim = input("NIM         : ")
            self.tugas = int(input("Nilai Tugas : "))
            self.uts = int(input("Nilai UTS   : "))
            self.uas = int(input("Nilai UAS   : "))
            self.nilaiakhir = (self.tugas * 30 / 100) + (self.uts * 35 / 100) + (self.uas * 35 / 100)
            data[self.nama] = [self.nim, self.tugas, self.uts, self.uas, self.nilaiakhir]
            print("\33[33m\nDATA BERHASIL DI UBAH!")
        else:
            print("Data {0} tidak ada".format(self.nama))
            print("\33[31m\nDATA TIDAK DI TEMUKAN!")

    def hapus(self):
        print()
        print("Hapus Data Mahasiswa")
        self.nama = input("Nama       : ")
        if self.nama in data.keys():
            del data[self.nama]
            print("\33[31m\nDATA BERHASIL DI HAPUS!")
        else:
            print("Data {0} tidak ada".format(self.nama))
            print("\33[31m\nDATA TIDAK DI TEMUKAN!")

datamhs = mahasiswa("nama","nim","tugas","uts","uas","nilaiakhir")