brus = input("Har du lyst på en brus?")
if brus == "ja":
    print("Her har du en brus")

elif brus == "nei":
    print("Den er grei")

else:
    print("Det forstod jeg ikke helt")

"""Jeg lagde et ganske enkelt program her. Kjører en if-test, men etter oppgaven,
går det kun an å skrive ja eller nei. Alt mulig annet går under else.
For å optimalisere dette kunne man lagt inn flere mulige svar.
Jeg testet ut programmet på en venn og han svarte på inputen med "jaaa".
Dette blit jo tatt imot som alt mulig annet enn ja og nei, og datamaskinen forstår det ikke."""
