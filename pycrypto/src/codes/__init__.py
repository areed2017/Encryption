from encryption.RSA import encrypt as rsa_encrypt
from encryption.AES import decrypt as aes_decrypt


class DeactivationRequestCode:
    """
    RegistrationRequestCode


    Usage:
        GIVEN: When deactivating a license ( "api/ops/license/deactivation" )
        RECEIVED: Never
    """

    def __init__(self, hardware_id=None, registration_code=None):
        self.hardware_id = hardware_id
        self.registration_code = registration_code

    def encrypt(self):
        return rsa_encrypt(str(self))

    def __str__(self):
        return str(self.hardware_id) + "-" + str(self.registration_code)


class RegistrationCode:
    """
    RegistrationRequestCode


    Usage:
        GIVEN: Passed into a DeactivationRequestCode when it is being given to the api
        RECEIVED: As a response from registering
    """

    def __init__(self, aes_encrypted_string=None, hardware_id=None,
                 license_id=None, product_id=None, edition_id=None, model_type=None,
                 model_data=None, domain=None, user_control_type=None,
                 max_clients=None, max_workers=None, program_specific_function_limit_id=None):
        """
            Option1 : Give an aes encrypted string and Hardware id
            Option2: Build from everything else
        """
        if aes_encrypted_string is None:
            self.license_id = license_id
            self.product_id = product_id
            self.edition_id = edition_id
            self.model_type = model_type
            self.model_data = model_data
            self.domain = domain
            self.user_control_type = user_control_type
            self.max_clients = max_clients
            self.max_workers = max_workers
            self.program_specific_function_limit_id = program_specific_function_limit_id
        else:
            decrypted = aes_decrypt(aes_encrypted_string, hardware_id).str.split("-")
            self.license_id = decrypted[0]
            self.product_id = decrypted[1]
            self.edition_id = decrypted[2]
            self.model_type = decrypted[3]
            self.model_data = decrypted[4]
            self.domain = decrypted[5]
            self.user_control_type = decrypted[6]
            self.max_clients = decrypted[7]
            self.max_workers = decrypted[8]
            self.program_specific_function_limit_id = decrypted[9]

    def encrypt(self):
        return rsa_encrypt(str(self))

    def __str__(self):
        delimiter = "-"
        return str(self.license_id) + delimiter + str(self.product_id) + delimiter + \
               str(self.edition_id) + delimiter + str(self.model_type) + delimiter + str(self.model_data) + \
               delimiter + str(self.domain) + delimiter + str(self.user_control_type) + delimiter + \
               str(self.max_clients) + delimiter + str(self.max_workers) + delimiter + \
               str(self.program_specific_function_limit_id)


class RegistrationRequestCode:
    """
    RegistrationRequestCode


    Usage:
        GIVEN: to the api when registering ( "api/ops/license/regestration" )
        RECEIVED: Never
    """

    def __init__(self, hardware_id=None, pc_info=None):
        self.hardware_id = hardware_id
        self.pc_info = pc_info

    def encrypt(self):
        return rsa_encrypt(str(self))

    def __str__(self):
        return str(self.hardware_id) + "-" + str(self.pc_info)
