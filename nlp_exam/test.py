import nltk
from nltk.tokenize import word_tokenize
py_txt = word_tokenize ("Example of nltk pos tag.")
res = nltk.pos_tag (py_txt)
print(py_txt)
print(res)

