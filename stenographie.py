#!/usr/bin/python3

from PIL import Image
filename = ""
secret = ""
bin( ord( 'A' ) )[2:].rjust(8,'0') # donne : '01000001'
bin( ord( 'B' ) )[2:].rjust(8,'0') # donne : '01000010'
print("File : steganographie.py v0.1 starting \n Done by https://github.com/iS0Z ")
#Two functions -------------------------------------------
def imgwork(filename, secret):
	fileimg = Image.open(filename)
	fW , fH	= fileimg.size
	r, g, b = fileimg.split()
	r = list( r.getdata())
	secret_len = len(secret)
	secret_bin = bin(secret_len)[2:].rjust(8,"0")
	ascii = [ bin(ord(x))[2:].rjust(8,"0") for x in secret ]
	rc = ''.join(ascii)
	for j in range(8):
		r[j] = 2 * int( r[j] // 2 ) + int(secret_bin[j])
	for i in range(8*secret_len):
		r[i+8] = 2 * int( r[i+8] // 2 ) + int( rc[i] )
    #recreate img red 
	new_r = Image.new("L", (16, 16))
	new_r = Image.new("L",(fW,fH))
	new_r.putdata(r)
	imgnew = Image.merge('RGB', (new_r,g,b))
	new_filename = "s_" + filename
	imgnew.save(new_filename)

def get_secret(filename):
	im = Image.open(filename)
	r , g , b = im.split()
	r = list( r.getdata() )
	# lecture de la longueur de la chaine
	p = [ str(x%2) for x in r[0:8] ]
	q = "".join(p)
	q = int(q,2)

	# lecture du message
	n = [ str(x%2) for x in r[8:8*(q+1)] ]
	b = "".join(n)
	message = ""
	for k in range(0,q):
		l = b[8*k:8*k+8]
		message += chr(int(l,2))

	print("The secret is : " + message)

print("Use this script to add coded message in imgs\n")
print("Use images that max size is 600px*600px\n")
print("File will be saved as \"s_[filename]\" \n")
print("Choose an option\n")
print("1) Encode | 2) Decode \n")
choicemenu = input("Choice : ")
if choicemenu == 1 or choicemenu == "1":
	filemenu = input("Enter filename of image : ")
	secretmenu = input("Tell me what to hide : ")
	imgwork(filemenu, secretmenu)
elif choicemenu == "2" or choicemenu == 2:
	filename = input("Filename : ")
	get_secret(filename)
else: 
	print("erreur")
	exit()
