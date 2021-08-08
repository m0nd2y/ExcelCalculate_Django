from django.http.response import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.
def calculate(request) :
    file = request.FILES['fileInput']
    df = pd.read_excel(file, sheet_name='Sheet1', header=0)
    grade_dic = {}
    total_row_num = len(df.index)
    for i in range(df.index) :
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
    return HttpResponse("calculate, calculate function!")