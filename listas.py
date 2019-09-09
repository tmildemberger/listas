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
                                                .replace('"', ' ').split())),
                           feitos=[]))
            pass

        # print(kk)

        jurek = open('kk.json', 'w')
        json.dump(kk, jurek)

        # return kk

def recall_barreto():
    jurek = open('kk.json')
    kk = json.load(jurek)
    print(kk)

fisica = 2
import os
data = dict()
if os.path.exists('data.json'):
    aa = open('data.json')
    data = json.load(aa)

while True:
    print('q: quit')
    print('g: get data')
    print('p: print data')
    print('e: exercise')
    user = input()
    if user == 'q':
        jurek = open('data.json', 'w')
        json.dump(data, jurek)
        exit(0)
    elif user == 'g':
        fis = input('numero da fisica: ')
        parse_barreto(fis)
        jurek = open('kk.json')
        data = json.load(jurek)
    elif user == 'p':
        recall_barreto()
    elif user == 'e':
        while True:
            aaa = list(a for a in data)
            for i, c in enumerate(list(a['cap'] for a in aaa)):
                print(f'{i + 1}: {c}')
            user = int(input()) - 1
            if user < 0 or user >= len(aaa):
                break
            print('-----------')
            print('-----------')
            print('-----------')
            print('-----------')
            print(aaa[user]['cap'])
            print('-----------')
            print(aaa[user])
            print('-----------')
            afazer = list(k for k in aaa[user]['exs'] if k not in aaa[user]['feitos'])
            print(afazer)
            import random
            ye = random.choice(afazer)
            print(f'faça o ex {ye}')
            print('-----------')
            yn = input(f'fez o ex {ye}? ')
            if yn not in ['0', 'n', 'N']:
                aaa[user]['feitos'].append(ye)


