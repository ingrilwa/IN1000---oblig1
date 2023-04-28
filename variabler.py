"""Først legger jeg inn en input og printer ut dette i variabelen navn"""
navn = input("Hva heter du?")
print("Hei", navn)
alder = 20
"""Her lager jeg to variabler som består av heltall.
deretter lager jeg en ny variabel som regner ut differansen mellom de to første og printer dette ut"""
tall = 4
print(alder)
print(tall)
differanse = alder - tall
print("Differanse:", differanse)
navn2 = input("Skriv inn et nytt navn")
"""Her legger jeg navnene sammen i en samlet variabel og tilpasser fremvisningen av den nye variabelen,
slik at det blir mer funksjonelt og estetisk finere."""
sammen = navn + navn2
print(sammen)
sammen = navn + " og " + navn2
print(sammen)
