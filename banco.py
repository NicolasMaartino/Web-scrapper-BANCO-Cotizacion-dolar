from dolar import Dolar

class CajaAhorro:
    def __init__(self,pesos,cbu,numero_cta,dolares,banco,dolar):
        self.dolar = dolar
        self._banco = banco
        self._pesos = pesos
        self._dolares = dolares
        self._cbu = cbu
        self._numero_cta = numero_cta
    def mostrar_pesos(self):
        return self._pesos
    def mostrar_dolares(self):
        return self._dolares
    def depositar_pesos(self,cantidad):
        self._pesos += cantidad
    def retirar_pesos(self,cantidad):
        if self._pesos > cantidad:
            self._pesos -= cantidad
        else:
            print("Ha superado el limite de pesos de su cuenta.")
    def comprar_dolares(self,cantidad):
        conversion = self.dolar.conversion_compra(cantidad)
        if (self._pesos) >= conversion:
            self._dolares += cantidad
            self.retirar_pesos(conversion)
            self._banco.vender_dolares(cantidad)
        else:
            print("No se pudo realizar la transaccion por falta de dinero.")
    def vender_dolares(self,cantidad):
        conversion = self.dolar.conversion_venta(cantidad)
        if self._dolares >= cantidad:
            self._dolares -= cantidad
            self.depositar_pesos(conversion)
            self._banco.comprar_dolares(cantidad)
        else:
            print("No se realizo la transaccion por falta de dinero.")


class BancoNacion:
    def __init__(self,reservas_dolares,reservas_pesos,dolar):
        self.reservas_dolares = reservas_dolares
        self.reservas_pesos = reservas_pesos
        self.dolar = dolar

    def vender_dolares(self,dolares):
        conversion = self.dolar.conversion_compra(dolares)
        self.reservas_dolares -= dolares
        self.reservas_pesos += conversion
    
    def comprar_dolares(self,dolares):
        conversion = self.dolar.conversion_venta(dolares)
        self.reservas_dolares += dolares
        self.reservas_pesos -= pesos
