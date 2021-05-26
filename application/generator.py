class FunctionalityGenerator:
    def __init__(self, path, func1, func2):
        if path == 'default':
            text = self.generate_default_sentences()
        else:
            text = self.generate_custom_sentences()

        if func1 == 1:
            self.generate_first_functionality(text)

        if func2 == 1:
            self.generate_second_functionality(text)

    def generate_default_sentences(self):
        return "ok"

    def generate_custom_sentences(self):
        return "ok"

    def generate_first_functionality(self, text):
        pass

    def generate_second_functionality(self, text):
        pass


class InputGenerator:
    def __init__(self):
        pass