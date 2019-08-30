import os
import pandas as pd
import numpy as np
import requests

# files = os.listdir('./Links/')
# files.sort()
# print(files)

# for name in files[:1]:
# 	df = pd.read_csv('./Links/'+name)


journals = pd.read_csv('./Journal Names.csv')
print(journals.shape)

os.chdir('Data')

for i in range(journals.shape[0]//300):
	df = pd.read_csv('../Links/'+journals['Title'][i]+'.csv')

	folder = journals['Title'][i]
	try:
		os.mkdir(folder)
	except:
		print(df)
		
	os.chdir(folder)
	print(os.getcwd())

	for j in range(df.shape[0]):

		url = df['Link'][j]
		os.system('wget '+url)

	
"""
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
  
r = requests.get(file_url, stream = True) 
  
with open("python.pdf","wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
  
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk) 
"""	