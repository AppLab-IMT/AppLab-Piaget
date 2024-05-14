def hasheando(password):
    HASH = "!AAUG!"
    pass_reverse = password[::-1]
    passA = HASH + pass_reverse + HASH
    return passA

def rainbow(hasheado, password_input):
    list_hash = hasheado.split("!AAUG!")
    hash_inverso = list_hash[1][::-1]  # Invertendo a hash para comparar corretamente
    if hash_inverso == password_input:
        return True
    else:
        return False
