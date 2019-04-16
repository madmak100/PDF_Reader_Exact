import spacy
import re
import json
from Trial_new import check
import traceback
import pandas as pd
import dateutil.parser as dparser
from date_extractor import extract_dates
from date_extractor import getFirstDateFromText

headings_dir = "C:\\PyWork\\Trial_Program"
lc_dir = "C:\\PyWork\\Trial_2"
tc_dir = "C:\\PyWork\\Tenant_Company"
ll_dir = "C:\\PyWork\\Landlord_Company"
pb_dir = "C:\\PyWork\\OI_V2"#Except_Name_n_Address"
area_dir = "C:\\PyWork\\Area_Extractor"
monetary_dir = "C:\\PyWork\\Monetary_Find_V2"
lc_int_rate_dir = "C:\\PyWork\\LC_INT_RATE"
tar_dir = "C:\\PyWork\\POAR_Extract"
holdover_dir = "C:\\PyWork\\Holdover"
insurace_dir = "C:\\PyWork\\Insurance"
tna_dir = "C:\\PyWork\\TENANT'S_NOTICE_ADDRESS"
exhibit_dir = "C:\\PyWork\\Exhibit"

nlp = spacy.load(headings_dir)
nlp1 = spacy.load(tna_dir)
nlp2 = spacy.load(lc_dir)
nlp3 = spacy.load(tc_dir)
nlp4 = spacy.load(ll_dir)
nlp5 = spacy.load(pb_dir)
nlp6 = spacy.load(area_dir)
nlp9 = spacy.load(monetary_dir)
nlp10 = spacy.load(lc_int_rate_dir)
nlp11 = spacy.load(tar_dir)
nlp12 = spacy.load(holdover_dir)
nlp13 = spacy.load(insurace_dir)
nlp14 = spacy.load(exhibit_dir)

