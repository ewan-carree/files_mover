# Permet de trier le dossier téléchargement - lancer en arrière plan avec & dans la ligne de commande

#http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/
#https://www.youtube.com/watch?v=R090APfdu58

import os
import time
import platform

repertoire = dict()

# Verifier OS pour faire tourner le programme
def detect_OS():
	global repertoire
	OS = platform.system()
	if OS == "Linux":
		repertoire = {"video": "/mnt/c/Users/carre/Videos", "picture": "/mnt/c/Users/carre/Pictures", "music": "/mnt/c/Users/carre/Music", "document" :"/mnt/c/Users/carre/Documents"}
		set_path("/mnt/c/Users/carre/Downloads")
	elif OS == "Windows":
		repertoire = {"video": "C:/Users/carre/Videos", "picture": "C:/Users/carre/Pictures", "music": "C:/Users/carre/Music", "document" :"C:/Users/carre/Documents"}
		set_path("C:/Users/carre/Downloads")
	else:
		print("This program isn't built to run on this OS")
		sys.exit(0)

def sort_files():
	files = os.listdir(get_path())
	for file in files:
		_, ext = os.path.splitext(file)
		if ext == ".pdf": 
			os.rename(get_path()+"/"+file, repertoire["document"]+"/"+file)
		if ext == ".txt": 
			os.rename(get_path()+"/"+file, repertoire["document"]+"/"+file)
		if ext == ".mp3": 
			os.rename(get_path()+"/"+file, repertoire["music"]+"/"+file)
		if ext == ".mp4": 
			os.rename(get_path()+"/"+file, repertoire["video"]+"/"+file)
		if ext == ".png": 
			os.rename(get_path()+"/"+file, repertoire["picture"]+"/"+file)
		if ext == ".jpg": 
			os.rename(get_path()+"/"+file, repertoire["picture"]+"/"+file)
		#possibilité de rajouter plusieurs autres extensions de fichiers


set_path = lambda fileName : os.chdir(fileName) #va dans le dossier de travail
get_path = lambda : os.getcwd() #répertoire actuel


def move():
	detect_OS()
	sort_files()


# ce qui suit ce if ne sera effectué qu'à partir de programme principal et non importé dans un autre programme
if __name__ == '__main__': 
	detect_OS()
	while True:
		sort_files()
		time.sleep(0.5)




