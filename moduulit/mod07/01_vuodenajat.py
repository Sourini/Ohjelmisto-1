vuodenaikatuple = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukausi = int(input('anna kuukauden numero: '))
vuodenaika = vuodenaikatuple[kuukausi-1]
print(f'vuodenaika on {vuodenaika}')