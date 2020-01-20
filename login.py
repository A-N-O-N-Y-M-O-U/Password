user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'MAIN IT' and user == 'ABELLARD':

	print "Kamu Berhasil Login"
	
else:

	print "Username atau Password Salah !"