import nltk


def get_resources():
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')


def read_file():
    with open("text.txt", "r") as fin:
        text = fin.read()
    return text


def tokenize_text(text):
    text = nltk.word_tokenize(text)
    return text


def transform_text(text):
    return nltk.pos_tag(text)


if __name__ == '__main__':
    print(transform_text(tokenize_text(read_file())))
