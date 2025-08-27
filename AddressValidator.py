def email(address):
  dot=address.find(".")
  at=address.find("@")
  while True:
    if (dot==-1):
      print("Invalid Email Address")
    elif (at==-1):
      print("Invalid Email Address")
    else:
      print("This is a valid email address")
      break
email("prathameshmore792gmail.com")

