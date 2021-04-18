import validate_email


class EmailValidater:
    @staticmethod
    def IsEmailExists(email_to_check: "") -> bool:
        return validate_email.validate_email(email_to_check, verify=True)
