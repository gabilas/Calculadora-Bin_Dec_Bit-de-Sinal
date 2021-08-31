from tkinter import *

def calculadora():

    print("Bem vindo ao conversor de número Decimal para número Binário")
    print("==========================================")
    print("")
    print("Se quiser sair digite 'q', caso contrário entre com 'ENTER'")
    
    sair = input()
    
    while sair != 'q':
    
        num = int(input("Digite o número decimal: "))   
            
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
                                       
            print("")
            print('O número decimal {} convertido para binario com bit de sinal é: {}'.format(num, bin_final))
            print("")
        
            print("Se quiser sair digite 'q', caso contrário entre com 'ENTER'")
            sair = input()
                               
        else: 
                
            num_bin = bin(num)[2:]
            tamanho_bin = len(num_bin)
            bin_final = '0 '
                
            for i in num_bin:
                bin_final += i
                    
            print("")
            print('O número decimal {} convertido para binario com bit de sinal é: {}'.format(num,bin_final))
            print("")
        
            print("Se quiser sair digite 'q', caso contrário entre com 'ENTER'")
            sair = input()
calculadora()

app = Tk()

app.title("Teste")

app.mainloop()
