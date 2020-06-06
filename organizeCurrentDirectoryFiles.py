import shutil, os, time

def organizeCurrentDirectoryFilesByItsLastModificationYear():
	'''
	Clasifies all the files of the current directory by the year of its last modification,
	and then reorganizes each of them in subdirectories with the name of the year. 
	'''
	for file in os.listdir():

		if (file == 'main.py') or os.path.isdir(file):
			continue

		fileProps = os.stat(file)
		yearOfLastModification = time.gmtime(fileProps.st_mtime).tm_year

		try: 
			os.mkdir(f'./{str(yearOfLastModification)}')
		except FileExistsError:
			pass

		shutil.move(file, f'./{str(yearOfLastModification)}')


if __name__ == '__main__':
	answer = input("Press 'y' and enter if you are SURE of reorganizing ALL the files in the current directory.\n")
	if answer == 'y':
		organizeCurrentDirectoryFilesByItsLastModificationYear()
	
