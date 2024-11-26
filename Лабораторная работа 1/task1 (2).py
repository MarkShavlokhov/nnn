numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum = 0
for i in range(len(numbers)):
    if numbers[i] != None:
        sum += numbers[i]
sr = sum/len(numbers)
sr= f"{sr:.2f}"
numbers[4]=float(sr)

print("Измененный список:", numbers)
