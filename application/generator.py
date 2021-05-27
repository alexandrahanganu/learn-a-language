import spacy
from string import ascii_letters


class FunctionalityGenerator:
    def __init__(self, path, func1, func2, input, output):
        self.first = self.second = self.file_name = ""
        self.input = input
        self.output = output

        if path == 'default':
            self.file_name = "../metadata/default_grammar.txt"
        else:
            self.file_name = path

        if func1 == 1:
            self.first = self.generate_functionality('first')

        if func2 == 1:
            self.second = self.generate_functionality('second')

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r") as fin:
            text = fin.read()
        return text

    def tokenize_text(self, file_name):
        sp = spacy.load('en_core_web_sm')
        file = sp(self.read_file(file_name))
        return file

    @staticmethod
    def tag_text(file):
        pos = []
        tag = []
        exp = []
        for i in range(0, len(file)):
            pos.append(file[i].pos_)
            tag.append(file[i].tag_)
            exp.append(spacy.explain(file[i].tag_))
        return tag

    def generate_facts(self):
        self.facts = "(deffacts facts\n\t\t(waiting_input)\n\t\t(answer)\n\t\t"
        ruleIndex = 1
        phraseIndex = 1
        nonTerminalIndex = 1
        file = self.tokenize_text(self.file_name)
        tags = self.tag_text(file)
        for i in range(0, len(tags)):
            self.facts += "(rule G"
            self.facts += str(ruleIndex)
            self.facts += " "
            if i == 0:
                self.facts += "S"
            elif tags[i - 1] == "." and i - 1 >= 0:
                self.facts += "S"
                nonTerminalIndex = 1
            else:
                self.facts += ascii_letters[ascii_letters.index('A') + nonTerminalIndex - 2]
                self.facts += str(phraseIndex)
            self.facts += " "
            self.facts += tags[i]
            self.facts += " "
            if i < len(tags) - 1 and tags[i] == ".":
                self.facts += "S"
                self.facts += ")"
                self.facts += "\n\t\t"
                phraseIndex += 1
            elif i == len(tags) - 1:
                self.facts += "EPS"
                self.facts += ")"
            else:
                self.facts += ascii_letters[ascii_letters.index('A') + nonTerminalIndex - 1]
                self.facts += str(phraseIndex)
                self.facts += ")"
                self.facts += "\n\t\t"
            nonTerminalIndex += 1
            ruleIndex += 1
        self.facts += "\n)"

    def generate_functionality(self, number):
        self.generate_facts()
        with open(f"../metadata/{number}_functionality_template_part1.txt", "r") as fin:
            result = fin.read()
        result += '\n\n' + self.facts + '\n'
        with open(f"../metadata/{number}_functionality_template_part2.txt", "r") as fin:
            result += fin.read()
        result = result.replace("input_path", self.input)
        result = result.replace("output_path", self.output+f"/{number}_output.dat")
        return result

    def return_functionalities(self):
        return self.first, self.second


class InputGenerator:
    def __init__(self, text):
        self.text = text
        self.result = ""
        self.generate_tags()

    def tokenize_text(self):
        sp = spacy.load('en_core_web_sm')
        self.file = sp(self.text)

    def generate_tags(self):
        self.tokenize_text()

        pos = []
        tag = []
        exp = []

        for i in range(0, len(self.file)):
            pos.append(self.file[i].pos_)
            tag.append(self.file[i].tag_)
            exp.append(spacy.explain(self.file[i].tag_))

        self.result = " ".join(tag)


if __name__ == '__main__':
    f = FunctionalityGenerator('default', 1, 1)
    first, second = f.return_functionalities()
    print(first, second)
