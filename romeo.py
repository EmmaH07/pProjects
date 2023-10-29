"""
Author: Emma Harel
Date: 07/10/23
Description: encrypting or decrypting a message based on parameter in sys.argv
"""
import sys
import logging

logging.basicConfig(filename='romeo.log', level=logging.DEBUG)

ENCRYPT_DICT = {
    "A": 56, "B": 57, "C": 58, "D": 59, "E": 40,
    "F": 41, "G": 42, "H": 43, "I": 44, "J": 45,
    "K": 46, "L": 47, "M": 48, "N": 49, "O": 60,
    "P": 61, "Q": 62, "R": 63, "S": 64, "T": 65,
    "U": 66, "V": 67, "W": 68, "X": 69, "Y": 10,
    "Z": 11, "a": 12, "b": 13, "c": 14, "d": 15,
    "e": 16, "f": 17, "g": 18, "h": 19, "i": 30,
    "j": 31, "k": 32, "l": 33, "m": 34, "n": 35,
    "o": 36, "p": 37, "q": 38, "r": 39, "s": 90,
    "t": 91, "u": 92, "v": 93, "w": 94, "x": 95,
    "y": 96, "z": 97, " ": 98, ",": 99, ".": 100,
    ";": 101, "'": 102, "?": 103, "!": 104, ":": 105
}

DECRYPT_DICT = {
    56: "A", 57: "B", 58: "C", 59: "D", 40: "E",
    41: "F", 42: "G", 43: "H", 44: "I", 45: "J",
    46: "K", 47: "L", 48: "M", 49: "N", 60: "O",
    61: "P", 62: "Q", 63: "R", 64: "S", 65: "T",
    66: "U", 67: "V", 68: "W", 69: "X", 10: "Y",
    11: "Z", 12: "a", 13: "b", 14: "c", 15: "d",
    16: "e", 17: "f", 18: "g", 19: "h", 30: "i",
    31: "j", 32: "k", 33: "l", 34: "m", 35: "n",
    36: "o", 37: "p", 38: "q", 39: "r", 90: "s",
    91: "t", 92: "u", 93: "v", 94: "w", 95: "x",
    96: "y", 97: "z", 98: " ", 99: ",", 100: ".",
    101: ";", 102: "'", 103: "?", 104: "!", 105: ":"
}


def encryption(msg):
    """
    input: a massage to encrypt
    output: a string containing the encrypted message
    encrypts a message based on the encryption dictionary
    """
    if msg == "":
        encrypted_msg = ""
    else:
        encrypted_msg = ""
        for char in msg:
            encrypted_msg += str(ENCRYPT_DICT[char]) + ","

        encrypted_msg = encrypted_msg[:-1]
    logging.debug("message inputted: " + msg + " message encrypted: " + encrypted_msg)
    return encrypted_msg


def decryption(encrypted_msg):
    """
    input: an encrypted message
    output: a string containing the decrypted message
    decrypts a message based on the decryption dictionary
    """
    if encrypted_msg == "":
        decrypted_msg = ""
    else:
        num_array = encrypted_msg.split(",")
        decrypted_msg = ""
        for item in num_array:
            decrypted_msg += str(DECRYPT_DICT[int(item)])

    logging.debug("encrypted message: " + encrypted_msg + " decrypted message : " + decrypted_msg)
    return decrypted_msg


def put_in_file(msg):
    """
    input: a massage to put in a file
    puts a string in encrypted_msg.txt file
    """
    try:
        with open('./encrypted_msg.txt', 'w') as f:
            f.write(msg)
    except IOError:
        logging.error("IOError")
        print("error while trying to open the file")


def get_from_file():
    """
    output: a string containing the encrypted message
    gets the string from encrypted_msg.txt file
    """
    try:
        with open('./encrypted_msg.txt', 'r') as f:
            msg = f.read()
            return msg
    except FileNotFoundError:
        logging.error("File not found")
        print("File not found")


