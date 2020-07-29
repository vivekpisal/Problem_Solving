import phonenumbers

from phonenumbers import geocoder
number=+919987770322
ch_number=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_number,'en'))