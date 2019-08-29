import urllib.request
import json

def parse_barreto(fisica):
    url = f'http://hpc.ct.utfpr.edu.br/~barreto/disciplinas/js/listas_fis{fisica}.js'

    with urllib.request.urlopen(url) as response:
        js = response.read()
        # print(js)

        ok = list(filter(lambda x: x.find('Problemas') != -1, js.decode('utf-8').replace('<b>', '\n').splitlines()))

        # ok = list(filter(lambda x: x.find('Problemas') != -1, js.decode('utf-8').splitlines()))

        # print(ok)
        kk = []

        for line in ok:
            kk.append(dict(cap=line[0:line.find('<br>')],exs=list(map(lambda x: int(x), line[line.find('</b>:') + 5:].replace(',', ' ')
                                                .replace(';', ' ')
                                                .replace('<br>', ' ')
                                                .replace('"', ' ').split()))))
            pass

        # print(kk)

        jurek = open('kk.json', 'w')
        json.dump(kk, jurek)

        # return kk

def recall_barreto():
    jurek = open('kk.json')
    kk = json.load(jurek)
    print(kk)

while True:
    print('q: quit')
    print('g: get data')
    print('p: print data')
    user = input()
    if user == 'q':
        exit(0)
    elif user == 'g':
        fis = input('numero da fisica: ')
        parse_barreto(fis)
    elif user == 'p':
        recall_barreto()
