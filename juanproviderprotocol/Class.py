from pydantic import BaseModel
class for_cancelations(BaseModel):
  {
  "paymentId": str,
  "requestId": str
}
class card(BaseModel):
    {"holder": str,
    "holderToken": str,
    "number": str,
    "csc": str,
    "bin": str,
    "numberToken": str,
    "numberLength": int,
    "cscToken": str,
    "cscLength": int,
    "expiration": {
      "month": str,
      "year": str
      }
    ,
    "document": str,
    "paymentOrigin":str,
    "cryptogram": str,
    "eci":str}
class miniCart(BaseModel):
  {
    "shippingValue": int,
    "taxValue": int,
    "buyer": {
      "id": str,
      "firstName": str,
      "lastName": str,
      "document": str,
      "documentType": str,
      "email": str,
      "phone": str,
      "isCorporate": bool,
      "corporateName": str,
      "tradeName": str,
      "corporateDocument": str,
      "createdDate": str
    },
    "shippingAddress": {
      "country": str,
      "street": str,
      "number": str,
      "complement": str,
      "neighborhood": str,
      "postalCode": str,
      "city": str,
      "state": str
    },
    "billingAddress": {
      "country": str,
      "street": str,
      "number": str,
      "complement": str,
      "neighborhood":str,
      "postalCode": str,
      "city": str,
      "state": str
    },
    "items": [
      {
        "id":str,
        "name": str,
        "price": float,
        "quantity": int,
        "discount": int,
        "deliveryType": str,
        "categoryId":str,
        "sellerId": str,
        "taxRate": float,
        "taxValue":float
      }
    ]
  }

class recipients(BaseModel):
    [
    {
      "id": str,
      "name": str,
      "documentType": str,
      "document": str,
      "role": str,
      "chargeProcessingFee": bool,
      "chargebackLiable": bool,
      "amount": float,
      "comissionAmount": int
    }
  ] 
class merchantSettings(BaseModel):
  [
    {
      "name": str,
      "value": int
    }
  ]
class data(BaseModel):
   {
     "reference": str,
     "orderId":str,
     "shopperInteraction":str,
    "verificationOnly": bool,
    "transactionId":str,
    "paymentId":str,
    "paymentMethod":str,
    "paymentMethodCustomCode":str,
    "merchantName":str,"value":float,
    "referenceValue":float,"currency":str,
    "installments":int,
    "installmentsInterestRate":int,
    "installmentsValue":float,
    "deviceFingerprint":str,
    "ipAddress":str,
    card:card,
    miniCart: miniCart,
    recipients:recipients,
    merchantSettings:merchantSettings,
    "url":str,"inboundRequestUrl":str,
    "secureProxyUrl":str,
    "sandBoxMode":bool,
    "totalCartValue":float,
    "callbackUrl":str,
    "returnUrl":str 
   }
class forsettle(BaseModel):
   {
  "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
  "requestId": "2019-02-04T22:53:42-40000",
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91",
  "value": 45,
  "authorizationId": "5784589",
  "tid": "5784589",
  "recipients": [
    {
      "id": str,
      "name": str,
      "documentType": str,
      "document": str,
      "role": str,
      "chargeProcessingFee": bool,
      "chargebackLiable": bool,
      "amount": float
    },
    {
      "id": str,
      "name": str,
      "documentType": str,
      "document": str,
      "role":str,
      "chargeProcessingFee": bool,
      "chargebackLiable": bool,
      "amount": float,
      "commissionAmount": float
    }
  ]
  }
class forrefund(BaseModel):
   {
  "requestId": str,
  "settleId": str,
  "paymentId": str,
  "tid": str,
  "value": int,
  "transactionId": str,
  "recipients": [
    {
      "id": str,
      "name": str,
      "documentType": str,
      "document": str,
      "role": str,
      "amount": float
    },
    {
      "id": str,
      "name":str,
      "documentType": str,
      "document":str,
      "role": str,
      "amount": float,
      "comissionAmount": int
    }
  ]
}
  