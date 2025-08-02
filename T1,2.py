import ast

#YO ,this class is like our secret F1 radio protocol ._.
#It packs a bunch of commands into one str >> encode
#And unpacks them perfectly on the other side >> decode

class Codec:
    def encode(self ,list_of_commands):
        return ''.join(f"{len(cmd)}#{cmd}"for cmd in list_of_commands)
    
    #Take that mega string and split it back to the OG list

    def decode(self ,encoded_string):
        i=0
        decoded_list=[]
        while i<len(encoded_string):

            #Find where the len ends >> before '#'

            j=i
            while encoded_string[j] != '#':
                j+=1
            l=int(encoded_string[i:j])
            cmmd=encoded_string[j+1:j+1+l]
            decoded_list.append(cmmd)
            i=j+1+l
        return decoded_list


#MAIN

if __name__=="__main__":
    c=Codec()     

    #INPUT
    inP=input("INPUT : ")   

    #Convert the input
    cmmd=ast.literal_eval(inP)

    #Encode that baby
    en=c.encode(cmmd)

    #Decode it back
    de=c.decode(en)

    print("OUTPUT : " ,de)   