class Lease_Data_Extractor(object):

    def __init__(self):

        self.test_text = None
        self.headings_list = []
        self.opportunity_list =[]
        self.exhibits_list = []
        self.copy = None
        self.first_section = None
        self.Function_List = []
        self.OP_List = []
        self.EX_List = []
        self.Ist_Page_Info_List = []
        self.tempo = None
        self.dataframe = None

    def load_pdf(self):
        self.test_text = check().text_json1
        self.test_text = re.sub(r"(.*)INTENTIONALLY OMITTED.","",self.test_text)
        self.test_text = re.sub(r"(.*)INTENTIONALLY OMITTED","",self.test_text)

    def headings_extractor(self):

        doc = nlp(self.test_text)
        for ent in doc.ents:
            print(ent.label_, ent.text)
            self.headings_list.append(ent.text)
        self.copy = re.sub('\n',' ',self.test_text)

    def first_section_extractor(self):
        self.frst_section = re.sub(self.headings_list[2],'',re.search('{0}(.*){1}'.format(self.headings_list[1],self.headings_list[2]), self.copy).group())

    def commencement_date_extractor(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                  "December"]
        trial = {}
        commencement_date = ""
        try:
            for month in months:
                commencement_date = re.search(r'{0}(.*)\d'.format(month),self.frst_section)
                if commencement_date:
                    trial = {'Field_Name': 'Commencement_Date',
                             'Start_Index': self.copy.index(commencement_date.group())
                        , 'End_Index': len(commencement_date.group())+ self.copy.index(commencement_date.group()),
                             'Text': commencement_date.group(),'Value': ''}
                    trial['Value'] = str(getFirstDateFromText(commencement_date.group()))
                    self.opportunity_list.append(trial)
                    break
        except:
            pass
    # cmp_ll = nlp4(frst_section)
    # for ent in cmp_ll.ents:
    #     print(ent.label_, ent.text)
    #     try:
    #         start_index = copy.index(ent.text)
    #         end_index = start_index+len(ent.text)
    #         trial_1 = {'Field_Name' : ent.label_,'Start_Index': start_index, 'End_Index': end_index,'Text':ent.text,'Value':ent.text}
    #     except:
    #         trial_1 = {}
    #     opportunity_list.append(trial_1)

    def tenant_address_extractor(self):
        tnt_adrs = nlp1(self.frst_section)
        trial1 = {}
        for ent in tnt_adrs.ents:
            #print(ent.label_, ent.text)
            try:
                start_index = self.copy.index(ent.text)
                end_index = start_index+len(ent.text)
                value = re.split(r'\d\. ',self.copy[start_index:end_index])[1]
                value = re.split(r'after the Commencement Date:|After the Commencement Date:',value)[1]
                trial1 = {'Field_Name' : ent.label_,'Start_Index': start_index, 'End_Index': end_index,'Text':
                    self.test_text[start_index:end_index],'Value':value}
                self.opportunity_list.append(trial1)
                try :
                    value = re.split(r'Attention:|Attn:',value)[1]
                    trial2 = {'Field_Name': 'Attention/Contact Name', 'Start_Index': start_index, 'End_Index': end_index,
                           'Text': self.test_text[start_index:end_index], 'Value': value}
                    self.opportunity_list.append(trial2)
                except :
                    pass
            except:
                pass

    def tenant_company_extractor(self):
        cmp_tnt = nlp3(self.frst_section)
        for ent in cmp_tnt.ents:
            #print(ent.label_, ent.text)
            try:
                start_index = self.copy.index(ent.text)
                end_index = start_index+len(ent.text)
                trial = {'Field_Name' : ent.label_,'Start_Index': start_index, 'End_Index': end_index,'Text':
                    self.test_text[start_index:end_index],'Value':self.test_text[start_index:end_index]}
                self.opportunity_list.append(trial)
            except:
                pass

    def premise_building_area_extractor(self):
        prms_bld = nlp5(self.frst_section)
        trial = {}
        for ent in prms_bld.ents:
            #print(ent.label_, ent.text)
            if ent.label_ == "Commencement_Date":
                continue
            try:
                start_index = self.copy.index(ent.text)
                end_index = start_index+len(ent.text)
                trial = {'Field_Name' : ent.label_,'Start_Index': start_index, 'End_Index': end_index,
                           'Text':self.test_text[start_index:end_index],'Value':''}
            except:
                trial = {}
            area = nlp6(ent.text)
            tmp = ''
            for enty in area.ents:
                #print(enty.label_, enty.text)
                strt_idx = self.copy.index(enty.text)
                end_idx = strt_idx + len(enty.text)
                tmp = self.test_text[strt_idx:end_idx]
            if tmp == '':
                tmp = ent.text
            trial['Value'] = tmp
            self.opportunity_list.append(trial)

    def cam_security_deposit_extractor(self):
        mont_value = nlp9(self.frst_section)
        for ent in mont_value.ents:
            print(ent.label_, ent.text)
            try:
                start_index = self.copy.index(ent.text)
                end_index = start_index+len(ent.text)
                trial = {'Field_Name' : ent.label_,'Start_Index': start_index, 'End_Index': end_index,
                           'Text':self.test_text[start_index:end_index],'Value':self.test_text[start_index:end_index]}
                self.opportunity_list.append(trial)
            except:
                pass
            
    def cam_incl_excl_and_recdue_extractor(self,text):
        documen = nlp11(self.tempo)
        for ento in documen.ents:
            if not ento.label_ in text:
                continue
            strt_idx = self.copy.index(ento.text)
            end_idx = strt_idx + len(ento.text)
            trial = {'Field_Name': ento.label_, 'Start_Index': strt_idx, 'End_Index': end_idx, 'Text': self.tempo,
                     'Value': self.test_text[strt_idx:end_idx]}
            self.opportunity_list.append(trial)

    def tenant_audit_rights_extractor(self):
        phrases = ["For a period of one", "Upon Tenant's written request"]
        try:
            for phrase in phrases:
                tenant_audit_rights = re.search(r'{0}(.*)\([a-z]\)|{0}(.*)'.format(phrase), self.tempo)
                text = re.search(r'{0}(.*)\([a-z]\)|{0}(.*)'.format("Payment of Additional Rent"), self.tempo)
                text = text.group()
                if tenant_audit_rights:
                    trial = {'Field_Name': 'TENANT_AUDIT_RIGHTS',
                             'Start_Index': self.copy.index(text), 'End_Index':
                                 len(text) + self.copy.index(text),
                             'Text': text,
                             'Value': tenant_audit_rights.group()}
                    self.opportunity_list.append(trial)
                    break
        except:
            pass

    def management_fee_extractor(self):
        mangmnt_fee = re.search(r'{0}(.*)\([a-z]\) Payment|{0}(.*)'.format("Common Area Maintenance"), self.tempo)
        try:
            if mangmnt_fee:
                trial = {'Field_Name': 'MANAGEMENT_FEE_NOTES',
                         'Start_Index': self.copy.index(self.tempo), 'End_Index':
                             len(self.tempo) + self.copy.index(self.tempo),
                         'Text': self.tempo,
                         'Value': mangmnt_fee.group()}
                self.opportunity_list.append(trial)
        except:
            pass

    def amcap_extractor(self):
        amcap = re.search(r'{0}(.*)\([a-z]\) Payment|{0}(.*)'.format("Additional Rent."), self.tempo)
        try:
            if amcap:
                trial_2 = {'Field_Name': 'AMORTIZED_CAP_RECOVERY_PART1',
                           'Start_Index': self.copy.index(self.tempo), 'End_Index':
                               len(self.tempo) + self.copy.index(self.tempo),
                           'Text': self.tempo,
                           'Value': amcap.group()}
                self.opportunity_list.append(trial_2)
        except:
            pass

    def major_sections_extractor(self,List):
        List.append('RENT')
        for i in range(0,len(self.headings_list)-1):
            try:
                temp = re.sub(self.headings_list[i + 1], '',
                              re.search('{0}(.*){1}'.format(self.headings_list[i], self.headings_list[i + 1]), self.copy).group())
                start_index = self.copy.index(temp)
                end_index = start_index+len(temp)

                if any(op in self.headings_list[i] for op in List) and 'CLAUSE' not in self.headings_list[i]:
                    self.tempo = self.copy[start_index:end_index]
                    trial2 = {}
                    trial8 = {}

                    if 'LATE CHARGE' in self.headings_list[i]:
                        docu = nlp2(self.tempo)
                        for ent in docu.ents:
                            strt_idx = self.copy.index(ent.text)
                            end_idx = strt_idx + len(ent.text)
                            trial2 = {'Field_Name': ent.label_, 'Start_Index': strt_idx, 'End_Index': end_idx,'Text': temp,
                                      'Value': self.test_text[strt_idx:end_idx]}
                            self.opportunity_list.append(trial2)

                    elif 'RENT' in self.headings_list[i]:
                        if 'CAM_EXCLUSION' in List:
                            self.cam_incl_excl_and_recdue_extractor('CAM_EXCLUSION')
                        if 'CAM_INCLUSION' in List:
                            self.cam_incl_excl_and_recdue_extractor('CAM_INCLUSION')
                        if 'RECDUE' in List:
                            self.cam_incl_excl_and_recdue_extractor('RECDUE')
                        if 'TENANT AUDIT RIGHTS' in List:
                            self.tenant_audit_rights_extractor()
                        if 'MANAGEMENT FEE NOTES' in List:
                            self.management_fee_extractor()
                        if 'AMORTIZED CAP RECOVERY PART1' in List:
                            self.amcap_extractor()

                    elif 'MISCEL' in self.headings_list[i]:
                        docume = nlp10(self.tempo)
                        for ent in docume.ents:
                            strt_idx = self.copy.index(ent.text)
                            end_idx = strt_idx + len(ent.text)
                            trial2 = {'Field_Name': ent.label_, 'Start_Index': strt_idx, 'End_Index': end_idx, 'Text': temp,
                                      'Value': self.test_text[strt_idx:end_idx]}
                            self.opportunity_list.append(trial2)

                    elif 'HOLDOVER' in self.headings_list[i]:
                        docum = nlp12(self.tempo)
                        for ent in docum.ents:
                            strt_idx = self.copy.index(ent.text)
                            end_idx = strt_idx + len(ent.text)
                            trial = {'Field_Name': ent.label_, 'Start_Index': strt_idx, 'End_Index': end_idx, 'Text': temp,
                                      'Value': self.test_text[strt_idx:end_idx]}
                            self.opportunity_list.append(trial)
                        if not docum.ents :
                            trial = {'Field_Name': self.headings_list[i], 'Start_Index': start_index, 'End_Index': end_index,
                                     'Text': temp, 'Value': temp}
                            self.opportunity_list.append(trial)

                    elif 'INSURANCE' in self.headings_list[i]:
                        document = nlp13(self.tempo)
                        for ent in document.ents:
                            strt_idx = self.copy.index(ent.text)
                            end_idx = strt_idx + len(ent.text)
                            trial = {'Field_Name': ent.label_, 'Start_Index': strt_idx, 'End_Index': end_idx, 'Text': temp,
                                      'Value': self.test_text[strt_idx:end_idx]}
                            self.opportunity_list.append(trial)
                        if not document.ents :
                            trial = {'Field_Name': self.headings_list[i], 'Start_Index': start_index, 'End_Index': end_index,
                                     'Text': temp, 'Value': temp}
                            self.opportunity_list.append(trial)

                    else:
                        trial = {'Field_Name': self.headings_list[i], 'Start_Index': start_index, 'End_Index': end_index,
                                 'Text': temp,'Value': temp}
                        self.opportunity_list.append(trial)

            except:
                print(traceback.print_exc())

    def exhibits_extractor(self,List):

        dc = nlp14(self.test_text)
        for ent in dc.ents:
            #print(ent.label_, ent.text)
            self.exhibits_list.append(ent.text)

        self.exhibits_list = [re.sub(r'\n',' ',x) for x in self.exhibits_list]
        #print(self.exhibits_list)

        for i in range(0,len(self.exhibits_list)-1):

            try:
                tem = re.sub(self.exhibits_list[i + 1], '',
                              re.search('{0}(.*){1}'.format(self.exhibits_list[i], self.exhibits_list[i + 1]), self.copy).group())
                #print(tem)
                start_index = self.copy.index(tem)
                end_index = start_index+len(tem)

                if any(ex in self.exhibits_list[i] for ex in List) and '-' not in self.exhibits_list[i]:
                    trial = {'Field_Name': self.exhibits_list[i], 'Start_Index': start_index, 'End_Index': end_index,
                             'Text': self.test_text[start_index:end_index], 'Value': self.test_text[start_index:end_index]}
                    self.opportunity_list.append(trial)

            except:
                print(traceback.print_exc())

    def function_executor(self,List1,List2,List3):

        self.Ist_Page_Info_List = List1
        self.OP_List = List2
        self.EX_List = List3
        self.Function_List.append({'Name': 'Load PDF', 'Value': 'self.load_pdf()'})
        self.Function_List.append({'Name': 'Extract Headings', 'Value': 'self.headings_extractor()'})
        self.Function_List.append({'Name': 'Extract First Section', 'Value': 'self.first_section_extractor()'})
        self.Function_List.append({'Name': 'Extract Commencement Date', 'Value': 'self.commencement_date_extractor()'})
        self.Function_List.append({'Name': 'Extract Tenant Address', 'Value': 'self.tenant_address_extractor()'})
        self.Function_List.append({'Name': 'Extract Tenant Company', 'Value': 'self.tenant_company_extractor()'})
        self.Function_List.append(
            {'Name': 'Extract Other First Page Infos', 'Value': 'self.premise_building_area_extractor()'})
        self.Function_List.append(
            {'Name': 'Extract CAM and Security Deposit', 'Value': 'self.cam_security_deposit_extractor()'})
        self.Function_List.append(
            {'Name': 'Extract Major Opportunities', 'Value': 'self.major_sections_extractor(self.OP_List)'})
        self.Function_List.append({'Name': 'Extract Exhibits', 'Value': 'self.exhibits_extractor(self.EX_List)'})

        Final_List = self.Ist_Page_Info_List

        if self.Ist_Page_Info_List:
            Final_List.append('Extract Headings')
            Final_List.append('Extract First Section')
        if self.OP_List:
            Final_List.append('Extract Headings')
            Final_List.append('Extract Major Opportunities')
        if self.EX_List:
            Final_List.append('Extract Headings')
            Final_List.append('Extract Exhibits')

        for Function in self.Function_List:
            if any(func in Function['Name'] for func in Final_List) or 'Load PDF' in Function['Name']:
                eval(Function['Value'])

    def abstracted_data_list_json_output_and_CSV_File(self):
        Output ={}
        Output['Fields'] = self.opportunity_list
        print(Output)
        with open('data.json', 'w') as outfile:
            json.dump(Output, outfile)

        self.dataframe = pd.DataFrame(Output['Fields'])
        self.dataframe.drop({'End_Index','Start_Index'},axis=1,inplace = True)
        self.dataframe['Field_Name'] = self.dataframe['Field_Name'].apply(lambda x: re.sub(r'\d|\.','',x).strip())
        self.dataframe.to_csv('Lease_Extraction_Results.csv')
        print(self.dataframe)

if __name__ == "__main__":
    Lease_Extractor = Lease_Data_Extractor()
    #Lease_Extractor.load_pdf()
    OP_List = ['LATE CHARGE', 'USE', 'UTILITIES', 'ALTERATION', 'HOLDOVER', 'ACCEPTANCE', "TENANT'S REPAIR",
                   "INSURANCE", "MISCEL", "DEPOSIT", "PARKING", "LANDLORD'S REPAIR",'CAM_INCLUSION','CAM_EXCLUSION',
               'RECDUE','AMORTIZED CAP RECOVERY PART1','TENANT AUDIT RIGHTS','MANAGEMENT FEE NOTES']
    Ist_Page_Info_List = ['Extract Tenant Company','Extract Commencement Date','Extract Tenant Address',
                          'Extract Other First Page Infos','Extract CAM and Security Deposit']
    #OP_List = ['PARKING','LATE CHARGE',]
    EX_List = ['VAC', 'CONSTRUCTION', 'TI WORK', 'IMPROVEMENT' , 'RENT' ,'Rent']
    #EX_List = ['VAC']
    Lease_Extractor.function_executor(Ist_Page_Info_List,OP_List,EX_List)
    Lease_Extractor.abstracted_data_list_json_output_and_CSV_File()
