#The reason why I didn't do this class normally is a lack of docs for this lib
import phonenumbers


class PhoneConverter:
    def __init__(self, phone_to_convert: str, country=None):
        self.phone_to_convert = phone_to_convert
        self.country = country
        self.Parser = phonenumbers.parse(self.phone_to_convert, self.country)

    def GetCountryCode(self) -> str:
        if not self.country:
            return phonenumbers.phonenumberutil.region_code_for_country_code(
                self.Parser.country_code)

        return self.country

    def IsPhoneNumberExists(self) -> bool:
        return phonenumbers.is_valid_number(self.Parser)

    def GetConvertedPhoneNumber(self) -> str:
        return phonenumbers.format_number(self.Parser,
                                          phonenumbers.PhoneNumberFormat.E164)
    