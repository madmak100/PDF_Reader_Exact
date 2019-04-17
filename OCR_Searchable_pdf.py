# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:12:10 2018

@author: sumanth.vaidya
"""

from subprocess import call
import os
import glob
import pytesseract
from PIL import Image
from PyPDF2 import PdfFileMerger
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


class Searchable_pdf_converter():
    
    def __init__(self,source_name,source_type,dest_type, source_path, destination_path, PDF_path=None):
        
        self.source_name = source_name
        self.source_type = source_type
        self.dest_type = dest_type
        self.source_path = source_path
        self.destination_path = destination_path
        self.PDF_path = PDF_path
        self.JPEG_path = None
        
    def convert_scannedpdf_to_jpg(self):
        
        input_path = self.source_path+self.source_name
        output_path = self.source_path+self.source_name[:self.source_name.rfind(self.dest_type)]
        os.makedirs(output_path)
        
        self.JPEG_path = output_path+os.sep+self.source_name+os.sep 
        print(self.JPEG_path)
        
        converter_path = r"C:\Program Files\Anaconda3\lib\site-packages\pdf2jpg\pdf2jpg.jar"
        
        output = call(['java', '-jar', converter_path,'-i', input_path, '-o', output_path,  '-p', 'ALL'])
        print(output)
    
    def convert_jpg_to_pdf(self):
        
        self.PDF_path = self.destination_path+self.source_name+os.sep
        os.makedirs(self.PDF_path)
        
        print(self.PDF_path)
        
        input_jpg_files = self.JPEG_path +'*'+ self.source_type
        
        page_no = 0
        files = glob.glob(input_jpg_files)
        print(files)
        
        for _ in files:
        
            jpeg_file_name = str(page_no)+'_'+self.source_name + self.source_type
            file_name = os.path.join(self.JPEG_path, jpeg_file_name)
            print(file_name)
            
            self.SaveResultToDocument(file_name,page_no)
            page_no = page_no + 1
        
    def OCR_extract(self,file_path,page_no):
        
        #size = 2550, 2750
        image = Image.open(file_path)
        #im_resized = image.resize(size, Image.ANTIALIAS)
        text = pytesseract.image_to_pdf_or_hocr(image,lang='eng')
        
        target_path = self.PDF_path+str(page_no) +'_'+ self.source_name + self.dest_type
        
        with open(target_path,'wb') as tmp_pdf:
            tmp_pdf.write(text)
        tmp_pdf.close()
            
    def execute_pdf_conversion(self):
        
        self.convert_scannedpdf_to_jpg()
        self.convert_jpg_to_pdf()
        self.merge_pdf()
        
    def execute_jpg_conversion(self):
        
        input_path = self.source_path+self.source_name
        self.OCR_extract(input_path,'Result')

    def SaveResultToDocument(self,file_path,page_no):
        
        self.OCR_extract(file_path,page_no)
        
    def merge_pdf(self):
        
        pdf_files = self.PDF_path +'*'+ self.dest_type
        page_no = 0
        
        files = glob.glob(pdf_files)        
        merger = PdfFileMerger()
        
        for pdf in files:
            
            pdf = str(page_no)+'_'+self.source_name + self.dest_type
            merger.append(open(self.PDF_path+pdf, 'rb'))
            page_no = page_no + 1
        
        with open(self.destination_path+'Result_'+self.source_name, 'wb') as fout:
            merger.write(fout)
            merger.close()
            
if __name__=="__main__":
    
    current_date_time = '2018-10-20 072757'
    source_name= current_date_time+'-'+'Amendment.pdf'
    print(source_name)

    
    converter = Searchable_pdf_converter(source_name = source_name)
    converter.convert_scannedpdf_to_jpg()
    converter.convert_jpg_to_pdf()
    converter.merge_pdf()
