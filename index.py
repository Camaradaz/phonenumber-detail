import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phoneNumber = phonenumbers.parse("+541137176033")

timeZone = timezone.time_zone_for_number(phoneNumber)

Carrier = carrier.name_for_number(phoneNumber,'en')

Region = geocoder.description_for_number(phoneNumber,'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)

