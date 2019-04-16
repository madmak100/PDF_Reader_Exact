#print(text[2697:2897])
dir  = "C:\\PyWork\\Headings"
import re
text = ""
import spacy
text = re.sub('\n',' ',text)
#text = re.sub('RENT COMMENCEMENT','RENT-COMMENCEMENT',text)
#print(text)
text1 = text
#text = re.sub('\n',' ',text)


heading = re.findall(r'<H>(.*?)</H>',text)
exhibit = re.findall(r'<EXHIBIT>(.*?)</EXHIBIT>', text)
tnt = re.findall(r'<TNT>(.*?)</TNT>', text)
lnd = re.findall(r'<LNDLRD>(.*?)</LNDLRD>', text)
prms = re.findall(r'<PRMS>(.*?)</PRMS>', text)
bld = re.findall(r'<BLD>(.*?)</BLD>', text)
cmp = re.findall(r'<CMP>(.*?)</CMP>', text)
poar = re.findall(r'<POAR>(.*?)</POAR>', text)
area = re.findall(r'<AREA>(.*?)</AREA>', text)
pro_rata = re.findall(r'<TPRS>(.*?)</TPRS>', text)#CMNC_DATE
cmnc_date = re.findall(r'<CMNC_DATE>(.*?)</CMNC_DATE>', text)
addresses = re.findall(r'<ADRS>(.*?)</ADRS>', text)
cam_try = re.findall(r'<CAM_TRY>(.*?)</CAM_TRY>', text)
cam_inc = re.findall(r'<CAM_INC>(.*?)</CAM_INC>', text)
cam_exc = re.findall(r'<CAM_EXC>(.*?)</CAM_EXC>', text)
prm_use = re.findall(r'<PRM_USE>(.*?)</PRM_USE>', text)
tic = re.findall(r'<TIC>(.*?)</TIC>', text)
moe = re.findall(r'<MOE>(.*?)</MOE>', text)
sd = re.findall(r'<SD>(.*?)</SD>', text)
sd_br_moe = re.findall(r'<SD_BR_MOE>(.*?)</SD_BR_MOE>', text)
lcir = re.findall(r'<LATE_CHARGE_INT_RATE>(.*?)</LATE_CHARGE_INT_RATE>',text)

text = re.sub(r'<H>','',text)
text = re.sub(r'</H>','',text)
text = re.sub(r'<EXHIBIT>','',text)
text = re.sub(r'</EXHIBIT>','',text)
text = re.sub(r'<LATE_CHARGE_INT_RATE>','',text)
text = re.sub(r'</LATE_CHARGE_INT_RATE>','',text)
text = re.sub(r'<TNT>','',text)
text = re.sub(r'</TNT>','',text)
text = re.sub(r'<POAR>','',text)
text = re.sub(r'</POAR>','',text)
text = re.sub(r'<LNDLRD>','',text)
text = re.sub(r'</LNDLRD>','',text)
text = re.sub(r'<PRMS>','',text)
text = re.sub(r'</PRMS>','',text)
text = re.sub(r'<BLD>','',text)
text = re.sub(r'</BLD>','',text)
text = re.sub(r'<CMP>','',text)
text = re.sub(r'</CMP>','',text)
text = re.sub(r'<AREA>','',text)
text = re.sub(r'</AREA>','',text)
text = re.sub(r'<TPRS>','',text)
text = re.sub(r'</TPRS>','',text)
text = re.sub(r'<CMNC_DATE>','',text)
text = re.sub(r'</CMNC_DATE>','',text)#ADRS
text = re.sub(r'<ADRS>','',text)
text = re.sub(r'</ADRS>','',text)
text = re.sub(r'<CAM_TRY>','',text)
text = re.sub(r'</CAM_TRY>','',text)
text = re.sub(r'<CAM_INC>','', text)
text = re.sub(r'<CAM_EXC>','', text)
text = re.sub(r'</CAM_INC>','', text)
text = re.sub(r'</CAM_EXC>','', text)
text = re.sub(r'</PRM_USE>','', text)
text = re.sub(r'<PRM_USE>','', text)
text = re.sub(r'</SD>','', text)
text = re.sub(r'<SD>','', text)
text = re.sub(r'</TIC>','', text)
text = re.sub(r'<TIC>','', text)
text = re.sub(r'</MOE>','', text)
text = re.sub(r'<MOE>','', text)
text = re.sub(r'</SD_BR_MOE>','', text)
text = re.sub(r'<SD_BR_MOE>','', text)

