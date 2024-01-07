# bmi_calculator

def remark(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")


def bmi_calculator(units):
    wunit = ""
    hunit = ""
    if units == 1:
        wunit = "(kg)"
        hunit = "(m)"
    else:
        wunit = "(lbs)"
        hunit = "(feet)"
    print("Enter weight" + wunit + " and height" + hunit + ": ")
    weight, height = map(float, input().split())
    bmi = 0
    if units == 2:
        height = height * 12
        bmi = weight * 703 / height ** 2
    else:
        bmi = weight / height ** 2
    print("BMI: ", str(bmi)[0:5])
    remark(bmi)


if __name__ == "__main__":
    while True:
        choice = int(input("1)Calculate_BMI 2)Exit\nEnter choice: "))
        if choice == 1:
            units = int(input("Choose measurement Units:\n1)Metric 2)Imperial\n"))
            bmi_calculator(units)
        else:
            break
