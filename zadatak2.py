import tkinter as tk

class BrojacApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brojač")
        self.root.geometry("250x150")

        # Inicijalizacija brojača s IntVar
        self.broj = tk.IntVar(value=0)

        # Kreiranje labele koja prikazuje vrijednost brojača
        self.labela_broja = tk.Label(root, textvariable=self.broj, font=("Helvetica", 24))
        self.labela_broja.pack(pady=10)

        # Kreiranje okvira za gumbe
        self.okvir_gumba = tk.Frame(root)
        self.okvir_gumba.pack()

        # Gumb za smanjivanje
        self.gumb_smanji = tk.Button(self.okvir_gumba, text="Smanji", command=self.smanji_broj)
        self.gumb_smanji.pack(side=tk.LEFT, padx=5)

        # Gumb za povećavanje
        self.gumb_povecaj = tk.Button(self.okvir_gumba, text="Povećaj", command=self.povecaj_broj)
        self.gumb_povecaj.pack(side=tk.LEFT, padx=5)

    def povecaj_broj(self):
        """Povećava vrijednost brojača za 1."""
        trenutni_broj = self.broj.get()
        self.broj.set(trenutni_broj + 1)

    def smanji_broj(self):
        """Smanjuje vrijednost brojača za 1."""
        trenutni_broj = self.broj.get()
        self.broj.set(trenutni_broj - 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrojacApp(root)
    root.mainloop()
  
