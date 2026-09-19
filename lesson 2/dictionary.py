contact_info = {"Enes":"444-4321",
                "erlind":"555-555",
                }

enes_phone = contact_info["Enes"]
erlind_phone = contact_info["erlind"]
print(enes_phone)
print(erlind_phone)

contact_info["Enes"] = "444-7891" #set
print(contact_info)

contact_info["Elvis"] = "444-7777"
print(contact_info)

del contact_info["erlind"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {"Enes":{
    "phone_number":"123-5678",
    "email":"enes@gmail.com",
    "home_address":"123 street,tiran",
    "birthday":"02/04/2002"
},"Elvis":{
    "phone_number":"123-7777",
    "email":"elvis@gmail.com",
    "home_address":"123 street",
    "birthday":"02/04/2010"
},}

print(contact_information)

elvis_information = contact_information["Elvis"]
print(elvis_information)