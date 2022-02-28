print("\n  Tabuada\n")
print("-"*80)
numero = int(input('\nDigite o número que deseja ver a tabuada:'))
for contador in range(10):
    print(" {} x {:2} = {} ".format(numero, contador+1, numero*(contador+1)) )

print("-"*80)
input("\nDigite qualquer tecla para fechar o programa")

#Desenvolvido em 25/02/2022 por Lino gomes ( https://github.com/linoabreu/ )
