#=====================================================================================TUTORIAL=========================================================================================================================================

print ('Neste jogo vc devera acertar senha digite um numero se vier -1 eh porque esse numero eh nao esta na lista se vier 0 eh porque esta na lista e se vier 1 e porque esse numero esta na lista mas voce nao deixou na ordem certa')
print ('Vamos começar')

#==================================================================================VARIAVEIS RANDOMICAS===================================================================================================================================

import sys
import random

senha1 = random.randint(0,9)
senha2 = random.randint(0,9)
senha3 = random.randint(0,9)
senha4 = random.randint(0,9)
senha5 = random.randint(0,9)

todasenhas = senha1, senha2, senha3, senha4, senha5

#=====================================================================================Processo=========================================================================================================================================

#print (senha1, senha2, senha3, senha4, senha5)      ////     para mim testar
vida = 10

#=====================================================================================Variaveis========================================================================================================================================
#
while vida > 0:
    print(vida)


#==============================================================================Variaveis para o jogador================================================================================================================================

    respsenha1 = int(input ('Digite um numero para a senha voce tera 10 chances'))
    

#==============================================================================DEFINIR SE O PLAYER GANHOU OU NAO=======================================================================================================================


    if respsenha1 == senha1:
            print ('+1')
            
    elif respsenha1 == senha1 or respsenha1 == senha2 or respsenha1 == senha3 or respsenha1 == senha4 or respsenha1 == senha5:
        
        print (' 0')
    else:
        print ('-1 ')

#==============================================================================Variaveis para o jogador================================================================================================================================

    respsenha2 = int(input ('Digite um numero para a senha voce tera 10 chances'))
    
#======================================================================================================================================================================================================================================
#==============================================================================DEFINIR SE O PLAYER GANHOU OU NAO=======================================================================================================================


    if respsenha2 == senha2:
            
            print ('+1')
    elif respsenha2 == senha1 or respsenha2 == senha3 or respsenha2 == senha4 or respsenha2 == senha5:

        print (' 0')
    else:
        print ('-1 ')

#==============================================================================Variaveis para o jogador================================================================================================================================

    respsenha3 = int(input ('Digite um numero para a senha voce tera 10 chances'))
    
#======================================================================================================================================================================================================================================
#==============================================================================DEFINIR SE O PLAYER GANHOU OU NAO=======================================================================================================================

    if respsenha3 == senha3:
            print ('+1')
    elif respsenha3 == senha1 or respsenha3 == senha2 or respsenha3 == senha4 or respsenha3 == senha5:
        print (' 0')
    else:
        print ('-1 ')

#==============================================================================Variaveis para o jogador================================================================================================================================

    respsenha4 = int(input('Digite um numero para a senha voce tera 10 chances'))
    
#======================================================================================================================================================================================================================================
#==============================================================================DEFINIR SE O PLAYER GANHOU OU NAO=======================================================================================================================


    if respsenha4 == senha4:
            print ('+1')
    elif respsenha4 == senha1 or respsenha4 == senha2 or respsenha4 == senha3 or respsenha4 == senha5:
        print (' 0')
    else:
        print ('-1 ')
        
#==============================================================================Variaveis para o jogador================================================================================================================================
        
    respsenha5 = int(input('Digite um numero para a senha voce tera 10 chances'))
    
#======================================================================================================================================================================================================================================
#==============================================================================DEFINIR SE O PLAYER GANHOU OU NAO=======================================================================================================================


    if respsenha5 == senha5:
            print ('+1')
    elif respsenha5 == senha1 or respsenha5 == senha2 or respsenha5 == senha3 or respsenha5 == senha4:
        print (' 0')
    else:
        print ('-1 ')

#=================================================================================GANHOU!===============================================================================================================================================


    todarespsenhas = respsenha1, respsenha2, respsenha3, respsenha4, respsenha5
    if todarespsenhas == todasenhas:
        print ('Você ganhou'), sys.exit()


#==============================================================================FIM DE JOGO!=============================================================================================================================================

    if vida == 1:
        print ('suas vidas acabaram'), sys.exit()
    vida -= 1


