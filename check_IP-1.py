import re
str1 = "155.255.256.0"
if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", str1):
  print ("确认是IP")
else:
    print('这不是IP')
