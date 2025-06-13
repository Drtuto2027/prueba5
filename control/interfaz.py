import tkinter as tk #importamos la libreria tkinter

# Crear una ventana
root = tk.Tk() #creamos la ventana y se llama root
root.title("Ejemplo de Widgets") #le damos un titulo a la venta con el .title
root.geometry("400x300") #con el .geometry le damos dimension a la ventana
root.resizable(False,False) #con el .resizable le decimos que la persona no pueda modificarle el tamaño

# Listbox 
listbox = tk.Listbox(root) #aca declaramos la listbox y le decimos que se ubique en la ventana
listbox.insert(1, "Opción 1") #vemos aca con el .insert le insertamos informacion a esta lista
listbox.insert(2, "Opción 2")
listbox.insert(3, "Opción 3")
listbox.pack() # el .pack nos sirve para que las cosas se ubiquen en el centro una detras de otras y no tener que estar poniendo donde deben de ir las cosas exactamente

# Checkbutton
var_check = tk.IntVar() #creamos una variable tipo IntVar y la asociamos al checkbutton para que esta variable tome el valor del checkbutton que tomamos
checkbutton = tk.Checkbutton(root, text="Acepto los términos", variable=var_check) 
checkbutton.pack() 

# Radiobutton
var_radio = tk.IntVar() #creamos una variable nueva y tambien la asociamos a los radioButton para que tome el valor de lo que tomamos
radiobutton1 = tk.Radiobutton(root, text="Opción 1", value=1, variable=var_radio) #tenemos 3 radiobutton cada uno con un valor diferente
radiobutton2 = tk.Radiobutton(root, text="Opción 2", value=2, variable=var_radio)
radiobutton3 = tk.Radiobutton(root, text="Opción 3", value=3, variable=var_radio)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# Menú
menu = tk.Menu(root) 
root.config(menu=menu) 

# Ejecutar la ventana
root.mainloop() #si no hacemos uso del mainloop, la ventana no se abriria, es como un codigo que se repite hasta que uno se sale de el 
