digit = { 0:"",1:" thousand ",2:" million ",3:" billion ",4:" trillion "}
ones = {
    0:" ",
    1:" one ",
    2:" two ",
    3:" three ",
    4:" four ",
    5:" five ",
    6:" six ",
    7:" seven ",
    8:" eight ",
    9:" nine ",
}
decades = {
    0:" ",
    1:" ten ",
    2:" twenty ",
    3:" thirty ",
    4:" forty ",
    5:" fifty ",
    6:" sixty ",
    7:" seventy ",
    8:" eighty ",
    9:" ninety ",
}
text = input("Type your number here: ")
# text = "7,968,852,741"
text = text.replace(",","").replace(".","")

while len(text)%3 != 0:
    text = "0" + text
# # 007968852741
# 741     852    968     007
listt = []
for i in range(0,len(text)//3):
    parca = text[i*3:(i*3)+3]
    listt.insert(0,parca)
print(listt)
# ['741', '852', '968', '007']
lastresult = ""
step = 0
for item in listt:
    expression = item
    result = ""
    if int(expression[0]) != 0: # hundreds 7
        if int(expression[0]) != 1: # hundres 7
            result = ones[int(expression[0])]+" hundred "
        else:
            result = " hundred "
    result += decades[int(expression[1])]  # decades 4
    result += ones[int(expression[2])] # ones 1
    result += digit.get(step)
    lastresult = result + lastresult
    step += 1
print(lastresult)