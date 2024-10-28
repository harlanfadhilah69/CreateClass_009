class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f'Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm'


def main():
    try:
        panjang = int(input("Masukkan panjang persegi panjang (cm): "))
        lebar = int(input("Masukkan lebar persegi panjang (cm): "))

        if panjang <= 0 or lebar <= 0:
            print("Nilai panjang dan lebar tidak boleh Negatif (-)")
            return

        pp = PersegiPanjang(panjang, lebar)
        print(pp)
        print(f'Keliling: {pp.hitung_keliling()} cm')
        print(f'Luas: {pp.hitung_luas()} cm²')

    except ValueError:
        print("Input tidak valid")

main()