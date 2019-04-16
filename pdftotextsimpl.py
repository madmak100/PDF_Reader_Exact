from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage,PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import LAParams , LTTextBox
from pdfminer.converter import PDFPageAggregator
import spacy
from fuzzywuzzy import fuzz


import pdfminer


nlp2 = spacy.load(spacy_path)
# Open a PDF file.
fp = open(path, 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser, '')
# outlines = document.get_outlines()
# for (level,title,dest,a,se) in outlines:
#     print (level, title)


if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
text =  ''
text_from_pdf = open('textFromPdf.txt','w')
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBox):
            text = text+''.join([i if ord(i) < 128 else ' '
                                            for i in element.get_text()])
print(text)

doc = nlp2(text.replace('\n',' '))

for ent in doc.ents:
    print(ent.text,ent.label_)
