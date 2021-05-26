import spacy


def read_file(file_name):
    with open(file_name, "r") as fin:
        text = fin.read()
    return text


def tokenize_text():
    sp = spacy.load('en_core_web_sm')
    file = sp(read_file("text.txt"))
    return file


def tag_text(file):
    pos = []
    tag = []
    exp = []
    for i in range(0, len(file)):
        pos.append(file[i].pos_)
        tag.append(file[i].tag_)
        exp.append(spacy.explain(file[i].tag_))
    return pos, tag, exp


if __name__ == '__main__':
    tokenize_text()
    print(tag_text(tokenize_text()))
