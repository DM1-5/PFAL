import customtkinter as ctk
import PFAL

pf = PFAL.PFAL() # Creacion de la instancia de la clase PFAL

class PizzaFrame(ctk.CTkFrame):
    """Frame que contiene los widtgets con informacion sobre las pizzas y botones para fabricar y comprarlas"""
    def __init__(self, master, app,info):
        super().__init__(master)
        self.app = app # Referencia a la instancia de la clase App
        self.info = info # Referencia a la instancia de la clase InfoFrame

        self.option_label = ctk.CTkLabel(self, text="Escoge una pizza:", fg_color="transparent", font=("PoetsenOne", 12) )
        self.option_label.grid(row=1, column=0, sticky="N", padx=10)

        self.optionmenu_var = ctk.StringVar(value="Pizza 1") # Variable que almacena la opcion seleccionada en el OptionMenu
        self.optionmenu = ctk.CTkOptionMenu(self,values=["Pizza 1", "Pizza 2", "Pizza 3"], 
                                            command=self.optionmenu_callback, 
                                            variable=self.optionmenu_var, 
                                            font=("Fira Code Light", 12))

        self.optionmenu.grid(row=2, column=0,sticky="N", padx=10, pady=10)

        self.ingredientes_label = ctk.CTkLabel(self, text="Ingredientes:\n"+pf.str_ingredientes(0), fg_color="transparent", font=("Fira Code Light", 12))
        self.ingredientes_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        self.precio_label = ctk.CTkLabel(self, text="Precio: $"+str(pf.precios[0]), fg_color="transparent", font=("Fira Code Light", 12))
        self.precio_label.grid(row=5, column=0, padx=10, pady=10, sticky="N")

        self.button_descontar = ctk.CTkButton(self, text="Fabricar", font=("PoetsenOne", 12), command=self.fabricar_pizza)
        self.button_descontar.grid(row=6, column=0, padx=10, pady=10)

        self.button_comprar = ctk.CTkButton(self, text="Comprar", font=("PoetsenOne", 12), command=self.comprar)
        self.button_comprar .grid(row=7, column=0, padx=10, pady=10)

    def comprar(self):
        """Metodo que se ejecuta al hacer click en el boton comprar, llama al metodo compra de la instancia de la clase App"""
        print("Abriendo ventana de compra")
        self.app.compra(False)

    def optionmenu_callback(self, choice):
        """Metodo que se ejecuta al seleccionar una opcion en el OptionMenu, actualiza los labels de ingredientes y precio"""
        print("Opcion seleccionada:", choice)
        num_pizza = (int(choice[-1])- 1)
        print("Numero de indice:", num_pizza)
        self.ingredientes_label.configure(text="Ingredientes:\n"+pf.str_ingredientes(num_pizza))
        self.precio_label.configure(text="Precio: $"+str(pf.precios[num_pizza]))
        self.info.actualizar()
    
    def fabricar_pizza(self):
        """Metodo que se ejecuta al hacer click en el boton fabricar, llama al metodo fabricar de la instancia de la clase PFAL"""
        num_pizza = (int(self.optionmenu_var.get()[-1]) - 1)
        if pf.fabricar(num_pizza) == 0:
            self.info.actualizar()
        else:
            print("No hay suficiente inventario")
            print("Abriendo ventana de compra con error de falta de inventario")
            self.app.compra(True)


class InfoFrame(ctk.CTkFrame):
    """Frame que contiene los labels con la informacion de las ventas y el inventario"""
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
        """Metodo que actualiza los labels con la informacion de las ventas y el inventario"""
        print("Actualizando labels")
        self.inventario_label.configure(text="Inventario:\n"+pf.str_inventario())
        self.ventas_label.configure(text="Cantidad vendida:\n"+pf.str_ventas())
        self.total_ventas_label.configure(text=f"Saldo total ventas: {pf.total_ventas()}")
        self.ventas_tipo_label.configure(text="Ventas por tipo:\n"+pf.str_ventasTipo())


    
