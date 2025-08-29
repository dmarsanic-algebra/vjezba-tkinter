import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class EvidencijaTroskovaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evidencija troškova")
        self.root.geometry("600x500")

        self.db_ime = "troskovi.db"
        self.kreiraj_bazu()
        
        self.kreiraj_sučelje()
        self.prikazi_troskove()
        self.prikazi_statistiku()

    def kreiraj_bazu(self):
        """Kreira SQLite bazu podataka i tablicu za troškove ako ne postoji."""
        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS troskovi (
                id INTEGER PRIMARY KEY,
                iznos REAL NOT NULL,
                kategorija TEXT NOT NULL,
                datum TEXT NOT NULL,
                opis TEXT
            )
        """)
        conn.commit()
        conn.close()

    def kreiraj_sučelje(self):
        """Kreira sve widgete za korisničko sučelje."""
        # Unos podataka
        unos_okvir = ttk.LabelFrame(self.root, text="Unos troška")
        unos_okvir.pack(padx=10, pady=10, fill="x")

        self.label_iznos = ttk.Label(unos_okvir, text="Iznos:")
        self.label_iznos.grid(row=0, column=0, padx=5, pady=5)
        self.entry_iznos = ttk.Entry(unos_okvir, width=20)
        self.entry_iznos.grid(row=0, column=1, padx=5, pady=5)

        self.label_kategorija = ttk.Label(unos_okvir, text="Kategorija:")
        self.label_kategorija.grid(row=0, column=2, padx=5, pady=5)
        self.combo_kategorija = ttk.Combobox(unos_okvir, values=["Hrana", "Prijevoz", "Stanovanje", "Zabava", "Ostalo"])
        self.combo_kategorija.grid(row=0, column=3, padx=5, pady=5)

        self.label_opis = ttk.Label(unos_okvir, text="Opis:")
        self.label_opis.grid(row=1, column=0, padx=5, pady=5)
        self.entry_opis = ttk.Entry(unos_okvir, width=40)
        self.entry_opis.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        self.gumb_dodaj = ttk.Button(unos_okvir, text="Dodaj trošak", command=self.dodaj_trosak)
        self.gumb_dodaj.grid(row=1, column=3, padx=5, pady=5)

        # Tablica troškova
        tablica_okvir = ttk.LabelFrame(self.root, text="Popis troškova")
        tablica_okvir.pack(padx=10, pady=10, fill="both", expand=True)

        stupci = ("id", "iznos", "kategorija", "datum", "opis")
        self.tree_troskovi = ttk.Treeview(tablica_okvir, columns=stupci, show="headings")
        self.tree_troskovi.pack(fill="both", expand=True)
        
        self.tree_troskovi.heading("id", text="ID")
        self.tree_troskovi.heading("iznos", text="Iznos (€)")
        self.tree_troskovi.heading("kategorija", text="Kategorija")
        self.tree_troskovi.heading("datum", text="Datum")
        self.tree_troskovi.heading("opis", text="Opis")

        self.tree_troskovi.column("id", width=30, anchor="center")
        self.tree_troskovi.column("iznos", width=80, anchor="center")
        self.tree_troskovi.column("kategorija", width=100, anchor="center")
        self.tree_troskovi.column("datum", width=100, anchor="center")
        self.tree_troskovi.column("opis", width=180, anchor="w")

        # Gumb za brisanje
        gumb_obrisi_okvir = tk.Frame(self.root)
        gumb_obrisi_okvir.pack(pady=5)
        self.gumb_obrisi = ttk.Button(gumb_obrisi_okvir, text="Obriši odabrano", command=self.obrisi_trosak)
        self.gumb_obrisi.pack()

        # Statistika
        statistika_okvir = ttk.LabelFrame(self.root, text="Statistika")
        statistika_okvir.pack(padx=10, pady=10, fill="x")
        
        self.label_ukupno = ttk.Label(statistika_okvir, text="Ukupni troškovi: 0.00 €", font=("Arial", 12))
        self.label_ukupno.pack(side="left", padx=10, pady=5)
        
        self.label_najveci = ttk.Label(statistika_okvir, text="Najveći trošak: 0.00 €", font=("Arial", 12))
        self.label_najveci.pack(side="right", padx=10, pady=5)

    def dodaj_trosak(self):
        """Dodaje novi trošak u bazu podataka."""
        try:
            iznos = float(self.entry_iznos.get().replace(',', '.'))
            kategorija = self.combo_kategorija.get()
            opis = self.entry_opis.get().strip()
            datum = datetime.now().strftime("%Y-%m-%d %H:%M")

            if iznos <= 0 or not kategorija:
                messagebox.showwarning("Upozorenje", "Iznos mora biti pozitivan broj, a kategorija odabrana.")
                return

            conn = sqlite3.connect(self.db_ime)
            c = conn.cursor()
            c.execute("INSERT INTO troskovi (iznos, kategorija, datum, opis) VALUES (?, ?, ?, ?)",
                      (iznos, kategorija, datum, opis))
            conn.commit()
            conn.close()

            self.ocisti_unos()
            self.prikazi_troskove()
            self.prikazi_statistiku()
            messagebox.showinfo("Uspjeh", "Trošak uspješno dodan!")
            
        except ValueError:
            messagebox.showerror("Greška", "Unesite valjani broj za iznos.")

    def obrisi_trosak(self):
        """Briše odabrani trošak iz baze podataka."""
        odabrani = self.tree_troskovi.selection()
        if not odabrani:
            messagebox.showwarning("Upozorenje", "Odaberite trošak za brisanje.")
            return

        id_troska = self.tree_troskovi.item(odabrani)["values"][0]
        
        if messagebox.askyesno("Potvrda brisanja", "Jeste li sigurni da želite obrisati ovaj trošak?"):
            conn = sqlite3.connect(self.db_ime)
            c = conn.cursor()
            c.execute("DELETE FROM troskovi WHERE id=?", (id_troska,))
            conn.commit()
            conn.close()
            self.prikazi_troskove()
            self.prikazi_statistiku()
            messagebox.showinfo("Uspjeh", "Trošak uspješno obrisan!")

    def prikazi_troskove(self):
        """Učitava sve troškove iz baze i prikazuje ih u Treeview-u."""
        for redak in self.tree_troskovi.get_children():
            self.tree_troskovi.delete(redak)
        
        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        c.execute("SELECT * FROM troskovi ORDER BY datum DESC")
        troskovi = c.fetchall()
        for trosak in troskovi:
            self.tree_troskovi.insert("", tk.END, values=trosak)
        conn.close()
        
    def prikazi_statistiku(self):
        """Izračunava i prikazuje statističke podatke o troškovima."""
        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        
        # Ukupni troškovi
        c.execute("SELECT SUM(iznos) FROM troskovi")
        ukupno = c.fetchone()[0] or 0.0
        self.label_ukupno.config(text=f"Ukupni troškovi: {ukupno:.2f} €")
        
        # Najveći trošak
        c.execute("SELECT MAX(iznos) FROM troskovi")
        najveci = c.fetchone()[0] or 0.0
        self.label_najveci.config(text=f"Najveći trošak: {najveci:.2f} €")
        
        conn.close()

    def ocisti_unos(self):
        """Briše sadržaj iz polja za unos."""
        self.entry_iznos.delete(0, tk.END)
        self.combo_kategorija.set("")
        self.entry_opis.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EvidencijaTroskovaApp(root)
    root.mainloop()
  
