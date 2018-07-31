

# noinspection SpellCheckingInspection
def make_keys(key_path):
    # paths
    openssl = ""
    private_key_pem = key_path + "/private_key.pem"
    public_key_pem = key_path + "/public_key.pem"
    private_key_der = key_path + "/private_key.der"
    public_key_der = key_path + "/public_key.der"

    # commands
    print("openssl genrsa -out \"" + private_key_pem + "\" 2048")
    print("openssl pkcs8 -topk8 -inform PEM -outform DER -in \"" + private_key_pem + "\" -out \"" + private_key_der + "\" -nocrypt")
    print("openssl rsa -in \"" + private_key_pem + "\" -pubout -outform DER -out \"" + public_key_der + "\"")
    print("openssl rsa -in \"" + private_key_pem + "\" -pubout -outform PEM -out \"" + public_key_pem + "\"")


def pad(text, buffer_size):
    number_of_blank_space = buffer_size - len(text) % buffer_size
    character_by_that_value = chr(number_of_blank_space)
    filler = number_of_blank_space * character_by_that_value
    return text + filler


def unpad(text, buffer_size):
    last_char = text[len(text) - 1:]
    number_of_blank_space = ord(last_char)
    length_of_text = buffer_size - number_of_blank_space
    removed_filter = text[:length_of_text]
    return removed_filter
