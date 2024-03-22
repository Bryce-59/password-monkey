from variables import HASH, HASH_COMBINE

def generate_password (security_code : bytes, ciphertext : str):
    """Generate a new password given a ciphertext and a security code.
    
    Args:
    security_code (bytes) : a hash used to scramble the ciphertext 
      ciphertext (str) : used to generate a password

    Returns:
      password (str) : a string of valid ASCII characters for use as a password

    Raises:
      TypeError : bad parameter format
    """
    
    # precondition
    if type(ciphertext) is not str or type(security_code) is not bytes :
        raise TypeError("Invalid type")

    # code body
    raw = HASH_COMBINE(security_code, ciphertext.encode(), hash_function = HASH)
    pw = HASH(raw)
    return transcribe(pw)[:32]

def transcribe(pw : bytes):
    """Transcribe a bytes object into a string of valid ASCII characters (33-126).
    
    Args:
      pw (bytes) : a bytes object

    Returns: 
      result (str) : a string of valid ASCII characters

    Raises:
      TypeError : bad parameter format
    """

    # precondition
    if type(pw) is not bytes :
        raise TypeError("Invalid type")

    # code body
    result = ""
    for byte in pw:
        result += chr(int((93 * byte / 256) + 33))
    return result



def main():
    ct = input("Password: ")
    sc = input("Security Code: ")
    print(generate_password(HASH(sc.encode()), ct))

if __name__ == "__main__":
    main()