from tkinter import *
from tkinter import ttk
#Cores
cor1= "#000504"
cor2= "#38576b"
cor3= "#ECEFF1"
cor4= "#FFAB40"
cor5= "#feffff"
fundo= "#3b3b3b"

#--------------------------------------------------------------

#Janela Principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("231x323")

#Criado o Frame
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)
frame_janela = Frame(janela, width=300, height=56, bg= cor1, relief="flat",)
frame_janela.grid(row=0, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340,bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=1, column=0, sticky=NW)

#Label
app_janela = Label(frame_janela,text="123456789", width=16, height=2, relief="flat", anchor="e", bd=0, justify=RIGHT, font="Ivy 18", bg= '#37474F', fg=cor5)


#Botões da calculadora    

b1 = Button(janela, text="1",command=lambda: entrar_valor("1"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=270)

b2 = Button(janela, text="2",command=lambda: entrar_valor("2"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b2.place(x=55, y=270)

b3 = Button(janela, text="3",command=lambda: entrar_valor("3"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b3.place(x=110, y=270)

b0 = Button(janela, text="0",command=lambda: entrar_valor("0"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b0.place(x=169, y=270)

b4 = Button(janela, text="4",command=lambda: entrar_valor("4"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=221)

b5 = Button(janela, text="5",command=lambda: entrar_valor("5"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b5.place(x=55, y=221)

b6 = Button(janela, text="6",command=lambda: entrar_valor("6"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b6.place(x=110, y=221)

b7 = Button(janela, text="7",command=lambda: entrar_valor("7"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=172)

b8 = Button(janela, text="8",command=lambda: entrar_valor("8"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b8.place(x=55, y=172)

b9 = Button(janela, text="9",command=lambda: entrar_valor("9"), width=5, height=2,fg=cor5, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
b9.place(x=110, y=172)

bclear = Button(janela,command = lambda: limpar_tela(), text="C", width=5, height=2, fg=cor4,font=('Ivy 13 bold'),bg=cor2, relief=RAISED, overrelief=RIDGE)
bclear.place(x=0, y=121)

bdiv = Button(janela, text="/",command=lambda: entrar_valor("/"), width=5, height=2,fg=cor4, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
bdiv.place(x=55, y=121)

bequal = Button(janela ,command = lambda: calc(), text="=", width=5, height=2, bg=cor2,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
bequal.place(x=169, y=221)

bsub = Button(janela, text="-",command=lambda: entrar_valor("-"), width=5, height=2,fg=cor4, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
bsub.place(x=169, y=172)

bmult = Button(janela, text="x",command=lambda: entrar_valor("*"), width=5, height=2,fg=cor4, font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
bmult.place(x=110, y=121)

badicao = Button(janela, text="+",command=lambda: entrar_valor("+"), width=5, height=2,fg = cor4,font="Ivy 13 bold", bg=cor2, relief=RAISED, overrelief=RIDGE)
badicao.place(x=169, y=121)




#para armazenar todas as expressões que serão avaliadas
todos_valores = ""

# para entrada de valor único
valor_texto = StringVar()

#Funções de entrada de valores
def entrar_valor(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)
    
#Função de calc resultado    
def calc():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""
    
#Função de Limpar    
def limpar_tela(): 
    global todos_valores
    todos_valores = "" 
    valor_texto.set("")

app_scream = Label(frame_janela,textvariable=valor_texto,width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=cor1)
app_scream.place(x=0, y=0)

janela.mainloop()