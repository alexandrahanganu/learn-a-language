# learn-a-language

Implement a system able to learn a grammar for a natural language.

## The system has two main functionalities:
- Accepts as input raw text and uses it to learn or update a grammar.
- Accepts as input raw text and checks if all sentences are parse-able by the available grammar.

## First step: Add morpho-syntactic markups to that text. 
- Example output (NLTK):


## Second step: Convert the markups to CLIPS or PROLOG facts 
- [('Today', 'NN'), ('morning', 'NN'), (',', ','), ('Arthur', 'NNP'), ('felt', 'VBD'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]

converted to (CLIPS): =>

- (sentence NN NN , NNP VBD RB JJ .)
