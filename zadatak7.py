import tkinter as tk
from tkinter import messagebox
import requests

# Postavke API-ja
API_KEY = "VAŠ_OPENWEATHERMAP_API_KLJUČ"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class VrijemeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vremenska prognoza")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Unos grada
        self.okvir_unos = tk.Frame(self.root, bg="#f0f0f0")
        self.okvir_unos.pack(pady=10)

        self.label_grad = tk.Label(self.okvir_unos, text="Unesite grad:", bg="#f0f0f0", font=("Arial", 12))
        self.label_grad.pack(side="left", padx=5)

        self.entry_grad = tk.Entry(self.okvir_unos, width=25, font=("Arial", 12))
        self.entry_grad.pack(side="left", padx=5)

        self.gumb_dohvati = tk.Button(self.okvir_unos, text="Dohvati vrijeme", command=self.dohvati_vrijeme, font=("Arial", 10), bg="#4CAF50", fg="white")
        self.gumb_dohvati.pack(side="left", padx=5)
        
        # Prikaz podataka
        self.okvir_prikaz = tk.Frame(self.root, bg="#f0f0f0")
        self.okvir_prikaz.pack(pady=20)
        
        self.label_naziv_grada = tk.Label(self.okvir_prikaz, text="", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.label_naziv_grada.pack(pady=5)
        
        self.label_temperatura = tk.Label(self.okvir_prikaz, text="", font=("Arial", 16), bg="#f0f0f0")
        self.label_temperatura.pack(pady=5)
        
        self.label_opis = tk.Label(self.okvir_prikaz, text="", font=("Arial", 14), bg="#f0f0f0")
        self.label_opis.pack(pady=5)
        
        self.label_vlaga = tk.Label(self.okvir_prikaz, text="", font=("Arial", 12), bg="#f0f0f0")
        self.label_vlaga.pack(pady=5)

    def dohvati_vrijeme(self):
        """Šalje zahtjev OpenWeatherMap API-ju i prikazuje podatke."""
        grad = self.entry_grad.get().strip()
        if not grad:
            messagebox.showwarning("Upozorenje", "Molimo unesite naziv grada.")
            return

        # Provjera da li je API ključ postavljen
        if API_KEY == "VAŠ_OPENWEATHERMAP_API_KLJUČ":
            messagebox.showerror("Greška", "Molimo zamijenite 'VAŠ_OPENWEATHERMAP_API_KLJUČ' sa svojim ključem.")
            return

        url = f"{BASE_URL}?q={grad}&appid={API_KEY}&units=metric&lang=hr"
        
        try:
            response = requests.get(url)
            podaci = response.json()

            if podaci.get("cod") == 200:
                # Dohvaćanje relevantnih podataka
                temp = podaci["main"]["temp"]
                vlaznost = podaci["main"]["humidity"]
                opis_vremena = podaci["weather"][0]["description"]
                
                # Ažuriranje labela
                self.label_naziv_grada.config(text=f"{podaci['name']}, {podaci['sys']['country']}")
                self.label_temperatura.config(text=f"{temp}°C")
                self.label_opis.config(text=opis_vremena.capitalize())
                self.label_vlaga.config(text=f"Vlažnost: {vlaznost}%")

            else:
                # Ako API vrati grešku
                messagebox.showerror("Greška", f"Grad nije pronađen ili došlo je do greške: {podaci['message']}")
                self.ocisti_labele()

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Greška", f"Greška prilikom povezivanja: {e}")
            self.ocisti_labele()
        except Exception as e:
            messagebox.showerror("Greška", f"Dogodila se nepoznata greška: {e}")
            self.ocisti_labele()

    def ocisti_labele(self):
        """Briše sadržaj s labela za prikaz vremena."""
        self.label_naziv_grada.config(text="")
        self.label_temperatura.config(text="")
        self.label_opis.config(text="")
        self.label_vlaga.config(text="")

if __name__ == "__main__":
    # Važno: Prije pokretanja, nabavite besplatan API ključ s OpenWeatherMap stranice,
    # i zamijenite placeholder "VAŠ_OPENWEATHERMAP_API_KLJUČ" svojim ključem.
    # Stranica: https://openweathermap.org/api
    
    root = tk.Tk()
    app = VrijemeApp(root)
    root.mainloop()
  
