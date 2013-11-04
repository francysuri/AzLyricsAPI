import api.azapi
import sys

def query_yes_no(question, default="yes"):
	valid = {"yes":True,   "y":True,  "ye":True, "no":False,   "n":False}
	if default == None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "\
					"(or 'y' or 'n').\n")

def test():
	artist = raw_input("Insert artist: ")
	title = raw_input("Insert title: ")
	salvataggio = query_yes_no("Save lyrics in .txt file?")
	api.azapi.generating(artist, title, save=salvataggio)
	
	
if __name__ == '__main__':
	test()

