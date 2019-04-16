import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

def rasa_to_spacy_convertor(Outpu):
    Output = Outpu["rasa_nlu_data"]["common_examples"]
    copy = Output.copy()
    Output = []
    for out in copy:
        some_dict = {key: value for key, value in out.items() if key is not 'intent'}
        Output.append(some_dict)
    copy = Output.copy()
    Output = []
    for out in copy:
        trial = (out['text'],{'entities':[]})
        trial2 = []
        for tr in out['entities']:
            temp = (tr['start'],tr['end'],tr['entity'])
            trial2.append(temp)
        trial[1]['entities'] = trial2
        Output.append(trial)

    return Output