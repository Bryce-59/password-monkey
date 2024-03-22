import hash

#HASH (bytes) encoded string -> (bytes) hash
HASH = hash.sha512

#HASH_COMBINE (bytes, bytes) hash, encoded string -> (bytes) hashcombine
HASH_COMBINE = hash.boost_hashcombine