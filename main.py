import pytesseract  as tess
from PIL import Image
import re 
import json

aadharInfo = {}
aadharInfo["number"] = ""
aadharInfo["dob"] =""
tess.pytesseract.tesseract_cmd = r"C:\Users\Dell\AppData\Local\Tesseract-OCR\tesseract.exe"
fourDigitNumberPattern = "\d{4}"
datePattern =  "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
img = Image.open("aadhar_test.jpg")
text = tess.image_to_string(img)

array = text.split()
count=0
for index in reversed(range(len(array))):
    token = re.search(fourDigitNumberPattern, array[index])
    if token:
        aadharInfo["number"] += token.group() 
        count+=1
    if count==3:
        break

for index in reversed(range(len(array))):
    token = re.search(datePattern, array[index])
    # print(array[index])
    if token:
        aadharInfo["dob"] = token.group()
        break

for index in reversed(range(len(array))):
    if("MALE" in array[index] or "FEMALE" in array[index]):
        aadharInfo["gender"]=array[index]
        break

trial = text.split("\n")


numberPattern = r'[0-9]'

# Match all digits in the string and replace them with an empty string
name= re.sub(numberPattern, '', trial[3])
aadharInfo["name"] = name

maskedNumber = "********"+aadharInfo["number"][8:len(aadharInfo["number"])]
# print(maskedNumber)
aadharInfo["number"]= maskedNumber
json_object = json.dumps(aadharInfo, indent = 4) 
print(json_object)
# print(aadharInfo)