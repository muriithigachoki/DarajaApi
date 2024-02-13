import requests


from access_token import register_access_token
from encode import generate_password
from formatting import formatted_time
import keys


formatted_time = formatted_time()


def lipa_na_mpesa():

    access_token = register_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % access_token,
    }

    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": generate_password(formatted_time),
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": 174379,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "Kangai Poultry",
        "TransactionDesc": "Payment of one day chicks",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
