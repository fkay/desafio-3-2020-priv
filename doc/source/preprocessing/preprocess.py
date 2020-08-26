import json

texto = ''

path = 'E:\\dev\\MaratonaIBM\\desafio-3-2020\\doc\\source\\preprocessing\\'
arq = 'a_fascinante_fisica_do_dia_a_dia.json'

with open(path + arq, encoding='utf-8') as json_file:
    data = json.load(json_file)
    
    for p in data['paragraphs']:
        for c in p['cues']:
            texto += c['text']
    print(texto)

data = { 'texto': texto }

with open(path + 'p_' + arq , 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
