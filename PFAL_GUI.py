import numpy as np
import customtkinter as ctk
import PFAL

pf = PFAL.PFAL()

class App(ctk.CTk):
  
  def __init__(self):
    super().__init__()

    self.title("PFAL")
    self.geometry("650x400")
    self.title("PFAL")
    self.resizable(False, False)
    ctk.set_default_color_theme("themes/marsh.json")
    self.grid_columnconfigure(0, weight=1)

    self.titulo = ctk.CTkLabel(self, text="PizzApp", font=("PoetsenOne", 60))
    self.titulo.grid(row=0, column=0, padx=20, pady=20)

    self.option_label = ctk.CTkLabel(self, text="Escoge una pizza:", fg_color="transparent", font=("PoetsenOne", 12))
    self.option_label.grid(row=1, column=0, sticky="W", padx=10)

    self.optionmenu_var = ctk.StringVar(value="Pizza 1")
    self.optionmenu = ctk.CTkOptionMenu(self,values=["Pizza 1", "Pizza 2", "Pizza 3"], command=self.optionmenu_callback, variable=self.optionmenu_var, font=("PoetsenOne", 12))
    self.optionmenu.grid(row=2, column=0,sticky="W", padx=10, pady=10)

    self.ingredientes_label = ctk.CTkLabel(self, text="Ingredientes:\n"+pf.ingredientes(0), fg_color="transparent", font=("PoetsenOne", 12))
    self.ingredientes_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    self.inventario_label = ctk.CTkLabel(self, text="Inventario:\n"+pf.strinventario(), fg_color="transparent", font=("PoetsenOne", 12))
    self.inventario_label.grid(row=1, column=0, padx=10, pady=10)
  
    self.button_descontar = ctk.CTkButton(self, text="Fabricar", font=("PoetsenOne", 12), command=self.fabricar_pizza)
    self.button_descontar.grid(row=4, column=0, padx=10, pady=10)

  def optionmenu_callback(self, choice):
    print("optionmenu dropdown clicked:", choice)
    num_pizza = (int(choice[-1])- 1)
    self.ingredientes_label.configure(text="Ingredientes:\n"+pf.ingredientes(num_pizza))
    self.update()

  def fabricar_pizza(self):
    num_pizza = (int(self.optionmenu_var.get()[-1]) - 1)
    if pf.descontar(pf.getPizzas()[num_pizza]) == 0:
        self.inventario_label.configure(text="Inventario:\n"+pf.strinventario())
        self.update()
    else:
        print("No hay suficiente inventario")
    self.update()
    

app = App()
app.mainloop()