def check():
    assert encryption("My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I "
                      "have, for both are infinite.") == ("48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,"
                                                          "35,15,33,16,90,90,98,12,90,98,91,19,16,98,90,16,12,99,98,"
                                                          "48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,"
                                                          "16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19,"
                                                          "16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,19,12,93,16,"
                                                          "99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,"
                                                          "35,30,91,16,100")
    assert encryption("Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers' eyes; "
                      "Being vexed a sea nourish'd with loving tears: What is it else? a madness most discreet, "
                      "A choking gall, and a preserving sweet.") == ("47,36,93,16,98,30,90,98,12,98,90,34,36,32,16,98,"
                                                                     "39,12,30,90,16,15,98,94,30,91,19,98,91,19,16,"
                                                                     "98,17,92,34,16,98,36,17,98,90,30,18,19,90,101,"
                                                                     "98,57,16,30,35,18,98,37,92,39,18,16,15,99,98,"
                                                                     "12,98,17,30,39,16,98,90,37,12,39,32,33,30,35,"
                                                                     "18,98,30,35,98,33,36,93,16,39,90,102,98,16,96,"
                                                                     "16,90,101,98,57,16,30,35,18,98,93,16,95,16,15,"
                                                                     "98,12,98,90,16,12,98,35,36,92,39,30,90,19,102,"
                                                                     "15,98,94,30,91,19,98,33,36,93,30,35,18,98,91,"
                                                                     "16,12,39,90,105,98,68,19,12,91,98,30,90,98,30,"
                                                                     "91,98,16,33,90,16,103,98,12,98,34,12,15,35,16,"
                                                                     "90,90,98,34,36,90,91,98,15,30,90,14,39,16,16,"
                                                                     "91,99,98,56,98,14,19,36,32,30,35,18,98,18,12,"
                                                                     "33,33,99,98,12,35,15,98,12,98,37,39,16,90,16,"
                                                                     "39,93,30,35,18,98,90,94,16,16,91,100")
    assert encryption("I love cyber!") == "44,98,33,36,93,16,98,14,96,13,16,39,104"
    assert encryption("") == ""
    assert decryption("59,36,35,102,91,98,94,12,90,91,16,98,96,36,92,39,98,33,36,93,16,98,36,35,98,90,36,34,16,13,36,"
                      "15,96,99,98,94,19,36,98,15,36,16,90,35,102,91,98,93,12,33,92,16,98,30,91,100") == ("Don't waste "
                                                                                                          "your love "
                                                                                                          "on "
                                                                                                          "somebody, "
                                                                                                          "who "
                                                                                                          "doesn't "
                                                                                                          "value it.")
    assert decryption("48,96,98,36,35,33,96,98,33,36,93,16,98,90,37,39,92,35,18,98,17,39,36,34,98,34,96,98,36,35,33,"
                      "96,98,19,12,91,16,104,98,65,36,36,98,16,12,39,33,96,98,90,16,16,35,98,92,35,32,35,36,94,35,99,"
                      "98,12,35,15,98,32,35,36,94,35,98,91,36,36,98,33,12,91,16,104,98,61,39,36,15,30,18,30,36,92,90,"
                      "98,13,30,39,91,19,98,36,17,98,33,36,93,16,98,30,91,98,30,90,98,91,36,98,34,16,98,65,19,12,91,"
                      "98,44,98,34,92,90,91,98,33,36,93,16,98,12,98,33,36,12,91,19,16,15,98,16,35,16,34,96,"
                      "100") == ("My only love sprung from my only hate! Too early seen unknown, and known too late! "
                                 "Prodigious birth of love it is to me That I must love a loathed enemy.")
    assert decryption("49,30,39,98,18,30,93,16,98,34,16,98,12,98,19,92,35,15,39,16,15") == "Nir give me a hundred"
    assert decryption("") == ""


def main():
    if "encrypt" in sys.argv:
        msg = input("please enter a message: ")
        new_msg = encryption(msg)
        put_in_file(new_msg)

    elif "decrypt" in sys.argv:
        encrypted_msg = get_from_file()
        if encrypted_msg is not None:
            dec_msg = decryption(encrypted_msg)
            print(dec_msg)
        else:
            print("file not found")


if __name__ == "__main__":
    check()
    main()
