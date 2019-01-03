while True:
    try:
        num1 = int(input("첫번째 숫자를 입력하세요: "))
        break
    except ValueError:
        print("숫자를 입력하시오.")

while True:
    try:
        num2 = int(input("두번째 숫자를 입력하세요: "))
        break
    except ValueError:
        print("숫자를 입력하시오.")

if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp
    # num1, num2 = num2, num1

temp_num1 = num1
temp_num2 = num2

while temp_num2 != 0:
    rem = temp_num1 % temp_num2
    temp_num1 = temp_num2
    temp_num2 = rem

great_div = temp_num1
least_multi = int((num1 * num2) / great_div)

print("최대공약수:", great_div, "최소공배수:", least_multi)