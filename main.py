import requests, os, zipfile
import csv
from io import BytesIO

os.makedirs('./data', exist_ok=True)

url = 'https://datawarehouse-true.s3-sa-east-1.amazonaws.com/teste-true/teste_true_term.zip'

file_zip = BytesIO(requests.get(url).content)

zip = zipfile.ZipFile(file_zip)
zip.extractall('./data')

new_line = []

with open('./data/encad-termicas.csv') as csv_file:
    with open('./data/TERM.DAT', 'r') as term:
        csv_reader = csv.reader(csv_file, delimiter=',')
        term = term.readlines()
        max_line = len(term)
        for row_csv in csv_reader:
            for x in range(max_line):
                term_line_string = term[x]
                term_list_string = term_line_string.split()
                if term_list_string[0] == row_csv[0]:
                    for indice in range(len(row_csv)):
                        if term_list_string[0] == 140:
                            if term_list_string[indice] == 'MAUA':
                                new_line.append(row_csv[indice])
                        elif term_list_string[indice] != row_csv[indice]:
                            new_line.append(row_csv[indice])
                        else:
                            new_line.append(term_list_string[indice])
                    new_line.append('\n')
                    term[x] = "  ".join(new_line)
                    new_line.clear()
        print(term)
        print(" ".join(term))
        new_term = open('./data/TERM.DAT', 'w')
        new_term.write(" ".join(term))
