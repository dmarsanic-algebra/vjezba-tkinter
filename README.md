
Zadatci za vježbu
Ovaj README sadrži devet praktičnih zadataka za učenje Tkintera i osnovnih Python tehnika. Svaki zadatak ima jasan opis i smjernice.

---

## Kako koristiti
1. Za svaki zadatak napravi zaseban `.py` file (npr. `zadatak1.py`).
2. Pokreni file s `python zadatak1.py` (ili `python3` ovisno o sustavu).
3. Po potrebi dodaj dodatne pakete (npr. `requests`, `beautifulsoup4`).

**Preduvjeti**
- Python 3.11+
- Tkinter (dolazi uz standardnu Python instalaciju na većini sustava)
- Po potrebi:
  - `requests` (`pip install requests`)
  - `beautifulsoup4` (`pip install beautifulsoup4`)
  - `sqlite3` (standardni modul u Pythonu)
  - OpenWeatherMap račun i API ključ (za Zadatak 7)

---

## Zadatak 1. Jednostavna aplikacija „Pozdrav svijetu”
Kreirajte osnovnu aplikaciju Tkinter s jednim gumbom. Kada korisnik klikne na gumb, aplikacija bi trebala prikazati tekst „Pozdrav, svijete!” u labelu ispod gumba.

**Smjernice**
- Upotrijebite `Label` za prikazivanje teksta.
- Upotrijebite `Button` za interakciju s korisnikom.
- Implementirajte funkciju koja mijenja tekst u oznaci (labelu) nakon klika na gumb.

---

## Zadatak 2. Brojač
Razvijte aplikaciju Tkinter koja prikazuje broj u labelu i ima dva gumba označena s „Povećaj” i „Smanji”. Svaki put kada se klikne na gumb, broj prikazan u labelu treba se povećati ili smanjiti za 1.

**Smjernice**
- Upotrijebite `IntVar` za pohranu i praćenje promjena broja.
- Ažurirajte vrijednost prikazanu u labelu nakon svakog klika na gumb.

---

## Zadatak 3. Čitač tekstualnih datoteka
Kreirajte aplikaciju Tkinter koja ima polje za unos putanje do datoteke i gumb „Učitaj datoteku”. Nakon klika na gumb, sadržaj tekstualne datoteke trebao bi se prikazati u `Text` widgetu unutar aplikacije.

**Smjernice**
- Upotrijebite `Entry` za unos putanje do datoteke.
- Upotrijebite widget `Text` za prikaz sadržaja datoteke.
- Implementirajte funkciju koja čita sadržaj datoteke i prikazuje ga widgetu u `Text`.

---

## Zadatak 4. To-Do lista
Izradite aplikaciju za upravljanje to-do listom u kojoj korisnici mogu dodavati zadatke, označavati ih kao dovršene i brisati ih. Zadaci trebaju biti pohranjeni u tekstualnoj datoteci, a aplikacija treba učitavati postojeće zadatke pri pokretanju.

**Smjernice**
- Upotrijebite `Listbox` za prikaz zadataka.
- Implementirajte funkcije za dodavanje, brisanje i spremanje zadataka.
- Koristite se tekstualnom datotekom za pohranu zadataka.

---

## Zadatak 5. Kalkulator
Razvijte jednostavnu aplikaciju kalkulatora s Tkinterom. Aplikacija treba imati gumbe za brojeve (0–9) i osnovne operacije (+, −, *, /). Korisnik treba moći unijeti izraz i vidjeti rezultat proračuna.

**Smjernice**
- Koristite se widgetom `Entry` za unos i prikaz rezultata.
- Implementirajte osnovne matematičke operacije.
- Implementirajte funkciju koja izračunava rezultat nakon unosa izraza.

---

## Zadatak 6. Upravljanje kontaktima s SQLite bazom
Razvijte aplikaciju za upravljanje kontaktima. Korisnici mogu dodavati, uređivati, brisati i pretraživati kontakte. Podatci o kontaktima (ime, prezime, broj telefona, e-pošta) trebaju biti pohranjeni u SQLite bazi podataka.

**Smjernice**
- Koristite se SQLite bazom za pohranu podataka.
- Kreirajte sučelje za prikazivanje, dodavanje i uređivanje kontakata.
- Implementirajte funkcionalnost za pretraživanje i filtriranje kontakata.

---

## Zadatak 7. Prikaz podataka o vremenu korištenjem REST API-ja
Kreirajte aplikaciju koja korisnicima omogućuje unos naziva grada, a zatim prikazuje trenutačne vremenske uvjete (temperatura, vlažnost itd.) koristeći se podatcima s REST API-ja (npr. OpenWeatherMap).

**Smjernice**
- Upotrijebite `Entry` za unos naziva grada.
- Koristite se `requests` modulom za slanje zahtjeva API-ju i dohvaćanje podataka.
- Prikaz podataka u `Label` widgetima unutar aplikacije.

---

## Zadatak 8. Evidencija troškova
Razvijte aplikaciju za praćenje troškova u kojoj korisnici mogu unositi iznose i kategorije troškova. Podatci trebaju biti pohranjeni u SQLite bazi.

**Smjernice**
- Upotrijebite SQLite za pohranu podataka o troškovima.
- Implementirajte unos novih troškova i prikaz statistike.

---

## Zadatak 9. Čitač novinskih članaka koristeći se web-scrapingom
Razvijte aplikaciju koja korisnicima omogućuje unos URL-a novinskog portala, dohvaća najnovije članke s tog portala (npr. s pomoću BeautifulSoup) i prikazuje ih u aplikaciji.

**Smjernice**
- Upotrijebite `requests` i `BeautifulSoup` za web-scraping.
- Prikaz rezultata u Tkinterovu widgetu `Text`.
- Implementirajte funkcionalnost za preuzimanje i prikaz članka.

---

### Savjeti
- Počni jednostavno, pa nadograđuj (validacije, error poruke, dizajn).
- Koristi `grid` ili `pack` dosljedno po prozoru.
- Razdvoji logiku i UI gdje je moguće.
