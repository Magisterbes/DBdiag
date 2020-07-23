import tqdm
import os
import sys
import pickle as pck
import json

dir = ""

def DumpToFile(val, filepath):
    with open(filepath, 'wb') as pickle_file:
        pck.dump(val, pickle_file)

def DumpToJson(val, filepath):
    with open(filepath, 'w') as pickle_file:
        json.dump(val, pickle_file)


def LoadFromFile(filepath):
    with open(filepath, 'rb') as pickle_file:
        data = pck.load(pickle_file)
    return data


def LoadFromFileJSON(filepath):
    with open(filepath, 'rb') as pickle_file:
        data = json.load(pickle_file)
    return data

def SaveStemmedSample(sample, fname):
    
    text_file = open(fname, "w")
    text_file.write("")
    text_file.close()

    text_file = open(fname, "a", encoding='utf8')
    for txt in sample:
        text_file.write(txt)
        text_file.write('\n________________\n')
    text_file.close()

def FillFromFile(fname):
    res = []
    strr = ""
    f = open(fname)
    for line in tqdm.tqdm(f):
        if "________________" in line:
            swords, stemmed,wordscount  = nlp.tokenize_and_stem(strr)
            ss = " ".join(list(map(lambda t: " ".join(t), stemmed)))
            if str.strip(ss) != "" and  len(ss)>100:
                res.append(ss)
            strr =""
        strr +=line
    f.close()
    return res

def FillFromFileNoStemm(fname):
    res = []
    strr = ""
    f = open(fname)
    for line in tqdm.tqdm(f):
        if "________________" in line:
            res.append(strr)
            strr =""
        strr +=line.strip()
    f.close()
    return res


def FillFromFileLines(fname):
    res = []
    strr = ""
    f = open(fname,encoding="utf-8",errors='ignore')
    for line in tqdm.tqdm(f):
        res.append(line.strip())

    f.close()
    return res

def LoadSemiColDel(fname):
    res = []
    strr = ""
    f = open(fname,encoding="utf-8",errors='ignore')
    for line in tqdm.tqdm(f):
        res.append(line.strip().split(";"))

    f.close()
    return res

def SaveJustLines(sample, fname, rewrite = False):

    if rewrite:
        text_file = open(fname, "w")
        text_file.write("")
        text_file.close()

    text_file = open(fname, "a")
    for txt in sample:
        try:
            text_file.write(str(txt))
            text_file.write('\n')
        except Exception:
            text_file.close()
            text_file = open(fname, "wb")
            text_file.write(txt.encode("utf-8","ignore"))
    text_file.close()


def GetFilesStartWith(dir, string):
    lst = os.listdir(dir)
    res= []
    for fname in lst:
        if fname.startswith(string):
            res.append(fname)

    return res



def GetDataStartWith(name):
    files = GetFilesStartWith(io.dir,name)

    res = []
    for fname in files:
        data = FillFromFileNoStemm(io.dir + fname)
        for txt in data:
            res.append(txt)
    return res
