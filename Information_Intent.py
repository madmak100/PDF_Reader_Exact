"""Example of training an additional entity type

This script shows how to add a new entity type to an existing pre-trained NER
model. To keep the example short and simple, only four sentences are provided
as examples. In practice, you'll need many more — a few hundred would be a
good start. You will also likely need to mix in examples of other entity
types, which might be obtained by running the entity recognizer over unlabelled
sentences, and adding their annotations to the training set.

The actual training is performed by looping over the examples, and calling
`nlp.entity.update()`. The `update()` method steps through the words of the
input. At each word, it makes a prediction. It then consults the annotations
provided on the GoldParse instance, to see whether it was right. If it was
wrong, it adjusts its weights so that the correct action will score higher
next time.

After training your model, you can save it to a directory. We recommend
wrapping models as Python packages, for ease of deployment.

For more details, see the documentation:
* Training: https://spacy.io/usage/training
* NER: https://spacy.io/usage/linguistic-features#named-entities

Compatible with: spaCy v2.0.0+
"""
from __future__ import unicode_literals, print_function
import plac
import random
from spacy.util import decaying
from spacy.util import compounding
from spacy.util import minibatch
from pathlib import Path
import spacy
from convertor import rasa_to_spacy_convertor

# new entity label


# training data
# Note: If you're using an existing model, make sure to mix in examples of
# other entity types that spaCy correctly recognized before. Otherwise, your
# model might learn the new type, but "forget" what it previously knew.
# https://explosion.ai/blog/pseudo-rehearsal-catastrophic-forgetting

def main(new_model_name, output_dir, n_iter,model=None):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')
    ner.add_label('Amt')
    ner.add_label('Inv_Num')
    ner.add_label('Urn_Num')
    ner.add_label('Invcis_Num')
    ner.add_label('Po_Num')
    ner.add_label('Mul_Po')
    ner.add_label('Mul_Urns')
    # ner.add_label('Cur_Head')
    # ner.add_label('URN_Head')
    # ner.add_label('Inv_Headings')
    # ner.add_label('Without_Heading')
    # ner.add_label('Table_Indicator')
    #ner.add_label('Inv_Date')
    #ner.add_label('PO_Num')
    #ner.add_label('Amount')
    #ner.add_label('Due_Date')
    #ner.add_label('Payment_Ref')
    #ner.add_label('Sup_Num')
    #ner.add_label('Received_Date')
    #ner.add_label('Doc_Id')
    #ner.add_label(LABEL4)# add new entity label to entity recognizer
    #ner.add_label(LABEL6)
    #ner.add_label(LABEL5)
    if model is None:
        optimizer = nlp.begin_training()
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()

    dropout = decaying(0.4, 0.2, 1e-4)

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER

        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = get_batches(TRAIN_DATA, 'ner')
            losses = {}
            for batch in batches:
            #for text, annotations in TRAIN_DATA:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=next(dropout),
                           losses=losses)
            print('Epoch : ', itn, 'loss: ', losses)

    # test the trained model
    test_text = """"""
    doc = nlp(test_text)
    #print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        #print(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)

def get_batches(train_data, model_type):

    max_batch_sizes = {'tagger': 32, 'parser': 16, 'ner': 16, 'textcat': 64}
    max_batch_size = max_batch_sizes[model_type]
    if len(train_data) < 1000:
        max_batch_size /= 2
    if len(train_data) < 500:
        max_batch_size /= 2
    batch_size = compounding(1, max_batch_size, 1.5)
    batches = minibatch(train_data, size=batch_size)
    # print(batches)

    return batches

if __name__ == '__main__':
    TRAIN_DATA = {}
    TRAIN_DATA = rasa_to_spacy_convertor(TRAIN_DATA)
    main('Monetary_model',"C:\\PyWork\\",50,None)