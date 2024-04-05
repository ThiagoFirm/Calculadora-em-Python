from tkinter import *
from tkinter import ttk

cor1 = "#403d3a" #Cinza
cor2 = "#ffffff" #Branca
cor3 = "#1260de" #Azul
cor4 = "#000000" #Preta
cor5 = "#ff9900" # Laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x300")
janela.config(bg=cor1)


# criando frames
frame_tela = Frame(janela, width=235, height= 50, bg= cor1 )
frame_tela.grid(row=0, column = 0)

frame_corpo = Frame(janela, width=235, height= 268, bg = cor4)
frame_corpo.grid(row=1, column = 0)


# variavel todos valores
todos_valores = ''


# funcao para adicionar valor
def entrar_valor(exec):
    global todos_valores
    todos_valores = todos_valores + str(exec)

    #passando valor para a tela
    valor_texto.set(todos_valores)

# funcao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


# funcao para limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



# criando label
valor_texto = StringVar()

main_label = Label(frame_tela, textvariable= valor_texto, width = 16, height = 2, padx=7, relief=FLAT, anchor="e", justify= RIGHT, font=('Ivy 18'), bg=cor1, fg= cor2)
main_label.place(x=0, y=0)


# cirando butões
b_1 = Button(frame_corpo, text = "C", width = 11, height = 2,
              font = ('Ivy 13 bold'), relief = RAISED,
             overrelief=RIDGE, command = limpar_tela)
b_1.place(x=0,y=0)

b_2 = Button(frame_corpo, text = "%", width = 5, height = 2, 
             font = ('Ivy 13 bold'), relief = RAISED,
             overrelief=RIDGE, command = lambda: entrar_valor('%'))
b_2.place(x=118,y=0)

b_3 = Button(frame_corpo, text = "/", width = 5, height = 2,
              bg = cor5, fg =cor2, font = ('Ivy 13 bold'),
              relief = RAISED, overrelief=RIDGE, command = lambda: entrar_valor('/'))
b_3.place(x=177,y=0)

b_4 = Button(frame_corpo, text ="7", width = 5, height = 2, 
             font  = ('Ivy 13 bold'), relief= RAISED,
             overrelief= RIDGE, command = lambda: entrar_valor('7'))
b_4.place(x=0, y=50)

b_5 = Button(frame_corpo, text ="8", width = 5, height = 2, 
             font  = ('Ivy 13 bold'), relief= RAISED,
             overrelief= RIDGE, command = lambda: entrar_valor('8'))
b_5.place(x=59, y=50)

b_6 = Button(frame_corpo, text ="9", width = 5, height = 2, 
             font  = ('Ivy 13 bold'), relief= RAISED,
             overrelief= RIDGE, command = lambda: entrar_valor('9'))
b_6.place(x=118, y=50)

b_7 = Button(frame_corpo, text ="*", width = 5, height = 2,
              bg = cor5, fg= cor2, font  = ('Ivy 13 bold'),
              relief= RAISED, overrelief= RIDGE, command = lambda: entrar_valor('*'))
b_7.place(x=177, y=50)

b_8 = Button(frame_corpo, text ="4", width = 5, height = 2, 
             font  = ('Ivy 13 bold'), relief= RAISED,
             overrelief= RIDGE, command = lambda: entrar_valor('4'))
b_8.place(x=0, y=100)

b_9 = Button(frame_corpo, text ="5", width = 5, height = 2, 
             font  = ('Ivy 13 bold'), relief= RAISED,
             overrelief= RIDGE, command = lambda: entrar_valor('5'))
b_9.place(x=59, y=100)

b_10 = Button(frame_corpo, text ="6", width = 5, height = 2, 
              font  = ('Ivy 13 bold'), relief= RAISED,
              overrelief= RIDGE, command = lambda: entrar_valor('6'))
b_10.place(x=118, y=100)

b_11 = Button(frame_corpo, text ="-", width = 5, height = 2,
               bg= cor5, fg= cor2, font  = ('Ivy 13 bold'),
               relief= RAISED, overrelief= RIDGE, command = lambda: entrar_valor('-'))
b_11.place(x=177, y=100)

b_12 = Button(frame_corpo, text ="1", width = 5, height = 2, 
              font  = ('Ivy 13 bold'), relief= RAISED,
              overrelief= RIDGE, command = lambda: entrar_valor('1'))
b_12.place(x=0, y=150)

b_13 = Button(frame_corpo, text ="2", width = 5, height = 2, 
              font  = ('Ivy 13 bold'), relief= RAISED,
              overrelief= RIDGE, command = lambda: entrar_valor('2'))
b_13.place(x=59, y=150)

b_14 = Button(frame_corpo, text ="3", width = 5, height = 2, 
              font  = ('Ivy 13 bold'), relief= RAISED,
              overrelief= RIDGE, command = lambda: entrar_valor('3'))
b_14.place(x=118, y=150)

b_15 = Button(frame_corpo, text ="+", width = 5, height = 2,
               bg = cor5, fg= cor2, font  = ('Ivy 13 bold'),
               relief= RAISED, overrelief= RIDGE, command = lambda: entrar_valor('+'))
b_15.place(x=177, y=150)

b_16 = Button(frame_corpo, text ="0", width = 11, height = 2, 
              font  = ('Ivy 13 bold'), relief= RAISED,
              overrelief= RIDGE, command = lambda: entrar_valor('0'))
b_16.place(x=0, y=200)

b_17 = Button(frame_corpo, text =".", width = 5, height = 2, 
              font  = ('Ivy 13 bold'), relief= RAISED,
              overrelief= RIDGE, command = lambda: entrar_valor('.'))
b_17.place(x=118, y=200)

b_18 = Button(frame_corpo, text ="=", width = 5, height = 2,
               bg = cor5, fg = cor2, font  = ('Ivy 13 bold'),
               relief= RAISED, overrelief= RIDGE, command = calcular)
b_18.place(x=177, y=200)


janela.mainloop()