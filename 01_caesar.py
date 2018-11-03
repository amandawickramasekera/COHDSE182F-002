L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
text = input("Enter plain text	")

option = input("Enter e to encrypt or d to decrypt	")
if option == 'e':
	ci = ""
	for c in text.upper():
    		if c.isalpha(): ci += I2L[ (L2I[c] + key)%26 ]
    		else: ci += c
	print(ci)


elif option == 'd':
	pi = ""
	for c in text.upper():
    		if c.isalpha(): pi += I2L[ (L2I[c] - key)%26 ]
    		else: pi += c
	print (pi)
