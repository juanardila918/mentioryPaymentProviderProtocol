from typing import Union
import serial
import Class 
from fastapi import Body, FastAPI
import json
import asyncio
from typing import Any
from fastapi import Request, FastAPI
from fastapi.encoders import jsonable_encoder
from typing_extensions import Annotated
import requests
import aiohttp  
app = FastAPI()
with open('clients.json',"r") as file:
       contrast=json.load(file)

loop = asyncio.get_event_loop()  
client = aiohttp.ClientSession(loop=loop)
    
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/manifest")
async def read_root():
    return {
  "paymentMethods": [
    {
      "name": "Visa",
      "allowsSplit": "onCapture"
    },
    {
      "name": "Mastercard",
      "allowsSplit": "onCapture"
    },
    {
      "name": "American Express",
      "allowsSplit": "onCapture"
    },
    {
      "name": "BankInvoice",
      "allowsSplit": "disabled"
    },
    {
      "name": "Privatelabels",
      "allowsSplit": "disabled"
    },
    {
      "name": "Promissories",
      "allowsSplit": "disabled"
    }
  ],
  "customFields": [
    {
      "name": "Client ID",
      "type": "text"
    },
    {
      "name": "Secret Token",
      "type": "password"
    },
    {
      "name": "Currency",
      "type": "select",
      "options": [
        {
          "text": "COP",
          "value": "1"
        },
        {
          "text": "USD",
          "value": "2"
        }
      ]
    }
  ]
,
  "autoSettleDelay": {
    "minimum": "0",
    "maximum": "720"
  }
}
#uvicorn main:app --reload
async def callback(data:Class.data):
    asyncio.sleep(5)
    with open('data.json',"r") as file:
        data1=json.load(file)
    if (data1[data['paymentId']]['status']=='Undefined'):
      url=data1[data['paymentId']]["callbackUrl"]
      headers = {
      'Accept': "application/json",
      'Content-Type': "application/json; charset=utf-8",
      'X-VTEX-API-AppKey': 'vtexappkey-cenltier3-OKQDPM',
      'X-VTEX-API-AppToken':'LJIEKBGXQXZKVBDQAOZUFDMBRKJYROYNWZNWPTEHNRFEFXPWSLIRJXHHIUKKHDFTEPCJZJEKCCWAVKIWHZCSEPOIVBRJHBPANDMPQGBWQZBYUUHMRKDPIPMAMTCJTWRA'
      }
      data= '{"paymentId": "'+str(data['paymentId'])+'","status": "approved","authorizationId":"'+str(data['paymentId'])+"E"+"34"+'","nsu": "NSU987432","tid": "TID1578324421","acquirer": "FooBarPayments","delayToAutoSettle": 432000,"delayToAutoSettleAfterAntifraud": 120,"delayToCancel": 600}'
      
      response = requests.post(url=url,headers=headers,data=data)
     
    return(data)

