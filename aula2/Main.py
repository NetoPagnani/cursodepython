class Main:
    pass


print('Testando')

from cliente import Cliente

from conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome, 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()