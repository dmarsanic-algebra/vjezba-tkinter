import tkinter as tk
from tkinter import messagebox

class CitacDatotekaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Čitač tekstualnih datoteka")
        self.root.geometry("600x400")

        # Kreiranje okvira za unos i gumb
        self.okvir_unos = tk.Frame(root)
        self.okvir_unos.pack(pady=10)

        self.labela_putanja = tk.Label(self.okvir_unos, text="Putanja datoteke:")
        self.labela_putanja.pack(side=tk.LEFT, padx=5)

        self.entry_putanja = tk.Entry(self.okvir_unos, width=50)
        self.entry_putanja.pack(side=tk.LEFT, padx=5)
        
        # Postavljanje primjera putanje za lakše testiranje
        # NAPOMENA: Promijenite 'primjer.txt' u putanju do datoteke na vašem računalu
        self.entry_putanja.insert(0, "primjer.txt")

        self.gumb_ucitaj = tk.Button(self.okvir_unos, text="Učitaj datoteku", command=self.ucitaj_datoteku)
        self.gumb_ucitaj.pack(side=tk.LEFT, padx=5)

        # Kreiranje Text widgeta za prikaz sadržaja
        self.text_sadrzaj = tk.Text(root, wrap=tk.WORD)  # wrap=tk.WORD osigurava prijelom teksta
        self.text_sadrzaj.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def ucitaj_datoteku(self):
        """Čita datoteku s navedene putanje i prikazuje njen sadržaj."""
        putanja = self.entry_putanja.get()
        if not putanja:
            messagebox.showwarning("Upozorenje", "Molimo unesite putanju do datoteke.")
            return

        try:
            with open(putanja, 'r', encoding='utf-8') as f:
                sadrzaj = f.read()
            
            # Brisanje postojećeg sadržaja i umetanje novog
            self.text_sadrzaj.delete("1.0", tk.END)
            self.text_sadrzaj.insert(tk.END, sadrzaj)
        except FileNotFoundError:
            messagebox.showerror("Greška", f"Datoteka '{putanja}' nije pronađena.")
        except Exception as e:
            messagebox.showerror("Greška", f"Dogodila se greška: {e}")

if __name__ == "__main__":
    # Prije pokretanja, kreirajte testnu datoteku 'primjer.txt'
    # s nekim tekstom u istoj mapi gdje se nalazi i Python skripta.
    # Npr. stvorite datoteku i dodajte unutra:
    # Ovo je testna linija 1.
    # Ovo je testna linija 2.
    # Čitač bi trebao prikazati ovaj sadržaj.

    root = tk.Tk()
    app = CitacDatotekaApp(root)
    root.mainloop()
  
