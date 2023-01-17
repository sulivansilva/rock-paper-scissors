import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

escolha = int(input("Qual opção você escolhe? Digite 0 para 'Pedra', 1 para 'Papel' e 2 para 'Tesoura'.\n"))

while escolha >= 3:
    print("Opção inválida")
    break
else:    
    print("Você escolheu:")

    if escolha == 0:
        print(pedra)
    elif escolha == 1:
        print(papel)
    elif escolha == 2:
        print(tesoura)
       
    escolha_computador = random.randint(0,2)
    
    print("O computador escolheu: ")
    
    if escolha_computador == 0:
        print(pedra)
    elif escolha_computador == 1:
        print(papel)
    elif escolha_computador == 2:
        print(tesoura)
    
    if escolha == 0 and escolha_computador == 0:
        print("Empate!")
    elif escolha == 0 and escolha_computador == 1:
        print("Computador venceu!")        
    elif escolha == 0 and escolha_computador == 2:
        print("Você venceu!")        
    elif escolha == 1 and escolha_computador == 0:
        print("Você venceu!")        
    elif escolha == 1 and escolha_computador == 1:
        print("Empate!")
    elif escolha == 1 and escolha_computador == 2:
        print("Computador venceu!")        
    elif escolha == 2 and escolha_computador == 0:
        print("Computador venceu!")        
    elif escolha == 2 and escolha_computador == 1:
        print("Você venceu!")        
    else:
        print("Empate!")