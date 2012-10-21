def lowerChar(char):
   if ord(char) >= 65 and ord(char) <= 90:
      return chr(ord(char) + 32)
   else:
      return char
      
def lowerString(string):
   x = ""
   for i in range(0, len(string)):
      x = x + lowerChar(string[i])
   return x
   
x = input('The text you put in here will be returned in lower index characters: ')
print(lowerString(x))