# learn-a-language

Implement a system able to learn a grammar for a natural language.

## The system has two main functionalities:
- Accepts as input raw text and uses it to learn or update a grammar.
- Accepts as input raw text and checks if all sentences are parse-able by the available grammar.

## First functionality

Accepting as input raw text and using it to learn or update a grammar.

### First step: Add morpho-syntactic markups to that text. 
- Example output (NLTK):
- [('Today', 'NN'), ('morning', 'NN'), (',', ','), ('Arthur', 'NNP'), ('felt', 'VBD'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]


### Second step: Convert the markups to CLIPS or PROLOG facts 
- [('Today', 'NN'), ('morning', 'NN'), (',', ','), ('Arthur', 'NNP'), ('felt', 'VBD'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]

converted to (CLIPS): 

- (sentence NN NN , NNP VBD RB JJ .)

### Third step: learning or updating a grammar

Start with a set of rules (random or manual) for a grammar, for example one similar to homework 4 . 
Parse the input facts using that grammar and a parser (for example LR).
The facts not parsed are used to generate new grammar rules. For example, if a fact (sentence) starts with NN but no grammar rule has NN on the right side, a  new one is added left -> NN right where left and right are non-terminal symbols.
Repeat the above process until all input sentences are parsed.

## Second functionality

Accepts as input raw text and checks if all sentences are parse-able by the available grammar.

### First step: Add morpho-syntactic markups to that text. 

- Use any available annotator, for example https://nlp.stanford.edu/software/tagger.html (Java) or https://pythonexamples.org/nltk-pos-tagging/ (Python)

- Example output (NLTK):
- [('Today', 'NN'), ('morning', 'NN'), (',', ','), ('Arthur', 'NNP'), ('felt', 'VBD'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]

### Second step: Convert the markups to CLIPS or PROLOG facts   
- Example output:
- [('Today', 'NN'), ('morning', 'NN'), (',', ','), ('Arthur', 'NNP'), ('felt', 'VBD'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]

converted to (CLIPS): 

-(sentence NN NN , NNP VBD RB JJ .)

### Third step: parsing the input sentences
- If all input sentences are parsed by your grammar, output a confirming message. Otherwise output the sentences which are not parsed and the number of parsed sentences and total number of sentences.
