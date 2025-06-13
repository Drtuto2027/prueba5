import tkinter as tk
Ventana=tk.Tk()
Ventana.title("bienvenidos")
Ventana.geometry("800x400")
Ventana.resizable(0,0)

lblNom=tk.Label(Ventana,text="Nombre")
lblEdad=tk.Label(Ventana,text="Edad")
lblVoltage=tk.Label(Ventana,text="Voltage")

lblmesj=tk.Label(Ventana,text="bienvenido")

txtNom=tk.Entry(Ventana,width=5)
txtVoltage=tk.Entry(Ventana,width=5)
txtEdad=tk.Entry(Ventana,width=5)


lblNom.grid(row=0,column=0)
txtNom.grid(row=0,column=1)

lblVoltage.grid(row=0,column=1)
txtVoltage.grid(row=0,column=2)


lblEdad.grid(row=0,column=0)
txtEdad.grid(row=0,column=0)






Ventana.mainloop()