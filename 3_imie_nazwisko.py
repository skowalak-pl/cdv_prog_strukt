




name=input("Podaj imie:")
surname=input("Podaj nazwisko:")
yearsOld=input("Podaj ile masz lat:")
print("Twoje imie i nazwisko: " + name  + " " + surname + " , a Twoj wiek to: " + yearsOld + " lat ")


print("\nPodaj narodowość:", end="")
nationality=input()
surname="Kowalski"
firstLetter=surname[0]
print (firstLetter)

lastLetter=surname[len(surname) -1]
print(lastLetter)

#konwersja danych

a="10"
print(type(a))
a=int(a)
print(type(a))

b=6
print(type(b)) #int
b/=2 #b=b/2
print(type(b)) #float
print(b)

print()
surname="Nowakowski"
print(surname[0]) # N
print(surname[0:2]) # No
print(surname[-2]) # k
print(surname[-2:]) # ki
print(surname[:-2]) # Nowakows
print(surname[:-2:2]) # Nwkw
print("Test")


