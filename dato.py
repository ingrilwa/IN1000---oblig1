print("Du skal nå oppgi to datoer")
dag1 = input("Skriv inn en dato i form av et heltall")
maned1 = input("Skriv inn en måned i form av et heltall")

dag2 = input("Skriv inn en ny dato")
maned2 = input("Skriv inn en ny måned")
"""Jeg visste ikke helt hvordan jeg ville løse dette på best mulig måte,
men valgte å ta inn dag og måned hver for seg. For et helt optimalt program,
ville jeg lagt inn grenseverdier slik at kun gyldige datoer hadde gått an å skrive inn."""

if maned1 < maned2:
    print("Riktig rekkefølge!")

elif maned1 > maned2:
    print("Feil rekkefølge!")

else:
    if dag1 < dag2:
        print("Riktig rekkefølge")
    elif dag1 == dag2:
        print("Samme dato")
    else:
        print("Feil rekkefølge")

"""På slutten kjører jeg en if-setning som printer ut om man skrvier inn datoene i riktig rekkefølge
eller ikke."""
