try:

    opcao = int(input("digite o que deseja fazer: \n1 - fazer pix \n2- extrato \n3- depositar \n4 sair "))
    if opcao == 1:
        valor = input("digite o valor desejado: ")
        quem = input("digite o {valor} para {alguem}  ")
        print("Pix realizado com sucesso! ")
    elif opcao == 2:
        print("extrato bancário: ")
    elif opcao == 3:
        valor = input("digite o valor do depósito: ")
        print(f"Depósito de dinheiro{valor} realizado com sucesso")
        
    elif opcao == 4:
        print("saindo do sistema...")
        
    print("opcçao invalida. por favor tente de novo")

except ValueError:
    print("Erro: digite apenas numeros validos.")
