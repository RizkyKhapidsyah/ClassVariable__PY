# Class
class mahasiswa():
    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # Public
        self.nim = input_nim  # public

        mahasiswa.jumlah_mahasiswa += 1


# Main Program
Rizky = mahasiswa("Rizky Khapidsyah", 12676345)
Dessy = mahasiswa("Dessy Puspita Sari", 293827198)
Mesm = mahasiswa("Mesm", 327468327)

print(mahasiswa.jumlah_mahasiswa)