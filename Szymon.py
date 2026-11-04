tekst1 = "Witaj"
tekst2 = "Świecie"
print(tekst1 + "\n" + tekst2)


print("\n--- 2. Porównanie typów ---")

a_str = "7"
a_int = 7
a_float = 7.0

wynik_str = a_str * 4
wynik_int = a_int * 4
wynik_float = a_float * 4

print("Wynik str:", wynik_str, "| Typ:", type(wynik_str))
print("Wynik int:", wynik_int, "| Typ:", type(wynik_int))
print("Wynik float:", wynik_float, "| Typ:", type(wynik_float))


print("\n--- 3. Precision, Scale i testy ---")

liczba_f = 12.345
zaokraglona = round(liczba_f, 1)
print("Liczba zaokrąglona do 1 miejsca:", zaokraglona)
print("Czy jest instancją float?:", isinstance(zaokraglona, float))
print("Czy jest liczbą całkowitą (.is_integer())?:", zaokraglona.is_integer())


print("\n--- 4. Konwersja ---")

zmienna_tekstowa = "7"
konwersja = int(zmienna_tekstowa) + 10
print("Wynik konwersji i dodawania:", konwersja)

