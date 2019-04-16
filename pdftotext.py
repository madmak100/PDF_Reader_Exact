from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer

fp = open('', 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Password for initialization as 2nd parameter
document = PDFDocument(parser)

# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Create a PDF device object.
# device = PDFDevice(rsrcmgr)

# BEGIN LAYOUT ANALYSIS
# Set parameters for analysis.
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)



def parse_obj(lt_objs):
    data_string = ''
    sub_tit = ''
    new_txt = ''
    # loop over the object list
    for obj in lt_objs:
        # if it's a textbox, print text and location

        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            #print(obj)
            #obj.get_text().split('\n')


            if obj.get_text().isupper():
                if sub_tit is '':
                    data_string += "{0} {1}".format(sub_tit,obj.get_text())


                    sub_tit = ''
                else:
                    z = sub_tit.split('\n')
                    data_string += "{0} {1}".format(z[0],obj.get_text())


                    sub_tit = ''

            elif len(obj.get_text()) > 10 and obj.get_text()[0].isupper():
                out = obj.get_text().split(' ')
                if out[0].isupper() and out[1].isupper() and out[2].isupper():

                    if sub_tit is '':

                        new_str = ' '.join(out)
                        data_string += "{0}".format(new_str)

                    else:
                        z = sub_tit.split('\n')
                        new_str = ' '.join(out)
                        data_string += "{0} {1}".format(z[0],new_str)

                        sub_tit = ''

                elif out[0].isupper() and out[1].isupper():
                    if sub_tit is '':
                        new_str = ' '.join(out)
                        data_string += " {0}".format(new_str)
                    else:
                        z = sub_tit.split('\n')
                        new_str = ' '.join(out)
                        data_string += " {0} {1}".format(z[0],new_str)

                        sub_tit = ''

                elif out[0].isupper():
                    if sub_tit is '':

                        new_str = ' '.join(out)
                        data_string += "{0}".format(new_str)

                    else:
                        z = sub_tit.split('\n')
                        new_str = ' '.join(out)
                        data_string += "{0} {1}".format(z[0],new_str)

                        sub_tit = ''

                else:
                    if sub_tit is '':
                        data_string += "{0}".format(obj.get_text())
                    elif len(sub_tit) <= 10:
                        z = sub_tit.split('\n')
                        data_string += "{0} {1}".format(z[0],obj.get_text())
                        sub_tit = ''
                    else:
                        z = sub_tit.split('\n')
                        data_string += "{0} {1}".format(z[0],obj.get_text())

                        sub_tit = ''
            elif len(obj.get_text()) < 30:
                #print(len(obj.get_text()),obj.get_text())
                sub_tit += obj.get_text()

            else:
                if len(obj.get_text()) > 100:
                    if sub_tit is '':
                        data_string += "{0}".format(obj.get_text())
                    else:
                        z = sub_tit.split('\n')
                        data_string += "{0} {1}".format(z[0],obj.get_text())

                else:
                    if sub_tit is '':

                        data_string += "{0}".format(obj.get_text())
                    else:
                        z = sub_tit.split('\n')
                        data_string += "{0} {1}".format(z[0],obj.get_text())
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs)
    return data_string

for page in PDFPage.create_pages(document):
    # read the page into a layout object

    interpreter.process_page(page)

    layout = device.get_result()

    print(parse_obj(layout))

