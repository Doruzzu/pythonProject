# -*- coding: utf-8 -*-

"""
The program prints the validation rules published by EBA  in a XML format


<forEach name="row" values="values('IFRS-nGAAP_3469;r091','IFRS-nGAAP_3471;r092','IFRS-nGAAP_3473;r093','IFRS-nGAAP_3475;r094','IFRS-nGAAP_3477;r095','IFRS-nGAAP_3487;r110','IFRS-nGAAP_3497;r171','IFRS-nGAAP_3499;r172','IFRS-nGAAP_3501;r173','IFRS-nGAAP_3503;r174','IFRS-nGAAP_3505;r175','IFRS-nGAAP_3507;r176','IFRS-nGAAP_3509;r177','IFRS-nGAAP_3511;r178','IFRS-nGAAP_3519;r231','IFRS-nGAAP_3521;r232','IFRS-nGAAP_3523;r233','IFRS-nGAAP_3525;r234','IFRS-nGAAP_3527;r235','IFRS-nGAAP_3529;r236','IFRS-nGAAP_3531;r237','IFRS-nGAAP_3535;r315','IFRS-nGAAP_3537;r330','IFRS-nGAAP_3537;r330')">
	<rule id="$substr(row,1,IndexOf(row,';'))$"
	checkWhen="getSQLValue('select FI_COUNTRY_CODE from FINANCIAL_INST where F001 = ''$f001$''') = '003'  and getBankInfo('FI_ACCOUNTING')=2 "
	formula="FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_2.ft_20.ft_20_1![$substr(row,(IndexOf(row,';')+2),10)$,c020] = 0 " />
</forEach>

<forEach name="row" values="values('IFRS-nGAAP_3591;r085','IFRS-nGAAP_3593;r095','IFRS-nGAAP_3595;r120','IFRS-nGAAP_3599;r175','IFRS-nGAAP_3603;r275','IFRS-nGAAP_3603;r275')">
	<rule id="$substr(row,1,IndexOf(row,';'))$"
	checkWhen="getSQLValue('select FI_COUNTRY_CODE from FINANCIAL_INST where F001 = ''$f001$''') = '003'  and getBankInfo('FI_ACCOUNTING')=2 "
	formula="FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_2.ft_20.ft_20_3![$substr(row,(IndexOf(row,';')+2),10)$,c020] = 0 " />
</forEach>
"""
import os 

path=r'C:\Users\bogdan.doru\Desktop\Python files'

os.chdir(path)
os.getcwd()


dict_mod={'F 01.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_1.ft_1_1!',
          'F 01.02':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_1.ft_1_2!',
          'F 01.03':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_1.ft_1_3!',
          'F 02.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_2!',
          'F 03.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_3!',
          'F 04.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_4.ft_4_1!',
          'F 04.02.1':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_4.ft_4_2_1!',
          'F 04.02.2':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_4.ft_4_2_2!',
          'F 04.03.1':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_4.ft_4_3_1!',   
          'F 04.04.1':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_4.ft_4_4_1!',
          'F 07.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_7.ft_7_1!',
          'F 08.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_8.ft_8_1!',
          'F 08.02':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_8.ft_8_2!',
          'F 09.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_9.ft_9_1!',
          'F 09.01.1':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_9.ft_9_1_1!',
          'F 10.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_10!',
          'F 11.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_11.ft_11_1!',
          'F 11.03':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_11.ft_11_3!',
          'F 11.04':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_11.ft_11_4!',
          'F 12.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_12.ft_12_0!',
          'F 12.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_12.ft_12_1!',
          'F 12.02':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_12.ft_12_2!',
          'F 14.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_14!',
          'F 15.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_15!',
          'F 16.02':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_16.ft_16_2!',
          'F 16.03':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_16.ft_16_3!',
          'F 16.04':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_16.ft_16_4!',
          'F 16.04.1':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_16.ft_16_4_1!',
          'F 16.05':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_16.ft_16_5!',
          'F 17.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_17.ft_17_1!',
          'F 17.03':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_1.ft_17.ft_17_3!',
          'F 20.01':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_2.ft_20.ft_20_1!',
          'F 20.02':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_2.ft_20.ft_20_2!',
          'F 20.03':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_2.ft_20.ft_20_3!',
          'F 21.00':'FinRep_IFRS_nGAAP.consolidated_reporting_C.part_2.ft_21!' }



