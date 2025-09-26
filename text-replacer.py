import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

modified_words = []

for word, tag in tagged_words:
    if tag in ['NN','NNS','NNP','NNPS']:
        modified_words.append("AI")
    else:
        modified_words.append(word)


modified_sentence = " ".join(modified_words)

print("\nOriginal Sentence:",sentence)
print("\nModified Sentence:",modified_sentence)