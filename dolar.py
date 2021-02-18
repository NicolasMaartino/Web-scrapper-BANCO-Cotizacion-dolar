import requests
from bs4 import BeautifulSoup
class Dolar:
    def __init__(self,compra,venta,url):
        self.compra = compra
        self.venta = venta
        self.url = url

    def conversion_compra(self,unidades):
        return float(unidades)*(float(self.compra))
    def conversion_venta(self,unidades):
        return float(unidades)*(float(self.compra))
    
    def valor_dolar(self):
        respuesta = requests.get(self.url)
        soup = BeautifulSoup(respuesta.text,"html.parser")
        #Trabajo de scrapper
        #busqueda = soup.find_all("div",class_ = "tab-pane fade active in",id = "billetes")
        busqueda = soup.find_all("td")
        for indice in range (0,len(busqueda)):
            
            if "Dolar U.S.A" in str(busqueda[indice]):
                
                venta = busqueda[indice+1]
                compra = busqueda[indice+2]
                compra = str(compra).replace(",",".")
                venta = str(venta).replace(",",".")
                self.compra = compra[4:11]
                self.venta = venta[4:11]
            break
    
    def modificar_compra(self,nuevo_precio):
        self.compra = nuevo_precio
    
    def modificar_venta(self,nuevo_precio):
        self.venta = nuevo_precio

    