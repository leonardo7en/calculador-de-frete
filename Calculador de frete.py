
print('*************************************************************')
print("Bem vindo a loja do Leonardo Rodrigues")
print('*************************************************************')


valor = float (input('Entre com o valor unitário do produto:'))
quantidade = int (input('Entre com a quantidade desse produto:'))
semfrete = float (valor * quantidade)

print('O valor sem frete fica R$ {:.2f}.'.format(semfrete))

if (quantidade < 11):
    print ('O valor com frete foi de R$ {:.2f}.     (Frete foi de R$ 30.00) '.format(semfrete + 30))

elif (quantidade > 10 and quantidade < 101 ):
    print ('O valor com frete foi de R$ {:.2f}.     (Frete foi de R$ 60.00) '.format(semfrete + 60))

else:
 if (quantidade > 100 and quantidade < 1001 ):
    print ('O valor com frete foi de R$ {:.2f}.     (Frete foi de R$ 120.00) '.format(semfrete + 120))

 elif (quantidade > 1000):
    print ('O valor com frete foi de R$ {:.2f}.     (Frete foi de R$ 240.00) '.format(semfrete + 240))

print('Fim de programa!')