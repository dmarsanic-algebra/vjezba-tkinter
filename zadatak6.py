import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class KontaktApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Upravljanje kontaktima")
        self.root.geometry("700x500")

        self.db_ime = "kontakti.db"
        self.kreiraj_bazu()

        self.kreiraj_sucelje()
        self.prikazi_kontakte()

    def kreiraj_bazu(self):
        """Kreira SQLite bazu podataka i tablicu za kontakte ako ne postoje."""
        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS kontakti (
                id INTEGER PRIMARY KEY,
                ime TEXT NOT NULL,
                prezime TEXT NOT NULL,
                telefon TEXT,
                email TEXT
            )
        """)
        conn.commit()
        conn.close()

    def kreiraj_sucelje(self):
        """Kreira sve widgete za korisničko sučelje."""
        # Unos podataka
        unos_okvir = ttk.LabelFrame(self.root, text="Unos kontakta")
        unos_okvir.pack(padx=10, pady=10, fill="x")

        self.label_ime = ttk.Label(unos_okvir, text="Ime:")
        self.label_ime.grid(row=0, column=0, padx=5, pady=5)
        self.entry_ime = ttk.Entry(unos_okvir, width=30)
        self.entry_ime.grid(row=0, column=1, padx=5, pady=5)

        self.label_prezime = ttk.Label(unos_okvir, text="Prezime:")
        self.label_prezime.grid(row=0, column=2, padx=5, pady=5)
        self.entry_prezime = ttk.Entry(unos_okvir, width=30)
        self.entry_prezime.grid(row=0, column=3, padx=5, pady=5)

        self.label_telefon = ttk.Label(unos_okvir, text="Telefon:")
        self.label_telefon.grid(row=1, column=0, padx=5, pady=5)
        self.entry_telefon = ttk.Entry(unos_okvir, width=30)
        self.entry_telefon.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = ttk.Label(unos_okvir, text="E-pošta:")
        self.label_email.grid(row=1, column=2, padx=5, pady=5)
        self.entry_email = ttk.Entry(unos_okvir, width=30)
        self.entry_email.grid(row=1, column=3, padx=5, pady=5)

        # Kontrolni gumbi
        gumbi_okvir = tk.Frame(self.root)
        gumbi_okvir.pack(pady=5)
        
        self.gumb_dodaj = ttk.Button(gumbi_okvir, text="Dodaj kontakt", command=self.dodaj_kontakt)
        self.gumb_dodaj.pack(side="left", padx=5)

        self.gumb_uredi = ttk.Button(gumbi_okvir, text="Uredi odabrano", command=self.uredi_kontakt)
        self.gumb_uredi.pack(side="left", padx=5)

        self.gumb_obrisi = ttk.Button(gumbi_okvir, text="Obriši odabrano", command=self.obrisi_kontakt)
        self.gumb_obrisi.pack(side="left", padx=5)
        
        # Pretraživanje
        self.okvir_pretraga = tk.Frame(self.root)
        self.okvir_pretraga.pack(pady=5)
        self.label_pretraga = ttk.Label(self.okvir_pretraga, text="Pretraži:")
        self.label_pretraga.pack(side="left", padx=5)
        self.entry_pretraga = ttk.Entry(self.okvir_pretraga, width=40)
        self.entry_pretraga.pack(side="left", padx=5)
        self.entry_pretraga.bind("<KeyRelease>", self.filtriraj_kontakte)

        # Treeview za prikaz kontakata
        stupci = ("id", "ime", "prezime", "telefon", "email")
        self.tree = ttk.Treeview(self.root, columns=stupci, show="headings")
        self.tree.pack(padx=10, pady=5, fill="both", expand=True)

        self.tree.heading("id", text="ID")
        self.tree.heading("ime", text="Ime")
        self.tree.heading("prezime", text="Prezime")
        self.tree.heading("telefon", text="Telefon")
        self.tree.heading("email", text="E-pošta")

        self.tree.column("id", width=30, anchor="center")
        self.tree.column("ime", width=120)
        self.tree.column("prezime", width=120)
        self.tree.column("telefon", width=120)
        self.tree.column("email", width=150)
        
        self.tree.bind("<Double-1>", self.ucitaj_za_uredjivanje)

    def prikazi_kontakte(self):
        """Učitava sve kontakte iz baze i prikazuje ih u Treeview-u."""
        for redak in self.tree.get_children():
            self.tree.delete(redak)
        
        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        c.execute("SELECT * FROM kontakti ORDER BY prezime, ime")
        kontakti = c.fetchall()
        for kontakt in kontakti:
            self.tree.insert("", tk.END, values=kontakt)
        conn.close()

    def dodaj_kontakt(self):
        """Dodaje novi kontakt u bazu podataka."""
        ime = self.entry_ime.get().strip()
        prezime = self.entry_prezime.get().strip()
        telefon = self.entry_telefon.get().strip()
        email = self.entry_email.get().strip()

        if not ime or not prezime:
            messagebox.showwarning("Upozorenje", "Ime i prezime su obavezni!")
            return

        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        c.execute("INSERT INTO kontakti (ime, prezime, telefon, email) VALUES (?, ?, ?, ?)",
                  (ime, prezime, telefon, email))
        conn.commit()
        conn.close()

        self.ocisti_unos()
        self.prikazi_kontakte()
        messagebox.showinfo("Uspjeh", "Kontakt uspješno dodan!")

    def obrisi_kontakt(self):
        """Briše odabrani kontakt iz baze podataka."""
        odabrani = self.tree.selection()
        if not odabrani:
            messagebox.showwarning("Upozorenje", "Odaberite kontakt za brisanje.")
            return

        id_kontakt = self.tree.item(odabrani)["values"][0]
        
        if messagebox.askyesno("Potvrda brisanja", "Jeste li sigurni da želite obrisati ovaj kontakt?"):
            conn = sqlite3.connect(self.db_ime)
            c = conn.cursor()
            c.execute("DELETE FROM kontakti WHERE id=?", (id_kontakt,))
            conn.commit()
            conn.close()
            self.prikazi_kontakte()
            messagebox.showinfo("Uspjeh", "Kontakt uspješno obrisan!")

    def ucitaj_za_uredjivanje(self, event):
        """Popunjava polja za unos podacima odabranog kontakta."""
        odabrani = self.tree.selection()
        if odabrani:
            vrijednosti = self.tree.item(odabrani)["values"]
            self.ocisti_unos()
            self.entry_ime.insert(0, vrijednosti[1])
            self.entry_prezime.insert(0, vrijednosti[2])
            self.entry_telefon.insert(0, vrijednosti[3])
            self.entry_email.insert(0, vrijednosti[4])
            
            # Dodatno, spremamo ID kontakta za lakše ažuriranje
            self.gumb_uredi.config(text="Spremi izmjene", command=self.spremi_uredjivanje)
            self.id_za_uredjivanje = vrijednosti[0]

    def spremi_uredjivanje(self):
        """Sprema izmijenjene podatke u bazu podataka."""
        ime = self.entry_ime.get().strip()
        prezime = self.entry_prezime.get().strip()
        telefon = self.entry_telefon.get().strip()
        email = self.entry_email.get().strip()

        if not ime or not prezime:
            messagebox.showwarning("Upozorenje", "Ime i prezime su obavezni!")
            return

        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        c.execute("""
            UPDATE kontakti
            SET ime=?, prezime=?, telefon=?, email=?
            WHERE id=?
        """, (ime, prezime, telefon, email, self.id_za_uredjivanje))
        conn.commit()
        conn.close()

        self.ocisti_unos()
        self.gumb_uredi.config(text="Uredi odabrano", command=self.uredi_kontakt)
        self.prikazi_kontakte()
        messagebox.showinfo("Uspjeh", "Kontakt uspješno uređen!")

    def uredi_kontakt(self):
        """Dummy funkcija koja služi kao preklopnik."""
        odabrani = self.tree.selection()
        if odabrani:
            self.ucitaj_za_uredjivanje(None)
        else:
            messagebox.showwarning("Upozorenje", "Odaberite kontakt za uređivanje.")
            
    def filtriraj_kontakte(self, event):
        """Filtrira kontakte na temelju unosa u polje za pretragu."""
        unos = self.entry_pretraga.get().strip().lower()
        for redak in self.tree.get_children():
            self.tree.delete(redak)

        conn = sqlite3.connect(self.db_ime)
        c = conn.cursor()
        upit = """
            SELECT * FROM kontakti 
            WHERE lower(ime) LIKE ? OR lower(prezime) LIKE ? OR lower(telefon) LIKE ? OR lower(email) LIKE ?
            ORDER BY prezime, ime
        """
        c.execute(upit, (f"%{unos}%", f"%{unos}%", f"%{unos}%", f"%{unos}%"))
        kontakti = c.fetchall()
        for kontakt in kontakti:
            self.tree.insert("", tk.END, values=kontakt)
        conn.close()

    def ocisti_unos(self):
        """Briše sadržaj iz polja za unos."""
        self.entry_ime.delete(0, tk.END)
        self.entry_prezime.delete(0, tk.END)
        self.entry_telefon.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = KontaktApp(root)
    root.mainloop()
  
