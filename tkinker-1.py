# VIDEO UTILIZADO PARA APRENDERLO FAST: https://www.youtube.com/watch?v=MpkTYMzhV0A

import tkinter as tk

#instancia de TkInter.
app = tk.Tk()

rutaOrigen = tk.StringVar(app)
entrada = tk.StringVar(app)


#   Configurando la GUI

app.geometry("300x600")
app.configure(background="gray")
tk.Wm.wm_title(app, "Copiador Neptuno")

def setRutaOrigen():
    rutaOrigen.set("Copiar - ruta origen "+entrada.get())

tk.Button(
    app,
    text="Copiar",
    font=("Courier", 14),
    bg="#00a8e8",
    fg="white",
    command= setRutaOrigen,
    relief="flat"
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Label(
    app,
    text="Ruta de origen",
    textvariable=rutaOrigen,
    fg="white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Entry(
    app,
    fg="white",
    bg="black",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True,
)
#   Main loop para la GUI.
app.mainloop()

