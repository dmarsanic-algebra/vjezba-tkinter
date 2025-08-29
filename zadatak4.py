import tkinter as tk
from tkinter import messagebox

# Ime datoteke za pohranu zadataka
IME_DATOTEKE = "zadaci.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do lista")
        self.root.geometry("400x400")

        # Okvir za gornji dio (unos)
        self.gornji_okvir = tk.Frame(root)
        self.gornji_okvir.pack(pady=10)

        self.entry_zadatak = tk.Entry(self.gornji_okvir, width=30)
        self.entry_zadatak.pack(side=tk.LEFT, padx=5)

        self.gumb_dodaj = tk.Button(self.gornji_okvir, text="Dodaj zadatak", command=self.dodaj_zadatak)
        self.gumb_dodaj.pack(side=tk.LEFT, padx=5)

        # Okvir za listbox i scrollbar
        self.listbox_okvir = tk.Frame(root)
        self.listbox_okvir.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.listbox_zadaci = tk.Listbox(self.listbox_okvir, height=15, selectmode=tk.SINGLE)
        self.listbox_zadaci.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.listbox_okvir)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_zadaci.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_zadaci.yview)

        # Okvir za donje gumbe
        self.donji_okvir = tk.Frame(root)
        self.donji_okvir.pack(pady=10)

        self.gumb_brisi = tk.Button(self.donji_okvir, text="Obriši odabrani", command=self.obrisi_zadatak)
        self.gumb_brisi.pack(side=tk.LEFT, padx=5)

        self.gumb_dovrseno = tk.Button(self.donji_okvir, text="Označi kao dovršeno", command=self.oznaci_dovrseno)
        self.gumb_dovrseno.pack(side=tk.LEFT, padx=5)

        # Učitavanje zadataka pri pokretanju
        self.ucitaj_zadatke()

    def ucitaj_zadatke(self):
        """Učitava zadatke iz datoteke i prikazuje ih u Listbox-u."""
        try:
            with open(IME_DATOTEKE, "r", encoding="utf-8") as f:
                zadaci = f.readlines()
            for zadatak in zadaci:
                self.listbox_zadaci.insert(tk.END, zadatak.strip())
        except FileNotFoundError:
            # Datoteka ne postoji, što je u redu pri prvom pokretanju
            pass
        except Exception as e:
            messagebox.showerror("Greška", f"Dogodila se greška prilikom učitavanja: {e}")

    def spremi_zadatke(self):
        """Sprema trenutne zadatke iz Listbox-a u datoteku."""
        try:
            with open(IME_DATOTEKE, "w", encoding="utf-8") as f:
                svi_zadaci = self.listbox_zadaci.get(0, tk.END)
                for zadatak in svi_zadaci:
                    f.write(f"{zadatak}\n")
        except Exception as e:
            messagebox.showerror("Greška", f"Dogodila se greška prilikom spremanja: {e}")

    def dodaj_zadatak(self):
        """Dodaje novi zadatak iz unosa u Listbox."""
        zadatak = self.entry_zadatak.get().strip()
        if zadatak:
            self.listbox_zadaci.insert(tk.END, zadatak)
            self.entry_zadatak.delete(0, tk.END)
            self.spremi_zadatke()
        else:
            messagebox.showwarning("Upozorenje", "Molimo unesite zadatak.")

    def obrisi_zadatak(self):
        """Briše odabrani zadatak iz Listbox-a."""
        try:
            indeks_odabrano = self.listbox_zadaci.curselection()[0]
            self.listbox_zadaci.delete(indeks_odabrano)
            self.spremi_zadatke()
        except IndexError:
            messagebox.showwarning("Upozorenje", "Molimo odaberite zadatak za brisanje.")

    def oznaci_dovrseno(self):
        """Označava odabrani zadatak kao dovršen."""
        try:
            indeks_odabrano = self.listbox_zadaci.curselection()[0]
            zadatak = self.listbox_zadaci.get(indeks_odabrano)
            if not zadatak.startswith("✔ "):
                self.listbox_zadaci.delete(indeks_odabrano)
                self.listbox_zadaci.insert(indeks_odabrano, f"✔ {zadatak}")
                self.spremi_zadatke()
        except IndexError:
            messagebox.showwarning("Upozorenje", "Molimo odaberite zadatak za označavanje.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
  
