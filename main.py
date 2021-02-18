from dolar import Dolar
from banco import BancoNacion,CajaAhorro

def main():
    dolar = Dolar(0,0,"https://www.bna.com.ar/Personas")
    #valor diario del dolar
    dolar.valor_dolar()
    banco = BancoNacion(33000000,10000000000,dolar)
    clientes = {"42374435": CajaAhorro(0,23243243232,224423,0,banco,dolar),"14376872":CajaAhorro(0,3243433,32325325325,0,banco,dolar)}
    
    cliente = clientes["42374435"]

    cliente.depositar_pesos(100000)

    cliente.comprar_dolares(500)

    print("Pesos: ",cliente.mostrar_pesos())

    print("")
    print("Dolares: ",cliente.mostrar_dolares())

    

main()
