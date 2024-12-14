class Film:
    def __init__(self, baslik, yonetmen, yil):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.yil = yil

    def bilgiGoster(self):
        print(f"Film: {self.baslik}, Yönetmen: {self.yonetmen}, Yıl: {self.yil}")


class FilmKlasörü:
    def __init__(self):
        self.filmler = []

    def filmEkle(self, film):
        self.filmler.append(film)

    def filmCikar(self, film):
        for i in self.filmler:
            if i == film:
                self.filmler.remove(film)

    def filmGoster(self):
        for i in self.filmler:
            i.bilgiGoster()


class Kullanici:
    def __init__(self, isim):
        self.isim = isim
        self.izlenenFilmler = []

    def film_izle(self, film):
        self.izlenenFilmler.append(film)

    def izlenen_filmler_goster(self):
        if self.izlenenFilmler:
            print(f"{self.isim} kişisinin izlediği filmler:")
            for i in self.izlenenFilmler:
                i.bilgiGoster()
        else:
            print(f"{self.isim} film izlemedi.")



film1 = Film("Avengers", "Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth", 2012)
film2 = Film("The Lord of the Rings", "Peter Jackson", 2001)

hdFilm = FilmKlasörü()
hdFilm.filmEkle(film1)
hdFilm.filmEkle(film2)
hdFilm.filmGoster()


kullanici = Kullanici("Ati")
kullanici.film_izle(film1) 
kullanici.izlenen_filmler_goster()  



