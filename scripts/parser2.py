import spacy
def read_file(file_name):
    with open(file_name, "r") as fin:
        text = fin.read()
    return text


def tokenize_text(text):
    sp = spacy.load('en_core_web_sm')
    file = sp(text)
    return file


def tag_text(file):
    pos = []
    tag = []
    exp = []
    for i in range(0, len(file)):
        #print(file[i].pos_)
        pos.append(file[i].pos_)
        tag.append(file[i].tag_)
        exp.append(spacy.explain(file[i].tag_))
    return tag


import os
if __name__ == '__main__':
    text = input("Introduceti textul:")
    file = tokenize_text(text)
    tags = tag_text(file)
    #tokenize_text()
    #print(tag_text(tokenize_text()))
    print("tagurile propozitiei", tags)
    os.system(r'"D:/CLIPS/CLIPSWin.exe"') #aici aveti clips-ul instalat
    some_text = read_file("C:/Users/Theo/PycharmProjects/Pbr Project/help/aux_file.txt") #path-ul fisierului aux_file (e in folderul help)
    print(some_text)
    # intreaba la inceput cate propozitii vrea sa citeasca
    # daca una, atunci o sa citeasca dintr-un anumit fisier cu reguli singulare
    # daca mai multe din celalalt
    #     	(rule G9  B2 . EPS)
    #       (rule G6  E1 . EPS)