class CheckFrame(ctk.CTkFrame):
    """Frame que contiene los Entry para ingresar la cantidad de ingredientes a comprar"""
    def __init__(self, master):
        super().__init__(master)

        self.x_label = ctk.CTkLabel(self, text="Harina", font=("Fira Code Light", 16))
        self.x_label.grid(row=0, column=1, padx=20, pady=20, sticky="W")

        self.optionmenu_var = ctk.StringVar(value="Pizza 1")

        self.entry_x = ctk.CTkEntry(self, font=("Fira Code Light", 12),width=30)
        self.entry_x.grid(row=1, column=1, padx=20, pady=20, sticky="WE")

        self.y_label = ctk.CTkLabel(self, text="Queso", font=("Fira Code Light", 16))
        self.y_label.grid(row=0, column=2, padx=20, pady=20, sticky="W")

        self.entry_y = ctk.CTkEntry(self, font=("Fira Code Light", 12),width=30)
        self.entry_y.grid(row=1, column=2, padx=20, pady=20, sticky="WE")

        self.z_label = ctk.CTkLabel(self, text="Tomate", font=("Fira Code Light", 16))
        self.z_label.grid(row=0, column=3, padx=20, pady=20, sticky="W")

        self.entry_z = ctk.CTkEntry(self, font=("Fira Code Light", 12),width=30)
        self.entry_z.grid(row=1, column=3, padx=20, pady=20, sticky="WE")

    def get(self):
        """Metodo que retorna una lista con la cantidad de ingredientes ingresada en los Entry"""
        return [int(self.entry_x.get()), int(self.entry_y.get()), int(self.entry_z.get())]


class Compra(ctk.CTkToplevel):
    """Toplevel que contiene los widgets para comprar ingredientes"""
    def __init__(self, error, info):
        super().__init__()
        self.error = error # Variable que indica si hay un error en la compra
        self.info = info # Referencia a la instancia de la clase InfoFrame
        self.geometry("350x400")
        self.resizable(False, False)
        self.title("Compra")

        # Label que indica si no hay suficiente inventario
        if error:
            self.label = ctk.CTkLabel(self, text="No hay suficiente inventario", text_color="red",font=("Fira Code Light", 16))
            self.label.grid(row=0, column=0, padx=20, pady=20)

        label = ctk.CTkLabel(self, text="¿Desea comprar más ingredientes?", font=("Fira Code Light", 12))
        label.grid(row=1, column=0, padx=20, pady=20)

        self.checks = CheckFrame(self)
        self.checks.grid(row=2, column=0, padx=20, pady=20, sticky="WENS")

        button_comprar = ctk.CTkButton(self, text="Comprar", font=("PoetsenOne", 12), command=self.comprar)
        button_comprar.grid(row=3, column=0, sticky="W", padx=20, pady=20)

        button_cancelar = ctk.CTkButton(self, text="Cancelar", font=("PoetsenOne", 12), command=self.salir)
        button_cancelar.grid(row=3, column=0, sticky="E", padx=20,pady=20)

    def comprar(self):
        """Metodo que se ejecuta al hacer click en el boton comprar, llama al metodo comprar de la instancia de la clase PFAL"""
        datos = self.checks.get()
        print("Se agregaron los datos",datos)
        pf.comprar(datos)
        self.info.actualizar()
        self.salir()

    def salir(self):
        """Metodo que se ejecuta al hacer click en el boton cancelar, cierra la ventana"""
        print("Cerrando ventana de compra")
        self.destroy()

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        # Seccion de configuracion de la ventana principal
        self.title("PFAL")
        self.geometry("500x600")
        self.resizable(False, False)
        # Tema de la aplicacion
        ctk.set_default_color_theme("themes/marsh.json")
        self.grid_columnconfigure(0, weight=1)

        self.titulo = ctk.CTkLabel(self, text="PizzApp", font=("PoetsenOne", 60))
        self.titulo.grid(row=0, column=0, padx=20, pady=20)

        self.info = InfoFrame(self)
        self.info.grid(row=2, column=0, sticky="NSE", padx=10, pady=10)
    
        self.frame = PizzaFrame(self,self,self.info)
        self.frame.grid(row=2, column=0,sticky="WNS",padx=10, pady=10)

        self.toplevel_window = None # Variable que almacena la referencia a la ventana Compra
        
    def compra(self, error):
            # verifica si la ventana ya fue creada
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                print("Creando ventana de compra")
                self.toplevel_window = Compra(error, self.info)  
            else:
                print("La ventana ya existe, focuseandol")
                self.toplevel_window.focus()  


app = App() # Creacion de la instancia de la clase App
app.mainloop() # Metodo que inicia el loop principal de la aplicacion