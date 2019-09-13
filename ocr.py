import os
import shutil

folder_names = os.listdir("./Data/")
ocr_main = "./" # Source to ocr++ main without / at end

i = 0
for folder in folder_names:
	print("Starting "+folder)
	files = os.listdir("./Data/"+folder)

	for file in files:
		shutil.copy("./Data/"+folder+"/"+file, ocr_main+"/input/"+file)

	print("Copied "+len(files)+"\tRunning script on "+folder)
	os.system("python3 "+ocr_main+"main_script_batch.py")

	os.mkdir("./OCR/"+folder)
	shutil.copytree(ocr_main+"/output", "./OCR/"+folder)

	print("Output copied")
	shutil.rmtree(ocr_main+"/output")
	shutil.rmtree(ocr_main+"/input")

	i = i + 1
	print(i),

