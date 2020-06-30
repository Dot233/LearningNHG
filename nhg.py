#!/usr/local/bin/python3
import json
import random
import sys

diff = 3
wordnum = 10
filepath = './config.myl'
kda = lambda x: x['right'] - (x['wrong'] * 2)

def choose(wordlist):
    if len(wordlist) <= wordnum:
        return wordlist
    chosen = []
    nums = 0
    while nums < wordnum:
        i = random.randint(0, len(wordlist) - 1)
        chosen.append(wordlist[i])
        del wordlist[i]
        nums += 1
    return chosen

def apply(wordlist, tolist):
    for x in wordlist:
        for y in tolist:
            if x['word'] == y['word']:
                y.update(x)

def taining(wordlist):
    for x in wordlist:
        if x['type'] == 'Kanji':
            ans = input('输入完整假名(' + x['word'] + '): ')
            if ans == x['Gana']:
                x['right'] += 1
                print('正确')
            else:
                x['wrong'] += 1
                print('错误,答案是:', x['Gana'])
        else:
            ans = input('输入完整假名(' + x['meaning'] + '): ')
            if ans == x['word']:
                x['right'] += 1
                print('正确')
            else:
                x['wrong'] += 1
                print('错误,答案是:', x['word'])

def floatin(worddata):
    f = open(filepath, 'w')
    f.write(json.dumps(worddata))
    f.close()

f = open(filepath, 'r')
data = json.loads(f.readline())
f.close()

words = []

if 'add' in sys.argv:
    print('请输入要添加词汇的信息:')
    type = input('类型(1:假名词汇,2:汉字词汇): ')
    if type != '1' and type != '2':
        exit()
    elif type == '2':
        word = input('单词: ')
        Gana = input('假名: ')
        data.append({'right' : 0, 'wrong' : 0, 'type' : 'Kanji', 'word' : word, 'Gana' : Gana})
    else:
        word = input('单词: ')
        meaning = input('解释: ')
        data.append({'right' : 0, 'wrong' : 0, 'type' : 'Gana', 'word' : word, 'meaning' : meaning})
else:
    for x in data:
        num = kda(x)
        if num <= diff:
            words.append(x)

    words.sort(key = kda)
    l = choose(words)
    taining(l)
    apply(l, data)
floatin(data)