dict_mod_sub={'F 01.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_1.ft_1_1!',
          'F 01.02':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_1.ft_1_2!',
          'F 01.03':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_1.ft_1_3!',
          'F 02.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_2!',
          'F 03.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_3!',
          'F 04.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_4.ft_4_1!',
          'F 04.02.1':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_4.ft_4_2_1!',
          'F 04.02.2':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_4.ft_4_2_2!',
          'F 04.03.1':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_4.ft_4_3_1!',   
          'F 04.04.1':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_4.ft_4_4_1!',
          'F 07.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_7.ft_7_1!',
          'F 08.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_8.ft_8_1!',
          'F 08.02':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_8.ft_8_2!',
          'F 09.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_9.ft_9_1!',
          'F 09.01.1':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_9.ft_9_1_1!',
          'F 10.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_10!',
          'F 11.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_11.ft_11_1!',
          'F 11.03':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_11.ft_11_3!',
          'F 11.04':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_11.ft_11_4!',
          'F 12.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_12.ft_12_0!',
          'F 12.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_12.ft_12_1!',
          'F 12.02':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_12.ft_12_2!',
          'F 14.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_14!',
          'F 15.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_15!',
          'F 16.02':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_16.ft_16_2!',
          'F 16.03':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_16.ft_16_3!',
          'F 16.04':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_16.ft_16_4!',
          'F 16.04.1':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_16.ft_16_4_1!',
          'F 16.05':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_16.ft_16_5!',
          'F 17.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_17.ft_17_1!',
          'F 17.03':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_17.ft_17_3!',
          'F 20.01':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_2.ft_20.ft_20_1!',
          'F 20.02':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_2.ft_20.ft_20_2!',
          'F 20.03':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_2.ft_20.ft_20_3!',
          'F 21.00':'FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_2.ft_21!' }



dict_mod_Ind={'F 01.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_1.ft_1_1!',
          'F 01.02':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_1.ft_1_2!',
          'F 01.03':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_1.ft_1_3!',
          'F 02.00':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_2!',
          'F 03.00':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_3!',
          'F 04.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_4.ft_4_1!',
          'F 04.02.1':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_4.ft_4_2_1!',
          'F 04.02.2':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_4.ft_4_2_2!',
          'F 04.03.1':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_4.ft_4_3_1!',   
          'F 04.04.1':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_4.ft_4_4_1!',
          'F 07.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_7.ft_7_1!',
          'F 08.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_8.ft_8_1!',
          'F 08.02':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_8.ft_8_2!',
          'F 09.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_9.ft_9_1!',
          'F 09.01.1':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_9.ft_9_1_1!',
          'F 10.00':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_10!',
          'F 11.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_11.ft_11_1!',
          'F 11.03':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_11.ft_11_3!',
          'F 11.04':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_11.ft_11_4!',
          'F 12.00':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_12.ft_12_0!',
          'F 12.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_12.ft_12_1!',
          'F 12.02':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_12.ft_12_2!',
          'F 14.00':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_14!',
          'F 15.00':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_15!',
          'F 16.02':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_16.ft_16_2!',
          'F 16.03':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_16.ft_16_3!',
          'F 16.04':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_16.ft_16_4!',
          'F 16.04.1':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_16.ft_16_4_1!',
          'F 16.05':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_16.ft_16_5!',
          'F 17.01':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_17.ft_17_1!',
          'F 17.03':'FinRep_IFRS_nGAAP.individual_reporting.part_1.ft_17.ft_17_3!',
          'F 20.01':'FinRep_IFRS_nGAAP.individual_reporting.part_2.ft_20.ft_20_1!',
          'F 20.02':'FinRep_IFRS_nGAAP.individual_reporting.part_2.ft_20.ft_20_2!',
          'F 20.03':'FinRep_IFRS_nGAAP.individual_reporting.part_2.ft_20.ft_20_3!',
          'F 21.00':'FinRep_IFRS_nGAAP.individual_reporting.part_2.ft_21!' }

f=open('validation.txt','r')
output=open('outIFRS.txt','w')
dict_list={}
for line in f:
    ''' Contructing a dictionary with columns and rows '''
    rule_name=line[line.find('I'):line.find('I')+15].strip()
    name=line[line.find('F',3):line.find('F',3)+12].strip()
    if  name[-1].isalpha():
         name=name[:-2]
    row=line[line.find('r'):line.find('r')+4]
    col=line[line.find('c'):line.find('c')+4] 
    dict_list.setdefault(name,{})
    dict_list[name].setdefault(col,[])
    dict_list[name][col].append(rule_name+";"+row)
    dict_list[name].setdefault(row,[])
    dict_list[name][row].append(rule_name+";"+col)
    


