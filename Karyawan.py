from pickle import NONE


class Karyawan:
    _nama = ""
    _umur = ""
    _jenisKelamin = NONE
    _upahPerHari = NONE

    def init(self, nama, umur, jenisKelamin, upahPerHari):
        self._nama = nama
        self._umur = umur
        self._jenisKelamin = jenisKelamin
        self._upahPerHari = upahPerHari

    def getNama(self,nama):
        self._nama = nama

    def getUmur(self,umur):
        self._umur = umur

    def getMerk(self,jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def getMerk(self,upahPerhari):
        self._upahPerHari = upahPerhari

    def printInfo(self):
        print("Nama :", self._nama)
        print("Umur :", self._umur)
        print("Jenis Kelamin :", self._jenisKelamin)
        print("Upah Perhari :", self._upahPerHari)

    def hitungGajiBulanan(self,tiapHari):
        if self._upahPerHari  == None  or self._jenisKelamin == None:
            print ("EROR! Kapasitas BBM atau Jenis Bahan Bakar belum diinputkan")
        else :
            print("upahPerHari :",self.get_upahPerHari())
            print("Gaji Bulan ini :",self.get_upahPerHari()*tiapHari)