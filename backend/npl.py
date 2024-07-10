import spacy

npl = spacy.load('en_core_web_sm')

def preprocess_text(text):
    doc = npl(text)
    entities[(entity.text, entity.lable_)]

text = "Set a reminder for my meeting at 3 PM"
print(preprocess_text(text))

