x = input("Give x?")
print "You have put this in: ", x

y = input("Give y?")
print "You have put this in: ", y

z = raw_input("Give operation")
while True:
 if z == "+":
  print x+y
  break
 if z == "-":
  print x-y
  break
 if z == "*":
  print x*y
  break
 if z == "/":
  print x/y
  break
 else:
  print('plz give a proper operator')
  break
