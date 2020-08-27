import json
from os import listdir
from os.path import isfile, join

path = 'E:\\dev\\MaratonaIBM\\desafio-3-2020\\doc\\source\\preprocessing\\'

onlyfiles = [f for f in listdir(path) if (isfile(join(path, f)) & ("json" in f))]

#arq = 'a_fascinante_fisica_do_dia_a_dia.json'

for arq in onlyfiles:
    texto = ''
    with open(path + arq, encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        for p in data['paragraphs']:
            for c in p['cues']:
                texto += c['text'] + ' '
        #print(texto)

    data = { 
            'title': arq,
            "author": "none",
            'body': texto,
            "type": "video",
            "url": "http://" 
            }

    with open(path + 'processed\\' + arq , 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
        print("Arquivo salvo: " + arq)
