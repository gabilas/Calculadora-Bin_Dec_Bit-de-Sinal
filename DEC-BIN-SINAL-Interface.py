from tkinter import *

def calculadora():

    texto4["text"] = ""  
    texto4["text"] = "Insira um Valor"
    num = int(ent_valor.get())
       
    if num < 0:
            
        num_bin = bin(num)[3:]
        tamanho_bin = len(num_bin)
        bin_inverso = ''
                
        for i in num_bin: 
            if i == '0': 
                bin_inverso += '1'
                    
            else: 
                bin_inverso += '0'
                              
        bin_1 = bin(int(bin_inverso, 2))[2:].zfill(tamanho_bin)
        bin_2 = bin(int('1', 2))[2:].zfill(4)
        bin_soma = bin(int(bin_1,2) + int(bin_2,2))[2:].zfill(tamanho_bin)
        bin_final = '1 '
                               
        for i in bin_soma:
            bin_final += i

                       
        texto4["text"] = ""                                
        texto4["text"] += "A resposta com bit de sinal é: " 
        texto4["text"] += bin_final
                               
    else: 
        
        count = 0
        num_bin = bin(num)[2:]
        tamanho_bin = len(num_bin)
        bin_final = '0 '
                        
        for i in num_bin:
            bin_final += i
            
               
        texto4["text"] = "" 
        texto4["text"] += "A resposta com bit de sinal é:  " 
        texto4["text"] += bin_final
        
        
     

janela = Tk()

janela.title("Conversor Decimal para Binário com Bit de Sinal")
janela.geometry("550x350")
janela.configure(background="#008")

texto1 = Label(janela, text = "Bem vindo ao conversor de número Decimal para número Binário", background="#008", foreground="#fff")
texto1.place(x=100, y=50)     

texto2 = Label(janela, text = "==========================================", background="#008", foreground="#fff")
texto2.place(x=100, y=100)     

texto3 = Label(janela, text = "Digite o número decimal. Caso seja um número negativo digite '-' antes do número.", background="#008", foreground="#fff")
texto3.place(x=50, y=180)

ent_valor = Entry(janela, text = "Digite o número decimal: ", justify="center")
ent_valor.place(x=210, y=220)

calcular = Button(janela, text="Calcular", command = calculadora)
calcular.place(x=250, y=250)

texto4 = Label(janela, text = "Insira um Valor!!!", background="#008", foreground="#fff")
texto4.place(x=150, y=300, width=250, height=50)



janela.mainloop()   