text1 = re.sub(r'<H>','',text1)
text1 = re.sub(r'</H>','',text1)
text1 = re.sub(r'<EXHIBIT>','',text1)
text1 = re.sub(r'</EXHIBIT>','',text1)
text1 = re.sub(r'<LATE_CHARGE_INT_RATE>','',text1)
text1 = re.sub(r'</LATE_CHARGE_INT_RATE>','',text1)
text1 = re.sub(r'<TNT>','',text1)
text1 = re.sub(r'</TNT>','',text1)
text1 = re.sub(r'<LNDLRD>','',text1)
text1 = re.sub(r'</LNDLRD>','',text1)
text1 = re.sub(r'<PRMS>','',text1)
text1 = re.sub(r'</PRMS>','',text1)
text1 = re.sub(r'<BLD>','',text1)
text1 = re.sub(r'</BLD>','',text1)
text1 = re.sub(r'<CMP>','',text1)
text1 = re.sub(r'</CMP>','',text1)
text1 = re.sub(r'<POAR>','',text1)
text1 = re.sub(r'</POAR>','',text1)
text1 = re.sub(r'<AREA>','',text1)
text1 = re.sub(r'</AREA>','',text1)
text1 = re.sub(r'<TPRS>','',text1)
text1 = re.sub(r'</TPRS>','',text1)
text1 = re.sub(r'<CMNC_DATE>','',text1)
text1 = re.sub(r'</CMNC_DATE>','',text1)
text1 = re.sub(r'<ADRS>','',text1)
text1 = re.sub(r'</ADRS>','',text1)
text1 = re.sub(r'<CAM_TRY>','',text1)
text1 = re.sub(r'</CAM_TRY>','',text1)
text1 = re.sub(r'<CAM_INC>','', text1)
text1 = re.sub(r'<CAM_EXC>','', text1)
text1 = re.sub(r'</CAM_INC>','', text1)
text1 = re.sub(r'</CAM_EXC>','', text1)
text1 = re.sub(r'</PRM_USE>','', text1)
text1 = re.sub(r'<PRM_USE>','', text1)
text1 = re.sub(r'</SD>','', text1)
text1 = re.sub(r'<SD>','', text1)
text1 = re.sub(r'</TIC>','', text1)
text1 = re.sub(r'<TIC>','', text1)
text1 = re.sub(r'</MOE>','', text1)
text1 = re.sub(r'<MOE>','', text1)
text1 = re.sub(r'</SD_BR_MOE>','', text1)
text1 = re.sub(r'<SD_BR_MOE>','', text1)

exhibita = ""
poara = ""
ta = ""
la = ""
pa = ""
ba = ""
ca = ""
aa = ""
prsa = ""
cmnca = ""
ada = ""
cam_trya = ""
cam_incl = ""
cam_excl = ""
prmuse = ""
tica = ""
sda = ""
moea = ""
sdbrmoe = ""
lcira = ""
heads = ""

for i in tnt:
    idx = text.index(i)
    ta = ta + "({0},{1},LABEL1),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in lnd:
    idx = text.index(i)
    la = la + "({0},{1},LABEL2),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in prms:
    idx = text.index(i)
    pa = pa + "({0},{1},LABEL3),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in bld:
    idx = text.index(i)
    ba = ba + "({0},{1},LABEL4),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in cmp:
    idx = text.index(i)
    ca = ca + "({0},{1},LABEL1),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in area:
    idx = text.index(i)
    aa = aa + "({0},{1},LABEL2),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in pro_rata:
    idx = text.index(i)
    prsa = prsa + "({0},{1},LABEL2),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in cmnc_date:
    idx = text.index(i)
    cmnca = cmnca + "({0},{1},LABEL1),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in addresses:
    idx = text.index(i)
    ada = ada + "({0},{1},LABEL5),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in cam_try:
    idx = text.index(i)
    cam_trya = cam_trya + "({0},{1},LABEL),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in cam_inc:
    idx = text.index(i)
    cam_incl = cam_incl + "({0},{1},LABEL1),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in cam_exc:
    idx = text.index(i)
    cam_excl = cam_excl + "({0},{1},LABEL2),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in prm_use:
    idx = text.index(i)
    prmuse = prmuse + "({0},{1},LABEL6),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in sd:
    idx = text.index(i)
    sda = sda + "({0},{1},LABEL1),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in sd_br_moe:
    idx = text.index(i)
    sdbrmoe = sdbrmoe + "({0},{1},LABEL2),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in tic:
    idx = text.index(i)
    tica = tica + "({0},{1},LABEL3),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in moe:
    idx = text.index(i)
    moea = moea + "({0},{1},LABEL4),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in lcir:
    idx = text.index(i)
    lcira = lcira + "({0},{1},LABEL1),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in poar:
    idx = text.index(i)
    poara = poara + "({0},{1},LABEL3),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in exhibit:
    idx = text.index(i)
    exhibita = exhibita + "({0},{1},LABEL3),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])

for i in heading:
    idx = text.index(i)
    heads = heads + "({0},{1},LABEL),".format(idx, (idx + len(i)))
    print(text1[idx:idx + len(i)])
print(text)
#print(ta)
#print(la)
#print(pa)
#print(ba)
#print(prsa)
#print(ada)
#print(cam_trya)
#print(cam_incl)
#print(cam_excl)
#print(poara)
print(heads)
#print(prmuse)
#print(ca)
#print(aa)
#print(sda)
#print(sdbrmoe)
#print(tica)
#print(moea)

