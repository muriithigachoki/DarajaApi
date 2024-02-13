import requests


from access_token import register_access_token
import keys


def register_urls():

    access_token = register_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % access_token,
    }

    request = {
        "ShortCode": keys.short_code,
        "ResponseType": "Complete",
        "ConfirmationURL": "https://kangaipoultry.com/confirmation",
        "ValidationURL": "https://kangaipoultry.com/validation_url",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


register_urls()


def c2b_transactions():
    access_token = register_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % access_token,
    }

    request = {
        "ShortCode": keys.short_code,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": keys.msisdn_test,
        "BillRefNumber": "29834568",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


c2b_transactions()
