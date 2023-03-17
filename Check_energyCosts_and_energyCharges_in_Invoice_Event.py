
'''This  function prints the differences in energy cost and energy charges if they exists '''



def checkEnergySegmentsInvoice(invoice1,invoice2,path_invoices):
    import json
    import os
    path = r'C:\Users\bogdan.doru\Desktop\8070'

    os.chdir(path)

    with open(invoice1, mode='r') as f:
        invoice_1 = json.load(f)

    energyCosts_1 = invoice_1['contracts'][0]['contractInvoice']['energyCosts']
    energyCharges_1 = invoice_1['contracts'][0]['contractInvoice']['energyCharges']

    with open(invoice2, mode='r') as f:
        invoice_2 = json.load(f)

    energyCosts_2 = invoice_2['contracts'][0]['contractInvoice']['energyCosts']
    energyCharges_2 = invoice_2['contracts'][0]['contractInvoice']['energyCharges']

   # print(energyCosts_1 == energyCosts_2)
   # print(energyCharges_1 == energyCharges_2)

    for elem in ['taxRate', 'taxKey', 'taxType', 'amountNet', 'amountTax', 'amountGross']:
        if energyCosts_1[elem] != energyCosts_2[elem]:
            print("invoice_1  value  =  {value} <<<<>>> invoice_2  value =  {value_2} for key {key}".format(
                value=energyCosts_1[elem], value_2=energyCosts_2[elem], key=elem))

    for elem in ['taxRate', 'taxKey', 'taxType', 'amountNet', 'amountTax', 'amountGross']:
        if energyCharges_1[elem] != energyCharges_2[elem]:
         print("invoice_1  value  =  {value} <<<<>>> invoice_2  value =  {value_2} for key {key}".format(
                value=energyCharges_1[elem], value_2=energyCharges_2[elem], key=elem))




checkEnergySegmentsInvoice('invoice1.json','invoice2.json',r'C:\Users\bogdan.doru\Desktop\8070')