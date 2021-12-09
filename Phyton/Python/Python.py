import requests
import json
import urllib.request
from pprint import pprint
url = "https://apiecommerce.pagosinteligentes.com:8070/CheckOut/MethodGenerateTransaction"
values={
"generateTransaction": {
    "security": {
      "accountId": 30414,
      "token": "OTalRWWPXzpIyBAst88$"
    },
    "infoPayment": {
      "amount": 1000,
      "tax": 0,
      "description": "Prueba Swagger",
      "toolId": 5,
      "registryToolId": 0,
      "currency": "COP"
    },
    "infoClient": {
      "name": "Pagos Inteligentes",
      "idType": "CC",
      "idNumber": "123456789",
      "email": "comprobantes@pagosinteligentes.com",
      "phone": "573213285290"
    },
    "infoAdditional": {
      "disabledPaymentMethod": "20,21,24",
      "infoAdditional": 0,
      "urlResponseOk": "https://sag.pagosinteligentes.com:8140/",
      "urlResponseFail": "https://sag.pagosinteligentes.com:8140/",
      "urlResponsePending": "https://sag.pagosinteligentes.com:8140/",
      "urlNotificationPost": "https://sag.pagosinteligentes.com:8140/",
      "photo": "https://dl.dropboxusercontent.com/s/jghrtm678do5fts/carrito.jpg?dl=0",
      "cashDiscount": 100,
      "expiredCashDiscount": "2021/12/31",
      "deliveryAddres": True,
      "ammountShipping": 0
    }
  }
}
headers = {    
    "Content-Type": "application/json",
    "Accept": "application/json",
    }

data = json.dumps(values).encode("utf-8")
pprint(data)

try:
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as f:
        res = f.read()
    pprint(res.decode())
except Exception as e:
    pprint(e)
