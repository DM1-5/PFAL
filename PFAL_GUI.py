import customtkinter as ctk
import PFAL

pf = PFAL.PFAL()

class PizzaFrame(ctk.CTkFrame):
    def __init__(self, master, app,info):
        super().__init__(master)
        self.app = app
        self.info = info
        self.option_label = ctk.CTkLabel(self, text="Escoge una pizza:", fg_color="transparent", font=("PoetsenOne", 12) )
        self.option_label.grid(row=1, column=0, sticky="N", padx=10)

        self.optionmenu_var = ctk.StringVar(value="Pizza 1")
        self.optionmenu = ctk.CTkOptionMenu(self,values=["Pizza 1", "Pizza 2", "Pizza 3"], command=self.optionmenu_callback, variable=self.optionmenu_var, font=("Fira Code Light", 12))
        self.optionmenu.grid(row=2, column=0,sticky="N", padx=10, pady=10)

        self.ingredientes_label = ctk.CTkLabel(self, text="Ingredientes:\n"+pf.str_ingredientes(0), fg_color="transparent", font=("Fira Code Light", 12))
        self.ingredientes_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        self.precio_label = ctk.CTkLabel(self, text="Precio: $"+str(pf.precios[0]), fg_color="transparent", font=("Fira Code Light", 12))
        self.precio_label.grid(row=5, column=0, padx=10, pady=10, sticky="N")

        self.button_descontar = ctk.CTkButton(self, text="Fabricar", font=("PoetsenOne", 12), command=self.fabricar_pizza)
        self.button_descontar.grid(row=6, column=0, padx=10, pady=10)
      
    def optionmenu_callback(self, choice):
      print("optionmenu dropdown clicked:", choice)
      num_pizza = (int(choice[-1])- 1)
      self.ingredientes_label.configure(text="Ingredientes:\n"+pf.str_ingredientes(num_pizza))
      self.precio_label.configure(text="Precio: $"+str(pf.precios[num_pizza]))
      self.info.actualizar()
      
    def fabricar_pizza(self):
      num_pizza = (int(self.optionmenu_var.get()[-1]) - 1)
      if pf.fabricar(num_pizza) == 0:
          self.info.actualizar()
      else:
          print("No hay suficiente inventario")
          self.app.insuficiente()
      
  
class InfoFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.inventario_label = ctk.CTkLabel(self, text="Inventario:\n"+pf.str_inventario(), fg_color="transparent", font=("Fira Code Light", 12))
        self.inventario_label.grid(row=1, column=0, padx=10, pady=10)

        self.ventas_label = ctk.CTkLabel(self, text="Cantidad vendida:\n"+pf.str_ventas(), fg_color="transparent", font=("Fira Code Light", 12))
        self.ventas_label.grid(row=2, column=0, padx=10, pady=10)

        self.total_ventas_label = ctk.CTkLabel(self, text=f"Saldo total ventas: {pf.total_ventas()}", fg_color="transparent", font=("Fira Code Light", 12))
        self.total_ventas_label.grid(row=3, column=0, padx=10, pady=10)

        self.ventas_tipo_label = ctk.CTkLabel(self, text="Ventas por tipo:\n"+pf.str_ventasTipo(), fg_color="transparent", font=("Fira Code Light", 12))
        self.ventas_tipo_label.grid(row=4, column=0, padx=10, pady=10)

    def actualizar(self):
        self.inventario_label.configure(text="Inventario:\n"+pf.str_inventario())
        self.ventas_label.configure(text="Cantidad vendida:\n"+pf.str_ventas())
        self.total_ventas_label.configure(text=f"Saldo total ventas: {pf.total_ventas()}")
        self.ventas_tipo_label.configure(text="Ventas por tipo:\n"+pf.str_ventasTipo())

class aaa(ctk.CTkToplevel):
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.label = ctk.CTkLabel(self, text="No hay suficiente inventario", text_color="red",font=("Fira Code Light", 20))
        self.label.pack(padx=20, pady=20)



class App(ctk.CTk):
  
  def __init__(self):
    super().__init__()

    self.title("PFAL")
    self.geometry("500x600")
    self.resizable(False, False)
    ctk.set_default_color_theme("themes/marsh.json")
    self.grid_columnconfigure(0, weight=1)

    self.titulo = ctk.CTkLabel(self, text="PizzApp", font=("PoetsenOne", 60))
    self.titulo.grid(row=0, column=0, padx=20, pady=20)

    self.info = InfoFrame(self)
    self.info.grid(row=2, column=0, sticky="NSE", padx=10, pady=10)
  
    self.frame = PizzaFrame(self,self,self.info)
    self.frame.grid(row=2, column=0,sticky="WNS",padx=10, pady=10)

    self.toplevel_window = None
    
  def insuficiente(self):
          if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
              self.toplevel_window = aaa(self)  
          else:
              self.toplevel_window.focus()  


app = App()
app.mainloop()