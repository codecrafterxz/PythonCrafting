
print("welcome to my ciphermessenger ")      
alphabet = ['A' ,'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p','q', 'r',
   's', 't', 'u', 'v','w', 'x', 'y', 'Z','A', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p','q', 'r',
   's', 't', 'u', 'v','w', 'x', 'y', 'Z']
direction = input("type encode for encypt and decode for decrypt : ")
text = input("type your message").lower()
shift = int(input("tye number for shift :"))
def ciphertext(plaintext,shiftamount):
    if direction == "encode":
        ciphertext = ""
        for i in plaintext:
            position = alphabet.index(i)
            newposition = position + shiftamount
            newletter = alphabet[newposition]
            ciphertext += newletter
        print(f"your encode is {ciphertext}")
    elif direction == "decode":
        ciphertext1 = ""
        for i in plaintext:
            position = alphabet.index(i)
            newposition = position - shiftamount
            newletter = alphabet[newposition]
            ciphertext1 += newletter
        print(f"the decode is {ciphertext1}")
    else :
        ("please tell what you want ,do you want to encode your message or decode your message")
ciphertext(text,shift)