def max_col_row(dictionary):
   
    dict_max_list=[]
    
    for elem in dictionary.keys():
        maxx=0
        index_max=''
        lis=dictionary[elem].keys()
        for i in lis:
            list_max=[]
           
            if len(dictionary[elem][i]) >=maxx:
                maxx=len(dictionary[elem][i])
                index_max=i
            for key in lis:
                if key.startswith(index_max[0]):
                   list_max.append(key)
                
        dict_max_list.append([elem]+list_max)
    return   dict_max_list  

dor=max_col_row(dict_list)
d={} #dictionary that will contain the module and the columns d={modul:{col1: values,col2:values}}

for elem in dor:
    d.setdefault(elem[0],{})
    for i in elem[1:]: 
        d[elem[0]].setdefault(i)
        
# se va calcula prin functie valorile si se for asigna dict de mai sus       

        
def const_values(d):

    for mod in dor:
        for i in mod[1:]:
            values=''
            for j in dict_list[mod[0]][i]:
                values=values+"\'{:10s}\'".format(j).strip()+","          
            values=values+"\'{:10s}\'".format(dict_list[mod[0]][i][-1])
            d[mod[0]][i]=values
    return d        

# Printam regula 
val_dict=const_values(dict_list)
    
def print_for_each_rules():
    """ Prints rules in for each loop  ex :
    <forEach name="row" values="values('IFRS-nGAAP_3374;r010','IFRS-nGAAP_3376;r071','IFRS-nGAAP_3378;r072','IFRS-nGAAP_3380;r080','IFRS-nGAAP_3382;r090','IFRS-nGAAP_3384;r100','IFRS-nGAAP_3386;r110','IFRS-nGAAP_3388;r120','IFRS-nGAAP_3390;r130','IFRS-nGAAP_3392;r140','IFRS-nGAAP_3392;r140')">
            <rule id="$substr(row,1,IndexOf(row,';'))$"
            checkWhen="getSQLValue('select FI_COUNTRY_CODE from FINANCIAL_INST where F001 = ''$f001$''') = '003'" 
            formula="FinRep_IFRS_nGAAP.subconsolidated_reporting_SC.part_1.ft_16.ft_16_5![$substr(row,(IndexOf(row,';')+2),10)$,c020] = 0 " />
     </forEach>  """

    for elem in dor:
        for rowcol in elem[1:]:
            if rowcol.startswith('c'):
                
                print("<forEach name=\"row\" values=\"values({:50s})\">".format(val_dict[elem[0]][rowcol]),file=output)# sters file=output
                print("\t<rule id=\"$substr(row,1,IndexOf(row,';'))$\"",file=output)#sters file=output
                print("\tcheckWhen=\"getSQLValue(\'select FI_COUNTRY_CODE from FINANCIAL_INST where F001 = \'\'$f001$\'\'\') = \'003\'  and getBankInfo('FI_ACCOUNTING')=2 \" ",file=output)# sters file=output insert getBankInfo
                print("\tformula=\"{:10s}[$substr(row,(IndexOf(row,\';\')+2),10)$,{:3s}] = 0 \" />".format(dict_mod_sub[elem[0]],rowcol),file=output)# sters file=output
                print("</forEach>\n",file=output)# sters file=output
                print()
            elif rowcol.startswith('r'): 
                print("<forEach name=\"col\" values=\"values({:5s})\">".format(val_dict[elem[0]][rowcol]),file=output)#sters file=output
                print("\t<rule id=\"$substr(col,1,IndexOf(col,';'))$\"",file=output)
                print("\tcheckWhen=\"getSQLValue(\'select FI_COUNTRY_CODE from FINANCIAL_INST where F001 = \'\'$f001$\'\'\') = \'003\'\"",file=output)# sters file=output
                print("\tformula=\"{:10s}[$substr(col,(IndexOf(col,\';\')+2),10)$,{:3s}] = 0 \" />".format(dict_mod_sub[elem[0]],rowcol),file=output)# sters file=output
                print("</forEach>",file=output) #

print_for_each_rules()

f.close()
output.close()
              

 










