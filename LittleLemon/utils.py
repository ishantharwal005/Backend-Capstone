from rest_framework.response import Response
import requests
from django.http import response
import base64
from datetime import datetime
import requests
import random
from random import seed
from random import randint
from django.db import connection
from datetime import timedelta
import pytz


IST = pytz.timezone('Asia/kolkata')



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def write_API_Called(apiName, data):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date = now.strftime("%d%m%y")
    f = open(f"./Logs/ApiCalledLogs{date}.log", "a")
    f.writelines(
        [f'\n \n AT {apiName} Api Called {dt_string} \n ', f'Data Object Sent - {data} \n '])


today = datetime.now().strftime("%Y%m%d")


def getlocaltime():

    datetime_ist = datetime.now(IST)

    curr_clock = datetime_ist.strftime("%H%M%S")

    return curr_clock


def gettenantpharma(tenantrecno):
    pharma=False
    sqlquery=f"select pharma from tenant where recno = {tenantrecno}"
    with connection.cursor() as c:
        c.execute(sqlquery)
        row=dictfetchall(c)
        if len(row) > 0:
            pharma=row[0]['pharma']
    return pharma



def geteventtype(eventtype):

    if eventtype == 1:
        return "Action"

    if eventtype == 2:
        return "Referal"



def gettenantrecno(domainrecno):
    Tenantrecno=0
    gettenant = f"select tenantrecno from domain where recno={domainrecno}"
    with connection.cursor()as c:
        c.execute(gettenant)
        tenant = dictfetchall(c)
        if len(tenant) > 0:
            Tenantrecno = tenant[0]['tenantrecno']
    return Tenantrecno
def getcustomerrecnofromdomain(domainrecno):
    customerrecno=0
    getcreditcontrol = f"select customerrecno from domain where recno={domainrecno}"
    with connection.cursor() as c:
        c.execute(getcreditcontrol)
        domcc = dictfetchall(c)
        if len(domcc) > 0:
            customerrecno = domcc[0]['customerrecno']
    return customerrecno
def checksupplierisourcustomer(tenantrecno, supplierrecno):
    domainrecno=0
    sqlquery = f"select recno from domain where tenantrecno={tenantrecno} and customerrecno = {supplierrecno}"
    with connection.cursor() as c:
        c.execute(sqlquery)
        rows = dictfetchall(c)
        if len(rows)>0:
            domainrecno = rows[0]['recno']
    return domainrecno

def validateData(request_data, model):
    try:
        for key in model:
            if(request_data.get(key, None) == None):
                return {"Success": False, "Message": key+" is required."}
        return {"Success": True}
    except Exception as err:
        return {"Success": False, "Message": str(err)}
def checkifblank(amount):
    if amount ==None or amount == '':
        amount = 0.00
    else:
        amount = float(amount)
    return amount
# to generate billno smk
def generateinstringfromcommaseperated(str):
    breakstring = Convert_String(str)
    users = ""
    if len(breakstring) > 0:
        users = "("
        for user in breakstring:
            users = users + f"{user}, "

        lengthOfuser = len(users) - 2
        users = users[:lengthOfuser]
        users = users + ")"
    return users
def Convert_String(string):
    li = list(string.split(","))
    return li

def getToday():
    now = datetime.now()
    date = now.strftime("%Y%m%d")
    return date

def write_logs(input):
    f = open("./custom.log", "a")
    f.writelines(input)
    f.close()