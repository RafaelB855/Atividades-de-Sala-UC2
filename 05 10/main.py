from customtkinter import * 

app = CTk()
app.title("teste")
larguraPrograma = 800
alturaPrograma = 600
app.geometry(f"{larguraPrograma}x{alturaPrograma}")

app.grid_columnconfigure((0), weight=1)

tituloTopo = CTkLabel(master=app, text= "Ola mundo!", text_color="red",font=CTkFont(size=36,weight="bold"))
tituloTopo.grid(row=0,column=0, padx=20, pady=20)

corpoTexto = CTkLabel(master=app, text= "Este é meu programa!", text_color="blue",font=CTkFont(size=36,weight="bold"))
corpoTexto.grid(row=1,column=0, padx=20, pady=20)

app.mainloop()