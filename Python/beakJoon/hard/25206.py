dictionary = {"A+" :4.5 ,"A0" : 4.0,"B+" : 3.5,"B0" : 3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}
denominator = 0
numerator = 0.0
for i in range(0,20):
    input_value = list(input().split())
    if(input_value[2]!="P"):
        denominator += float(input_value[1])
        numerator += float(input_value[1])*dictionary[input_value[2]]
print(numerator/denominator)