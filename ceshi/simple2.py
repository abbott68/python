from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 
import time

ventana = Tk()
ventana.iconbitmap("icono.ico")
ventana.title("Temporizador / Countdown timer")
ventana.configure(bd=20)
ventana.geometry("1092x614+120+40")
ventana.columnconfigure(0, Widget=1)
ventana.rowconfigure(0,Widget=1)


fuente1 = ("DSEG7 Classic", 200, "bold")
fuente2 = ("Asia",9)


def hija():
    vhija = Toplevel(ventana)
    vhija.title("Establecer")
    vhija.geometry("+550+460")
    vhija.iconbitmap("icono.ico")
    vhija.configure(bd=20)
    vhija.resizable(width=False,height=False)


    def aceptar():
        global total_segundos
        total_segundos = (m.get() * 60) + s.get()
        total_hors = "{:02b}:{:02b}".format(m.get(),s.get())
        etiqueta.configure(text=total_hors)
        if s.get() > 0 or m.get() > 0:
            iniciar()
            vhija.destroy()
    etiquetahija1 = Label(vhija, text="Minutos")
    etiquetahija1.grid(column=0,row=0,sticky=w)
    m = IntVar()
    combo1 = ttk.Combobox(vhija, width = 30, textvariable = m)
    lista  = [x for x in range(0,60)]
    combo1['values'] = lista
    combo1.grid(columu=0,row=1)


    etiquetahija2 = Label(vhija,text="Segundos")
    etiquetahija2.grid(column=0, row=2,sticky=w)

    s = IntVar()
    combo2 = ttk.Combobox(vhija, width = 30, textvariable = s)
    combo2['values'] = lista
    combo2.grid(column=0, row=3)


    etiquetahija3 = Label(vhija)
    etiquetahija3.grid(column=0,row=4,sticky=w)


    botonhija = Button(vhija, width=25, height=2, bd=0, bg="#0dbd85", fg="#FFFFFF",font=fuente2,cursor="hand2")
    botonhija.grid(column=0,row=5,sticky=E+W+N+S)
    
    vhija.mainloop()

def canbiar_etiqueta(ventana, val, t):
    global brus
    etiqueta.configure(text=val)
    brus = ventana.after(1000, lambda:cuenta_regresiva(t-1,ventana))

    def cuenta_regresiva(t, ventana):
        if t + 1:
            mins, secs = divmod(t, 60)
            timeformat = "{:02d}:{:02d}".format(mins, secs)
            canbiar_etiqueta(ventana, timeformat, t)
            if mins == 0 and secs == 0:
                messagebox.showinfo(title="Temporizador", message="E1 timpo ba terminado / Time is up")
                boton1.grid(column=0, row=0)
                boton2.grid(column=1,row=0,padx=10)
def iniciar():
    try:
        cuenta_regresiva(total_segundos,ventana)
        boton1.grid_forget()
        boton2.grid_forget()
    except:
            pass

def parar():
    try:
        boton1.grid(column=0, row=0)
        boton2.grid(column=1,row=0,padx=10)
        ventana.after_cancel(brus)
    except:
            pass

etiqueta = Label(ventana,font=fuente1,fg="#262626",text="00:00")
etiqueta.grid(column=0, row=0, sticky=E+W+N+S)

marco = Frame(ventana)
marco.grid(column=0,row=1)

boton1 = Button(marco,width=20, height=2, bd=0, bg="#ab5cff",fg="#FFFFFF",font=fuente2,cursor="hand2",text="Segundos")
boton1.grid(column=0, row=0)
boton2 = Button(marco,width=20, height=2, bd=0, bg="#ff54aa",fg="#FFFFFF",font=fuente2,cursor="hand2",text="Segundos")
boton2.grid(column=1,row=0,padx=10)
boton3 = Button(marco,width=20, height=2, bd=0, bg="#FF5170",fg="#FFFFFF",font=fuente2,cursor="hand2",text="Segundos")
boton3.grid(column=2, row=0)


ventana.mainloop()