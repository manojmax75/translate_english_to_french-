import pandas as pd
import time
import os, psutil

start_time = time.time()

with open("t8.shakespeare.txt") as f:
    with open("t8.shakespeare.translated.txt", "w") as f1:
        for line in f:
            f1.write(line) 

            
data = pd.read_csv (r'find_words.txt',header=None)
data.to_csv (r'New_Products.csv', index=None,header=None)

data.dropna(inplace = True)

data_dict = data.to_dict('dict')

import csv
reader = csv.reader(open('french_dictionary.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v



unique_words_english=[]
unique_words_french=[]
unique_words_frequency=[]

for i in range(1000):
  count_=data_dict[0][i]
  file = open("t8.shakespeare.txt", "r")
  data_ = file.read()
  occurrences = data_.count(count_)

  if occurrences>=1:
    unique_words_english.append(data_dict[0][i])
    unique_words_french.append(d[data_dict[0][i]])
    unique_words_frequency.append(occurrences)
  
  search_text=data_dict[0][i]
  replace_text=d[search_text]

  with open(r't8.shakespeare.translated.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

  with open(r't8.shakespeare.translated.txt', 'w') as file:
    file.write(data)

word_count = pd.DataFrame(
    {'English Word': unique_words_english,
     'French Word': unique_words_french,
     'Frequency': unique_words_frequency
    })

word_count.to_csv (r'frequency.csv')
process = psutil.Process(os.getpid())
print("Time: ", (time.time() - start_time))
print("Memory: ", process.memory_info().rss)