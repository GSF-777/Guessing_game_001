from tkinter import *
from random import *

# Variáveis
tentativa = 1

def dificudade(escolha):
    global jogada_maq

    if escolha == "Easy":
        jogada_maq = randint(1,20)
    elif escolha == "Medium":
        jogada_maq = randint(1,30)
    elif escolha == "Hard":
        jogada_maq = randint(1,50)

    titulo.config(text=" Good Luck !!!")
    titulo.pack(pady=10)

    botao_f.pack_forget()
    botao_m.pack_forget()
    botao_d.pack_forget()
    

    entrada.pack(pady=10)
    botao_Check.pack(pady=10)
    botao_reiniciar.pack(padx=15)
    resultado.pack(pady=10)
    print(jogada_maq)
    

    

# Função para Check a jogada
def Check():
   
    global tentativa
    try:
        jogada_play = int(entrada.get())
    except ValueError:
        resultado.config(text="Please enter a valid number!!!")
        return

    print(jogada_maq)
    if jogada_play > jogada_maq:
        resultado.config(text="Nice try! ⬇️ Try lower.")
        tentativa += 1
    elif jogada_maq > jogada_play:
        resultado.config(text="Nice try! ⬆️ Try higher.")
        tentativa += 1

    else:
        if tentativa <= 3:
            resultado.config(text=f"🎉 Congratulations, You're lucky!\nTentativas: {tentativa}")
        else:
            resultado.config(text=f"🏆 Congratulations, You win!\nTentativas: {tentativa}")
        botao_Check.config(state="disabled")  # Desativa o botão ao vencer

# Função para reiniciar o jogo
def reiniciar():
    global jogada_maq, tentativa
    tentativa = 1

    botao_f.pack(pady=10)
    botao_m.pack(pady=10)
    botao_d.pack(pady=10)
    

    resultado.config(text=" ")
    resultado.pack_forget()


    entrada.delete(0, END)
    entrada.pack_forget()

    botao_Check.config(state="normal")
    botao_Check.pack_forget()

    botao_reiniciar.pack_forget()

    

# Janela principal
janela = Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("1000x500")

# Componentes da interface
titulo = Label(janela, text='Guessing game.\n Choose a difficulty.', font=("Arial", 16))
titulo.pack(pady=10)


botao_f = Button(janela, text="Easy", command=lambda: dificudade('Easy'))
botao_f.pack(pady=5)

botao_m = Button(janela, text='Medium', command=lambda: dificudade('Medium'))
botao_m.pack(pady=10)

botao_d = Button(janela, text='Hard', command=lambda: dificudade('Hard'))
botao_d.pack(pady=10)

botao_Check = Button(janela,text='Check', command=Check)
botao_reiniciar = Button(janela, text="Restart Game", command=reiniciar)
resultado = Label(janela, text="", font=("Arial", 12))

entrada = Entry(janela)

# Rodar a interface
janela.mainloop()
