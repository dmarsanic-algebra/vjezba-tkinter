import tkinter as tk

class KalkulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jednostavni kalkulator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Varijabla za pohranu izraza
        self.izraz = ""

        # Entry widget za prikaz unosa i rezultata
        self.entry_izlaz = tk.Entry(root, width=15, font=("Arial", 24), justify="right")
        self.entry_izlaz.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
        self.entry_izlaz.insert(0, "0")

        # Kreiranje gumba
        self.kreiraj_gumbe()

    def kreiraj_gumbe(self):
        """Kreira i postavlja gumbe na prozor."""
        gumbi = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        redak = 1
        stupac = 0
        for gumb in gumbi:
            tk.Button(self.root, text=gumb, font=("Arial", 18), width=5, height=2,
                      command=lambda gumb=gumb: self.pritisni_gumb(gumb)).grid(row=redak, column=stupac, padx=5, pady=5)
            stupac += 1
            if stupac > 3:
                stupac = 0
                redak += 1

    def pritisni_gumb(self, gumb):
        """Ažurira izraz ili ga izračunava ovisno o pritisnutom gumbu."""
        if gumb == "C":
            self.izraz = ""
            self.entry_izlaz.delete(0, tk.END)
            self.entry_izlaz.insert(0, "0")
        elif gumb == "=":
            try:
                # Upotrebom eval() funkcije procjenjujemo matematički izraz
                rezultat = str(eval(self.izraz))
                self.entry_izlaz.delete(0, tk.END)
                self.entry_izlaz.insert(0, rezultat)
                self.izraz = rezultat
            except (SyntaxError, ZeroDivisionError, NameError):
                self.entry_izlaz.delete(0, tk.END)
                self.entry_izlaz.insert(0, "Greška")
                self.izraz = ""
        else:
            if self.izraz == "" and gumb in ['+', '-', '*', '/']:
                # Sprječava da izraz započne s operatorom (osim - za negativne brojeve)
                if gumb != '-':
                    return
            self.izraz += str(gumb)
            self.entry_izlaz.delete(0, tk.END)
            self.entry_izlaz.insert(0, self.izraz)

if __name__ == "__main__":
    root = tk.Tk()
    app = KalkulatorApp(root)
    root.mainloop()
  
