import requests, os, zipfile
import csv
from io import BytesIO

os.makedirs('./data', exist_ok=True)

url = 'https://datawarehouse-true.s3-sa-east-1.amazonaws.com/teste-true/teste_true_term.zip'

file_zip = BytesIO(requests.get(url).content)

zip = zipfile.ZipFile(file_zip)
zip.extractall('./data')
