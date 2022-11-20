def numero_perfeito(num):

    print("Descubra se o numero é perfeito")
    # num = int(input("Digite o numero:"))
    soma = 0
    
    for divisor in range(1,num):
        if num % divisor == 0:
            soma += divisor

    if num == soma:
        print(num, "é um numero perfeito")
    else:
        print(num, "Nao é um numero perfeito")

numero_perfeito() 

