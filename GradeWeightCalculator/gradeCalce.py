
def main():
    #grades_list = [100, 100, 88, 72, 90, 91, 95, 89, 100]
    grades_list = [82, 90, 76]
    #weights_list = [20, 20, 10, 20, 20, 30, 10, 10, 10]
    weights_list = [20, 35, 45]
    wgt_factor = []

    if len(grades_list) == len(weights_list):
        for i in range(len(grades_list)):
            grade = grades_list[i]
            weight = weights_list[i]
            fac = grade * (weight / 100)
            wgt_factor.append(fac)
    else:
        print('Error')

    average = sum(wgt_factor)
    print(format(average, '.2f'))
main()
