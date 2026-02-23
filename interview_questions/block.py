# Given any input_word, return what the next word will be based on the probability of occurrences of words following the input_word in a training text ("corpus"). 

# Example corpus
import random


corpus = 'The sky is blue and this water is blue and the grass is green.'

# Example output
# Given this corpus, if we input "is" into the solution, the output should be "blue" approximately 2/3 of the time and "green" the other 1/3.

"""
Questions

 - Tokenization: spaces, or flexible
 - Capitalizaton / normalization: OK to normalize
 - Input cleaning: Can add if we have time, assume will be string. Special characters later
 - Limit vocabulary size
 - Vaguely follow SKLearn interface
 - If word not in corpus

Design

 - Helper functions
   - Tokenizer
   - Normalizer / cleaner
 - Fit
   - Data structure options:
     - Brute force is: [blue, blue, green]
     - More optimized: is: blue 2, green 1
   - Normalize, tokenize, create bigrams
   - For each bigram add to data structure
  - Predict
    - random.choices, weights
    - Normalize
    - Check provided key in data structure, and pull
    - Random.choices based on weights
    - Return selected
"""
# 1. Given any input_word, predict what the next word will be based on the occurrences of words following the input_word in the training text.

def tokenize(input_string):
    return input_string.split()


def clean_token(input_token):
    input_token = str(input_token).lower().replace('.', '')
    return input_token

class TokenPredictor(object):

    def __init__(self) -> None:
        self.learned_corpus = dict()

    def fit(self, corpus):
        tokens = tokenize(corpus)
        cleaned_tokens = list(map(clean_token, tokens))
        i = 0

        while i < len(cleaned_tokens) - 1:
            current = cleaned_tokens[i]
            if i == len(cleaned_tokens):
                next = None
            else:
                next = cleaned_tokens[i+1]

            if current in self.learned_corpus.keys():
                d = self.learned_corpus[current]
                d[next] = d.get(next, 0) + 1
                self.learned_corpus[current] = d
            else:
                d = {next: 1}
                self.learned_corpus[current] = d
            
            i += 1

        return self

    def predict(self, input_token):
        cleaned_token = clean_token(input_token)

        d = self.learned_corpus.get(cleaned_token, None)

        if d is None:
            return None
        return random.choices(list(d.keys()), weights = list(d.values()), k=1)[0]

    def generate_sentence(self, starting_word, sentence_length):
        generated_sentence = list()
        generated_sentence.append(clean_token(starting_word))

        for i in range(sentence_length):
            next_word  = self.predict(generated_sentence[-1])
            if next_word is None:
                break
            generated_sentence.append(next_word)
        print(generated_sentence)
        return ' '.join(generated_sentence)




tp = TokenPredictor()

tp.fit(corpus)

print(tp.learned_corpus)

for i in range(5):
    print(tp.predict('is'))

# 2. Now use this to generate a sentence given a starting word and a sentence length.

corpus = 'The sky is blue and the sun shines bright. This tree is green and clear. The sun is bright, and the tree looks green. Blue sky and bright sun. The sky is clear, and this tree is green. The sun shines and the sky is blue. This tree looks green and the sun is bright. Clear sky and green tree. The sky is blue, the sun shines bright, and the tree is green. This green tree looks bright under the clear sky.'
tp2 = TokenPredictor()

tp2.fit(corpus)
tp2.generate_sentence('the', 10)