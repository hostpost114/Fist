import os 
files=os.listdir(r'.')
print(files)
for file in files :
	if 'apk' in file:
		#print(len(file)-3)
		print(file)
		strings='adb install -r '+"\""+file+"\""
		print(strings)
		os.system(strings)
		