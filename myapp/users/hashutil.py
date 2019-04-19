from hashlib import sha256
from random import choice
from string import ascii_letters

'''Generating a random string of size 5'''
def makeSalt():
    return ''.join([
        choice(ascii_letters) for x in range(5)
        ])

'''Generate a hash for the password'''
def makeHash(password, salt = None):
    if salt==None: salt = makeSalt()
    hash = sha256(str.encode(password+salt)).hexdigest()
    return '{0},{1}'.format(hash, salt)

'''Check password from a given hash'''
def checkHash(password, hash):
    salt = hash.split(',')[1]
    if makeHash(password, salt)==hash:
        return True
    return False

if __name__ == '__main__':
    print(makeHash('root'))

