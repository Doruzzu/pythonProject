# -*- coding: utf-8 -*-
""" The program extracts data for a log file i.e. logdata.txt and  and returns a list of dictionary containing host,
user_name, time, request """

import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    logs=logdata.split('\n')
   
    pattern_host=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    pattern_user_name=r'(-)\s([A-Za-z0-9-]+)'#group(2)
   # pattern_time=r'd{1,2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}\s-\d{4}'#group()
    pattern_request=r"[A-Z]{3,}\s.*\sHTTP\/\d+\.\d+" #group()[A-Za-z./_\-+]+
    logs.remove("")
    list_of_dict=[]
    for elem in logs:
        dict_logs={}
        host=re.search(pattern_host,elem).group()
        dict_logs["host"]=host
        user_name=re.search(pattern_user_name, elem).group(2)
        dict_logs["user_name"]=user_name
        time=re.search(r'\d{1,2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}\s-\d{4}', elem).group()
        dict_logs["time"]=time
        request=re.search(pattern_request, elem).group()
        dict_logs["request"]=request
        
        list_of_dict.append(dict_logs)
        
        
    return list_of_dict

print(logs())