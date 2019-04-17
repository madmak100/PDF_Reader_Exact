import pandas as pd
import re
import nltk

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
df = pd.read_csv('',encoding="ISO-8859-1")
df_list = [sent for val in df.values.tolist() for j in val for sent in nltk.sent_tokenize(j)]
print(df_list)

final =[]
for i,line in enumerate(df_list):
    for word in nltk.pos_tag(nltk.word_tokenize(line.replace('\n',' \\n '))):
        final.append({'Sentence':i,'Word':word[0],'POS':word[1]})
dataframe = pd.DataFrame.from_dict(final)
print(dataframe)

