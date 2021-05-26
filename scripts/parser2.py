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
        pos.append(file[i].pos_)
        tag.append(file[i].tag_)
        exp.append(spacy.explain(file[i].tag_))
    return tag


def singularFacts():
    facts = "(deffacts facts\n\t\t(waiting_input)\n\t\t(answer)\n\t\t"
    index = 1
    phraseIndex = 1
    for i in range(0, len(tags)):
        facts += "(rule G"
        facts += str(index)
        facts += " "
        if (i == 0):
            facts += "S"
        else:
            facts += ascii_letters[ascii_letters.index('A') + index - 2]
            facts += str(phraseIndex)
        facts += " "
        facts += tags[i]
        facts += " "
        if (i < len(tags) - 1):
            facts += ascii_letters[ascii_letters.index('A') + index - 1]
            facts += str(phraseIndex)
            facts += ")"
            facts += "\n\t\t"
        else:
            facts += "EPS"
            facts += ")"
        index += 1
    facts += "\n)"
    return facts


def multipleFacts():
    facts = "(deffacts facts\n\t\t(waiting_input)\n\t\t(answer)\n\t\t"
    ruleIndex = 1
    phraseIndex = 1
    nonTerminalIndex = 1
    for i in range(0, len(tags)):
        facts += "(rule G"
        facts += str(ruleIndex)
        facts += " "
        if (i == 0):
            facts += "S"
            print(" primul if ")
        elif tags[i-1] == "." and i-1>=0:
            facts += "S"
            nonTerminalIndex = 1
            print(" primul elif ")
        else:
            facts += ascii_letters[ascii_letters.index('A') + nonTerminalIndex - 2]
            facts += str(phraseIndex)
            print(" primul else ")
        facts += " "
        facts += tags[i]
        facts += " "
        if i < len(tags) - 1 and tags[i] == ".":
            facts += "S"
            facts += ")"
            facts += "\n\t\t"
            phraseIndex += 1
            print(" al doilea if ")
        elif i == len(tags) - 1:
            facts += "EPS"
            facts += ")"
            print(" al doilea elif ")
        else:
            facts += ascii_letters[ascii_letters.index('A') + nonTerminalIndex - 1]
            facts += str(phraseIndex)
            facts += ")"
            facts += "\n\t\t"
            print(" al doilea else ")
        nonTerminalIndex += 1
        ruleIndex += 1
    facts += "\n)"
    return facts


from string import ascii_letters
if __name__ == '__main__':
    text = input("Introduceti textul:")
    file = tokenize_text(text)
    tags = tag_text(file)
    print("tagurile propozitiei", tags)
    some_text = read_file("C:/Users/Theo/PycharmProjects/Pbr Project/help/aux_file.txt") #path-ul fisierului aux_file (e in folderul help)
    #singularFacts = singularFacts()
    #print(singularFacts)
    multipleFacts = multipleFacts()
    print(multipleFacts)
    #os.system(r'"D:/CLIPS/CLIPSWin.exe"') #aici path-ul catre clips
    #print(some_text)



    # intreaba la inceput cate propozitii vrea sa citeasca
    # daca una, atunci o sa citeasca dintr-un anumit fisier cu reguli singulare
    # daca mai multe din celalalt
    #     	(rule G9  B2 . EPS)
    #       (rule G6  E1 . EPS)
