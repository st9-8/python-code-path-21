
class Crypto:
	"""Cryptage utilisant le chiffrement de césar
	ch = chaine, d = décalage"""
	def __init__(self, ch, d):
		self.ch, self.d = ch, d
		#On initialise les dictionnaires. cryptage pour crypter, decryptage pour décrypter
		self.cryptage = {}
		self.decryptage = {}
		
		#On construit les listes. alpha = alphabet normal. ald = alphabet avec le décalage
		self.alpha = [chr(x) for x in range(97, 123)]
		self.ald = [self.alpha[(i+self.d)%26] for i in range(26)] #Utilisation du modulo pour éviter le OutOfRange
		#Construction de cryptage
		for x in range(26):
			self.cryptage[self.alpha[x]] = self.ald[x]
		
	def inverser_dico(self):
		"""Construction du dictionnaire decryptage en inversant la valeur de cryptage afin d'accéder à la traduction"""
		for (k, v) in self.cryptage.items():
			self.decryptage[v] = k
		return self.decryptage

	def code(self, p):
		"""Coder et décoder le texte"""
		self.new_ch = []
		self.inverser_dico()
		for car in self.ch:
			if car is ' ':
				self.new_ch.append(' ')
			else:
				if p is True:
					self.new_ch.append(self.cryptage[car])
				else: 
					self.new_ch.append(self.decryptage[car])

		return self.new_ch
y = "y"
if __name__ == "__main__":
	while y:
		chx = input("Entrez C pour crypter ou D décrypter votre texte : ")
		if chx.upper() == 'C':
			x = True
		elif chx.upper() == 'D':
			x = None
		else:
			print ("Mauvais choix !")
			break
		
		decalage = input("De combien de lettres voulez vous décaler votre code : ")
		if decalage.isdigit():
			txt = input("Veuillez entrer votre texte :\n")
			a = Crypto(txt.lower(), int(decalage))
		else:
			print ("Vous devez entrer un nombre !")
			break
		
		try:
			a.code(x)
			print (''.join(a.code(x)))
		except:
			print ("Vous ne devez rentrer uniquement des lettres !")
			break
				
		r = input("Autre texte à crypter ? ( y: Oui, Entrée: Non ) : ")
		if r == 'y':
			continue
		else:
			break
