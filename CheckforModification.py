# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:01:18 2018

@author: bogdan.doru
"""

import os 


path="C:\\Users\\bogdan.doru\\Desktop\\New Validation Rules\\Files Check"
os.chdir(path)
os.getcwd()

Q3=open('Q3.txt','r')
Q4=open('Q4.txt','r')

q3=Q3.readlines()
q4=Q4.readlines()
Q3.close()
Q4.close()

list_modif_rules=[]
'''try:
    for i in range(len(q3)):
        sq3=q3[i].replace(" ","")
        sq4=q4[i].replace(" ","")
        if sq3[:-1]!=sq4[:-1]:
            list_modif_rules.append(q3[i][:8])
except IndexError:
    print("Len sq3 is {:4d} and len sq4 is {:4d}".format(len(q3),len(q4)))'''
    
dict_q3={}
dict_q4={}
mod_rules=[]
new_rules=[]
old_rules=[]

for elem in q3:
    dict_q3.setdefault(elem[:elem.find("\t")].strip(),'') # elem[:elem.find("F")+1] instead of 9
    dict_q3[elem[:elem.find("\t")].strip()]+=elem
    
    
for elem in q4:
    dict_q4.setdefault(elem[:elem.find("\t")].strip(),'')
    dict_q4[elem[:elem.find("\t")].strip()]+=elem                 
    
    
for i in dict_q4.keys():
    if i in dict_q3:
        q3=dict_q3[i].replace(" ","")
        q4=dict_q4[i].replace(" ","")
        if q3!=q4:
            mod_rules.append(i)
    if i not in dict_q3:
        new_rules.append(i)         
       
for i in dict_q3.keys():
    if i not in dict_q4:
        old_rules.append(i)
  # checking of validation rules  written in XML Corep2014
        
list_q4=list(dict_q4.keys())
list_no_gaap=[x for x in  list_q4 if x[:4]!='IFRS']


def checkId(id_file,xml_file):
    ''' Checks for given ID rules are written in the corresponding XML file 
        Exemple: checkId(id_file,xml_file)---> returns the tuple of the rules id's which are not in the xml_file  '''
        
        
    xml_f=open(xml_file,'r')
    id_f=open(id_file,'r')

    list_xml=xml_f.readlines()
    id=id_f.readlines()

    lis_cor=[x.strip('\n') for x in id]
    xml_f.close()
    id_f.close()

    not_in_xml=[]  # validation rules remaining to be written
    str_xml=str(list_xml)

    for i in lis_cor:
        if i not in str_xml:
            not_in_xml.append(i)
    return tuple(not_in_xml)   

''' fin=checkId('FinId.txt','FinrepXML.txt') ''' 
all_rem=checkId('ALLID.txt','ALLXML.txt')