import json
import sys
from collections import Counter

import spacy

nlp = spacy.load("en_core_web_md")

with open(sys.argv[1]) as file:
    book = file.read()

words = Counter()
word_count, token_count = 0, 0

doc = nlp(book)

for token in doc:
    token_count += 1
    if not token.is_alpha:
        continue
    word_count += 1
    words[token.lemma_.lower()] += 1

words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}

print("Done processing 👍")
print(f"token count: {token_count}, word count: {word_count}")
print(f"unique words approximation: {len(words)}")

with open("output.json", "w") as file:
    json.dump(words, file, indent=2, ensure_ascii=False)
