from UG5_71210753 import Karyawan

if __name__ == "__main__":
    orang1 = Karyawan._nama("Haniif", 90)
    orang1.printInfo()
    orang2 = Karyawan._nama("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()
    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)
