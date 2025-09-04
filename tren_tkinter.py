from tkinter import *

# ----------------------
# ventana principal
# ----------------------
ventana_principal = Tk()
ventana_principal.title("graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("600x400")
ventana_principal.config(bg="white")

# -------------------------
# frame de graficacion
# -------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=580, height=380)
frame_graficacion.place (x=10,y=10)

# -----------------------
# lienzo de graficacion 
# -----------------------
c = Canvas(frame_graficacion, width=560, height=360)
c.config(bg="cyan")
c.place(x=10,y=10)

rectangulo_1 = c.create_rectangle(390,0, 510, 20,fill="orangered3", outline="orangered3")
rectangulo_2 = c.create_rectangle(370,20, 530, 40,fill="orangered3", outline="orangered3")
rectangulo_3 = c.create_rectangle(400,50, 500, 130, outline="grey33", width=20)
rectangulo_4 = c.create_rectangle(210,90, 240, 140, fill="grey33", outline="grey33")
rectangulo_5 = c.create_rectangle(200,70, 250, 90, fill="grey33", outline="grey33")
circulo_1 = c.create_oval(110,150,300, 290, fill= "black")
rectangulo_6 = c.create_rectangle(150,130, 180, 310, fill="grey33", outline="grey33")
rectangulo_7 = c.create_rectangle(200,140, 510, 300, fill="red4", outline="red4")
circulo_2 = c.create_oval(210,260,290, 340, fill= "grey", outline="grey")
circulo_3 = c.create_oval(320,260,400, 340, fill= "grey", outline="grey")
circulo_4 = c.create_oval(430,260,510, 340, fill= "grey", outline="grey")
rectangulo_8 = c.create_rectangle(275,290, 335, 315,fill="black")
rectangulo_9 = c.create_rectangle(385,290, 445, 315,fill="black")
texto_1 = c.create_text(350,210, anchor="center", text="Jhoasnel Jose", font=("arial", 20, "bold"), fill="cyan", activefill="blue")
circulo_5 = c.create_oval(410,45,490, 120, fill= "khaki1", outline="khaki1")
circulo_6 = c.create_oval(440,95,460, 115, fill= "red3", outline="red3")
circulo_7 = c.create_oval(425,65,445, 85, fill= "white", outline="white")
circulo_8 = c.create_oval(455,65,475, 85, fill= "white", outline="white")
circulo_8 = c.create_oval(460,70,470, 80, fill= "mediumpurple3", outline="mediumpurple3")
circulo_8 = c.create_oval(430,70,440, 80, fill= "mediumpurple3", outline="mediumpurple3")
linea_1 = c.create_line(430, 55, 445, 65, fill="black", width=2)
linea_1 = c.create_line(470, 55, 455, 65, fill="black", width=2)

# ----------------------------
# desplegar ventana principal
# ----------------------------
ventana_principal.mainloop()