@app.post("/payments")
async def defineestatus(data:Class.data,request:Request):
    #null=None
    
    false=False
    true=True
    data = await request.json()
    if (data['paymentMethod']=="Visa" or data['paymentMethod']=="Mastercard" or data['paymentMethod']=="American Express" ):

      try: 
        if (contrast[data['card']['number']]["card"]==data['card']['number']):
          with open('data.json',"r") as file:
            data1=json.load(file)
            data1[data['paymentId']]=data
            data1[data['paymentId']]['status']="approved"
          with open('data.json',"w") as file:
            json.dump(data1, file)
          response = {
          "paymentId": data['paymentId'],
          "status": "approved",
          "authorizationId": data['paymentId']+"E"+"34",
          "nsu": "NSU987432",
          "tid": "TID1578324421",
          "acquirer": "FooBarPayments",
          "delayToAutoSettle": 432000,
          "delayToAutoSettleAfterAntifraud": 120,
          "delayToCancel": 600
          }
          print(response)
          return response
      except:
        with open('data.json',"r") as file:
          data1=json.load(file)
          data1[data['paymentId']]=data
          data1[data['paymentId']]['status']="denied"
        with open('data.json',"w") as file:
          json.dump(data1, file)
          response= {
        "paymentId": data['paymentId'],
        "status": "denied",
        "authorizationId": data['paymentId']+"E"+"34",
        "nsu": "NSU987432",
        "tid": "TID1578324421",
        "acquirer": "FooBarPayments",
        "delayToAutoSettle": 432000,
        "delayToAutoSettleAfterAntifraud": 120,
        "delayToCancel": 600
        }
        print(response)
        return response
    if (data['paymentMethod']=="Promissories"):
        with open('data.json',"r") as file:
          data1=json.load(file)
          data1[data['paymentId']]=data
          data1[data['paymentId']]['status']="Undefined"
        with open('data.json',"w") as file:
          json.dump(data1, file)
        response = {
        "paymentId": data['paymentId'],
        "status": "undefined",
        "authorizationId": data['paymentId']+"E"+"34",
        "nsu": "NSU987432",
        "tid": "TID1578324421",
        "acquirer": "FooBarPayments",
        "delayToAutoSettle": 432000,
        "delayToAutoSettleAfterAntifraud": 120,
        "delayToCancel": 600
        }
        print(response)
        await callback(data=data)
        print("check1")
        return response

@app.post("/payments/{paymentId}/settlements")
async def settlepayment(paymentId,data:Class.forsettle,request:Request):
    #null=None
    
    false=False
    true=True
    data = await request.json()
    print(data)
    with open('data.json',"r") as file:
       data1=json.load(file)
       data1[data['paymentId']]['status']="settled"
    with open('data.json',"w") as file:
       json.dump(data1, file)
    
    return {
"paymentId": str(paymentId),
"settleId": "2EA354989E7E4BBC9F9D7B66674C2574",
"value": data["value"],
"code": "null",
"message": "Successfully settled",
"requestId": data["requestId"]
}
@app.post("/payments/{paymentId}/settlements")
async def settlepayment(paymentId,data:Class.forsettle,request:Request):
    #null=None
    
    false=False
    true=True
    data = await request.json()
    print(data)
    with open('data.json',"r") as file:
       data1=json.load(file)
       data1[data['paymentId']]['status']="settled"
    with open('data.json',"w") as file:
       json.dump(data1, file)
    
    return {
"paymentId": str(paymentId),
"settleId": "2EA354989E7E4BBC9F9D7B66674C2574",
"value": data["value"],
"code": "null",
"message": "Successfully settled",
"requestId": data["requestId"]
}
@app.post("/payments/{paymentId}/refunds")
async def settlepayment(paymentId,data:Class.forrefund,request:Request):
    #null=None
    
    false=False
    true=True
    data = await request.json()
    print(data)
    with open('data.json',"r") as file:
       data1=json.load(file)
       data1[data['paymentId']]['status']="settled"
    with open('data.json',"w") as file:
       json.dump(data1, file)
    
    return {
"paymentId": str(paymentId),
"refundId": "2EA354989E7E4BBC9F9D7B66674C2574",
"value": data["value"],
"code": "null",
"message": "Successfully refunded",
"requestId": data["requestId"]
}
@app.post("/payments/{paymentId}/cancellations")
async def cancelpayment(paymentId,data:Class.for_cancelations,request:Request):
    #null=None
    
    false=False
    true=True
    data = await request.json()
    
    with open('data.json',"r") as file:
       data1=json.load(file)
       data1[data['paymentId']]['status']="cancelled"
    with open('data.json',"w") as file:
       json.dump(data1, file)
    
    return {
  "paymentId": str(paymentId),
  "cancellationId": "1231323234234",
  "code": "null",
  "message": "Successfully cancelled",
  "requestId":  data["requestId"]
  }