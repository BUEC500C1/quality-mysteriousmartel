# Copyright 2020 by Jennifer Campbell

def stringConvert(inputVal):
	numberStr = str(inputVal)
	return numberStr

def errorCheck(inputVal):
	numString = stringConvert(inputVal)
	if (numString.isdigit() == True):
		return True
	else:
		print("Invalid input")
		return False


def whatHaveTheRomans(piggies):
	Romani = {1: 'I', 5: 'V', 10: 'X', 50: 'L', \
	100: 'C', 500: 'D', 1000: 'M'}
	Romanes = errorCheck(piggies)
	Domum = []
	if (Romanes == True):
		Eunt = int(stringConvert(piggies))
		while Eunt > 0:
			if Eunt > 4000:
				Domum.append(Romani[1000])
				Eunt -= 1000
			else:
				if ((Eunt - 900) < 100 and (Eunt - 900) >= 0):
					Domum.append(Romani[100])
					Domum.append(Romani[1000])
					Eunt -= 900
				elif ((Eunt - 400) < 100 and (Eunt - 400) >= 0):
					Domum.append(Romani[100])
					Domum.append(Romani[500])
					Eunt -= 400
				elif ((Eunt - 90) < 10 and (Eunt - 90) >= 0):
					Domum.append(Romani[10])
					Domum.append(Romani[100])
					Eunt -= 90
				elif ((Eunt - 40) < 10 and (Eunt - 40) >= 0):
					Domum.append(Romani[10])
					Domum.append(Romani[50])
					Eunt -= 40
				elif ((Eunt - 9) < 1 and (Eunt - 9) >= 0):
					Domum.append(Romani[1])
					Domum.append(Romani[10])
					Eunt -= 9
				elif ((Eunt - 4) < 1 and (Eunt - 4) >= 0):
					Domum.append(Romani[1])
					Domum.append(Romani[5])
					Eunt -= 4
				else:
					Ite = max(key for key in Romani if key <= Eunt)
					Domum.append(Romani[Ite])
					Eunt -= Ite
		return ''.join(Domum)
	else:
		return Romanes

if __name__ == '__main__':

	testerVal = '10*2'
	testerTwo = 10.1

	print(whatHaveTheRomans(testerVal))
	print(whatHaveTheRomans(testerTwo))