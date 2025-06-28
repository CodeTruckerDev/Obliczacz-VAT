# Obliczacz VAT dla Mamy
# Rok powstania: ok. 2016–2017
# Autor: Piotr M. (CodeTruckerDev)

import tkinter as tk
from tkinter import messagebox, ttk

def show_tax(rate):
    # Oblicza wartości netto i VAT na podstawie kwoty brutto
    b = brutto.get()
    n = round(b / rate, 2)
    # Formatuje do stringa z dwoma cyframi po przecinku
    netto.set(format(n, '.2f'))
    t = round(b - n, 2)
    vat.set(format(t, '.2f'))

def message():
    messagebox.showinfo(':)', 'Mojej mamie - Żeby czasem było łatwiej.')

root = tk.Tk()
#root.geometry('308x200+250+250')
root.resizable(0, 0)
root.title('Obliczacz')

brutto = tk.DoubleVar()
netto = tk.StringVar()
vat = tk.StringVar()

ttk.Label(root, text='Wprowadź wartość brutto').grid(row=0, column=0, columnspan=5)

e = ttk.Entry(root, textvariable=brutto)
e.grid(row=1, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

ttk.Label(root, text='Wybierz stawkę podatku VAT').grid(row=2, column=0, columnspan=5)

b = ttk.Button(root, text='5 %', command=lambda r=1.05: show_tax(r))
b.grid(row=3, column=0, padx=5, pady=5)

b = ttk.Button(root, text='8 %', command=lambda r=1.08: show_tax(r))
b.grid(row=3, column=2, padx=5, pady=5)

b = ttk.Button(root, text='23 %', command=lambda r=1.23: show_tax(r))
b.grid(row=3, column=4, padx=5, pady=5)

ttk.Label(root).grid(row=4, column=0, columnspan=5)

ttk.Label(root, text='Netto', anchor='center').grid(row=5, column=0, columnspan=2, sticky='WE')
ttk.Label(root, text='VAT', anchor='center').grid(row=5, column=3, columnspan=2, sticky='WE')

l = ttk.Label(root, textvariable=netto, relief='raised', anchor='center')
l.grid(row=6, column=0, columnspan=2, sticky='WE', padx=3)

l = ttk.Label(root, textvariable=vat, relief='raised', anchor='center')
l.grid(row=6, column=3, columnspan=2, sticky='WE', padx=3)

b = ttk.Button(root, text='?', command=message)
b.grid(row=7, column=2)

root.mainloop()
