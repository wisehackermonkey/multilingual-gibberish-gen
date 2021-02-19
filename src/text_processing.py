"""
this code
project generates multilingual gibberish strings 
based on I.P.A. frequency distributions based on a
givin language

by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20210218
"""


import csv
import time
DATA_FILE_INPUT_PATH = "./src/data/en_US.txt"
DATA_FILE_OUTPUT_PATH = f"./src/output/results_eng_{time.time()}.txt"

with open(DATA_FILE_INPUT_PATH, encoding="utf-8") as raw_text_file:
    english_dictionary_reader = csv.reader(raw_text_file, delimiter='\t', quotechar='\'')
    results = ""
    with open(DATA_FILE_OUTPUT_PATH,mode="w",encoding="utf-8") as output_file:
        for i, defintion in enumerate(english_dictionary_reader):
            parsed = list(map(lambda a: (a.replace("/","")).replace("\'",""), defintion[1:]))
            print(parsed)
            output_file.write("".join(parsed))
            if i == 40:
                break
            
    
    