class Karyawan:

    _nama = ""
    _umur = ""
    _jenisKelamin = ""
    _upahPerHari = 0

    def _init_(self,nama,umur,jenisKelamin,upahPerHari):
        self._nama = nama
        self._umur = umur
        self._jenisKelamin = jenisKelamin
        self._upahPerHari = upahPerHari

    def getInfo(self):
        print("nama :", self._nama)
        print("umur :", self._umur)
        print("jenis kelamin :", self._jenisKelamin)
        print("upah per hari :", self._upahPerHari)

    def upah(self,tiapHari):
            if self._upahPerhari  == None:  
                print ("EROR! belum diinputkan")
            else :   
                print("diupah :",self.get_upahPerHari())
                print("nilai :",self.get_upahPerHari()* tiapHari)
