import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import urllib.parse

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Čitač novinskih članaka")
        self.root.geometry("800x600")

        # Okvir za unos URL-a
        unos_okvir = ttk.LabelFrame(self.root, text="Unesite URL novinskog portala")
        unos_okvir.pack(padx=10, pady=10, fill="x")

        self.label_url = ttk.Label(unos_okvir, text="URL:")
        self.label_url.pack(side="left", padx=5)

        self.entry_url = ttk.Entry(unos_okvir, width=60)
        self.entry_url.pack(side="left", padx=5, expand=True, fill="x")
        self.entry_url.insert(0, "https://www.24sata.hr/") # Primjer URL-a

        self.gumb_dohvati = ttk.Button(unos_okvir, text="Dohvati članke", command=self.dohvati_clanke)
        self.gumb_dohvati.pack(side="left", padx=5)

        # Okvir za prikaz članaka
        prikaz_okvir = ttk.LabelFrame(self.root, text="Najnoviji članci")
        prikaz_okvir.pack(padx=10, pady=10, fill="both", expand=True)

        self.text_prikaz = tk.Text(prikaz_okvir, wrap="word")
        self.text_prikaz.pack(side="left", fill="both", expand=True)
        
        # Scrollbar za tekst
        scrollbar = ttk.Scrollbar(prikaz_okvir, command=self.text_prikaz.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_prikaz.config(yscrollcommand=scrollbar.set)

    def dohvati_clanke(self):
        """Dohvaća i prikazuje naslove članaka s navedenog URL-a."""
        url = self.entry_url.get().strip()
        if not url:
            messagebox.showwarning("Upozorenje", "Molimo unesite valjan URL.")
            return

        # Provjera i formatiranje URL-a
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        try:
            # Slanje HTTP zahtjeva i parsiranje HTML-a
            response = requests.get(url, timeout=10)
            response.raise_for_status() # Izaziva iznimku za loše statuse (4xx ili 5xx)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            self.text_prikaz.delete("1.0", tk.END)
            self.text_prikaz.insert(tk.END, f"Dohvaćanje članaka s: {url}\n\n")

            # Ovisno o strukturi portala, moramo pronaći odgovarajuće elemente.
            # Ovdje je primjer za 24sata.hr, ali za druge portale potrebno je prilagoditi.
            naslovi_tagovi = soup.find_all('h3', class_='card__title')
            
            if not naslovi_tagovi:
                self.text_prikaz.insert(tk.END, "Nije pronađen nijedan naslov. Možda je potrebno prilagoditi pravila za scraping.")
                return

            self.text_prikaz.insert(tk.END, "--- Najnoviji članci ---\n\n")
            
            for i, naslov in enumerate(naslovi_tagovi[:20]): # Prikaz prvih 20 članaka
                naslov_tekst = naslov.get_text(strip=True)
                link = naslov.find_parent('a')['href']
                
                # Prilagodba relativnih linkova na apsolutne
                apsolutni_link = urllib.parse.urljoin(url, link)

                self.text_prikaz.insert(tk.END, f"{i+1}. {naslov_tekst}\n", "naslov_tag")
                self.text_prikaz.tag_config("naslov_tag", font=("Arial", 12, "bold"))
                
                self.text_prikaz.insert(tk.END, f"   Link: {apsolutni_link}\n\n", "link_tag")
                self.text_prikaz.tag_config("link_tag", foreground="blue", underline=True)
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Greška u povezivanju", f"Nije moguće dohvatiti stranicu: {e}")
            self.text_prikaz.delete("1.0", tk.END)
            self.text_prikaz.insert(tk.END, f"Greška: Nije moguće dohvatiti stranicu {url}\n\nProvjerite URL i internetsku vezu.")
        except Exception as e:
            messagebox.showerror("Greška", f"Dogodila se neočekivana greška: {e}")
            self.text_prikaz.delete("1.0", tk.END)

if __name__ == "__main__":
    # Napomena: Web-scraping može biti osjetljiv na promjene u strukturi web stranica.
    # Ako kod ne radi za određeni portal, potrebno je istražiti HTML strukturu
    # tog portala (npr. pomoću "Inspect Element" u pregledniku) i prilagoditi
    # pravila za pronalazak elemenata (npr. 'h3', 'class' itd.).

    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
  
