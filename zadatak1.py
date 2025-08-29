import tkinter as tk

def promijeni_tekst():
    """Mijenja tekst u labeli u 'Pozdrav, svijete!'."""
    label.config(text="Pozdrav, svijete!")

# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Pozdrav svijetu")
root.geometry("300x200")

# Kreiranje labele
label = tk.Label(root, text="")
label.pack(pady=20)

# Kreiranje gumba
gumb = tk.Button(root, text="Klikni me!", command=promijeni_tekst)
gumb.pack()

# Pokretanje glavne petlje Tkinter aplikacije
root.mainloop()
