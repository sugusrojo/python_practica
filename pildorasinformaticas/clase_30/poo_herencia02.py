class Vehiculos():
	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False


	def arrancar(self):

		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
    	self.cargado=cargar
    	if(self.cargado):
        	return "La furgoneta está cargada"
    	else:
        	return "La furgoneta NO está cargada"

class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


miMoto = Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))
