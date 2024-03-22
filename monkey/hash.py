import hashlib

def sha512 (var : bytes):
    """Generate the sha256 hash of a bytes object
    
    Args:
      var (bytes) : the bytes object

    Returns:
      hash (bytes) : the sha256 hash

    Raises:
      TypeError : bad parameter format
    """

    #precondition
    if type(var) is not bytes:
        raise TypeError("Invalid type")

    #code body
    return hashlib.sha512(var).digest()

def boost_hashcombine (seed : bytes, var : bytes, hash_function = None):
    """Combine a hash and a value to create a new hash,
    
    Based on the boost::hash_combine function, see below-
    https://www.boost.org/doc/libs/1_55_0/doc/html/hash/reference.html#boost.hash_combine

    Args:
      seed (bytes) : the hash to combine with the value
      var (bytes) : the value to combine with the hash

    Returns:
      hashcombine (bytes) : the boost::hashcombine hash

    Raises:
      TypeError : bad parameter format
    """

    #precondition
    if type(seed) is not bytes or type(var) is not bytes:
        raise TypeError("Invalid type")

    #code body
    max_length = len(seed)
    max_value = 2**(8*max_length)

    seed = int.from_bytes(seed)

    seed ^= (int.from_bytes(hash_function(var)) + 0x9e3779b9 + (seed<<6) + (seed>>2)) % max_value
    return (seed % max_value).to_bytes(max_length)