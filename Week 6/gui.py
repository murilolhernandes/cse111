import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def main():
  root= tk.Tk()

  frm_main = Frame(root)
  frm_main.master.title("Area of A Circle")
  frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

  populate_main_window(frm_main)

  root.mainloop()

def populate_main_window(frm_main):
  lbl_radius = Label(frm_main, text="Radius:")
  ent_radius = IntEntry(frm_main, width=4, lower_bound=0)
  lbl_radius_units = Label(frm_main, text="meters")

  lbl_area = Label(frm_main, text="Area:")
  # a = π r2
  lbl_calc = Label(frm_main, width=5)
  lbl_area_units = Label(frm_main, text="square meter (m2)")

  btn_clear = Button(frm_main, text="Clear")

  lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
  ent_radius.grid(      row=0, column=1, padx=3, pady=3)
  lbl_radius_units.grid(row=0, column=2, padx=3, pady=3)

  lbl_area.grid(        row=1, column=0, padx=3, pady=3)
  lbl_calc.grid(        row=1, column=1, padx=3, pady=3)
  lbl_area_units.grid(  row=1, column=2, padx=3, pady=3)

  btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=3, sticky="w")

  def calculate(event):
    try:
      radius = ent_radius.get()
      area = math.pi * radius**2
      lbl_calc.config(text=f"{area:.2f}")
    
    except ValueError:
      lbl_calc.config(text="")

  def clear():
    btn_clear.focus()
    ent_radius.clear()
    lbl_calc.config(text="")
    ent_radius.focus()

  ent_radius.bind("<KeyRelease>", calculate)

  btn_clear.config(command=clear)
  ent_radius.focus()

if __name__ == "__main__":
  main()