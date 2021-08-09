from math import e
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd

# Create your views here.
def calculate(request) :
    file = request.FILES['fileInput']

    origin_file_name = file.name
    user_name = request.session['user_name']
    now_HWS = document.today().strftime('%H%M%S')

    df = pd.read_excel(file, sheet_name='Sheet1', header=0)
    grade_dic = {}
    total_row_num = len(df.index)
    for i in range(total_row_num) :
        data = df.loc[i]
        if not data['grade'] in grade_dic.keys():
            grade_dic[data['grade']] = [data['value']]
        else :
            grade_dic[data['grade']].append(data['value'])
    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {}
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key]))/len(grade_dic[key])
    grade_list = list(grade_calculate_dic.keys())
    grade_list.sort()
    for key in grade_list :
        print("# grade: " , key)
        print("min:",grade_calculate_dic[key]['min'],end='')
        print("/ max:",grade_calculate_dic[key]['max'],end='')
        print("/ avg:",grade_calculate_dic[key]['avg'],end='\n\n')
    email_domain_dic = {}
    for i in range(total_row_num) :
        data = df.loc[i]
        email_domain = (data['email'].split("@"))[1]
        if not email_domain in email_domain_dic.keys():
            email_domain_dic[email_domain] = 1
        else :
            email_domain_dic[email_domain] += 1
    print("## EMAIL 도메일별 사용 인원")
    for key in email_domain_dic.keys() :
        print("#", key,": ", email_domain_dic[key],"명")
    #return HttpResponse("calculate, calculate function!")
    grade_calculate_dic_to_session = {}
    for key in grade_list:
        grade_calculate_dic_to_session[int(key)] = {}
        grade_calculate_dic_to_session[int(key)]['max'] = float(grade_calculate_dic[key]['max'])
        grade_calculate_dic_to_session[int(key)]['avg'] = float(grade_calculate_dic[key]['avg'])
        grade_calculate_dic_to_session[int(key)]['min'] = float(grade_calculate_dic[key]['min'])
    request.session['grade_calculate_dic'] = grade_calculate_dic_to_session
    request.session['email_domain_dic'] = email_domain_dic
    return redirect('/result')