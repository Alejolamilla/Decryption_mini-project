
import os

def private_key():

    try:
        private_key = int(input('Set the private key: '))
        public_key = int(input('Set the FIRST public key: '))
    except:
        print('\n Something was wrong :/ be sure that both keys does not have letter, dots or another symbol')
        private_key, public_key, encrypted_message = private_key()

    try:
        encrypted_message = str(input('Encrypted message: '))
    except:
        print('\n Something was wrong :/ verify your encrypted message and try again')
        private_key, public_key, encrypted_message = private_key()

    return private_key, public_key, encrypted_message
#_____________________________________________________________________________________________________________________________________
# if the encription has any specific separator use this function
def separate_code(encrypted_message):

    separator_list = ['a','A','b','B','c','C','d','D','>','<',':','*','-','+','%','@','&',';']
    new_message = encrypted_message

    for separator in separator_list:
        new_message = new_message.replace(separator, ',')

    message = new_message.split(',')
    message.remove('')

    return message

#_____________________________________________________________________________________________________________________________________

def decryption(privated_key,public_key, message):

    letters_code = {1:'z', 2:'y', 3:'x', 4:'w', 5:'v', 6:'u', 7:'t', 8:'s', 9:'r', 10:'q', 11:'p', 12:'o', 13:'ñ', 14:'n',
                    15:'m', 16:'l', 17:'k', 18:'j', 19:'i', 20:'h', 21:'g', 22:'f', 23:'e', 24:'d', 25:'c', 26:'b', 27:'a', 28:' '}

    Decoding_message = []
    final_message = ''
    for letter in message:
        dec_number = (int(letter)**int(privated_key))%int(public_key)
        to_letter = letters_code[dec_number]
        final_message += to_letter

    return final_message

#_____________________________________________________________________________________________________________________________________
if __name__ == '__main__':

    print('\n RSA DECRYPTION CODE \n Set the private key (only numbers) and the encrypted message')
    privated_key, public_key, encrypted_message = private_key()
    message = separate_code(encrypted_message)
    final_message = decryption(privated_key, public_key, message)

    print('your message is: {}'.format(final_message))
    os.system('pause')