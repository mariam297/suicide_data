from suicide_file_reader import BudgetFileReader

reader = BudgetFileReader("suicide_rate_data.xlsx")   #make an instance
x = reader.print_all_cell_data()

def suicide_no(entry):
    return entry[4]

def top(year, number):
    print("Top suicide rates: ")
    list1 = sorted(x[1:], key = suicide_no, reverse=True)
    counter = 0
    for row in list1:
        if counter < number:
            if row[1] == year:
                print(row)
                counter += 1


def gender(entry):
    return entry[3]

def compare_gender(country, year, age):
    print("Comparing suicide rates and genders")
    male_suicide_no = 0
    female_suicide_no = 0
    for row in x[1:]:
        if row[0] == country:
            if row[1] == year:
                if row[3] == age:
                    if row[2] == "male":
                        male_suicide_no = row[4]
                        print(row)
                    else:
                        female_suicide_no = row[4]
                        print(row)
    if male_suicide_no > female_suicide_no:
        print("Male suicide is higher than female suicide!")
    elif female_suicide_no < male_suicide_no:
        print("Female suicide is  higher than male suicide!")
    else:
        print("The entries you have entered does not exist!")


def average_suicide(year):
    print("Average suicide number:")
    total_suicide_no = 0     #Set to zero in order to compute a calculation
    number_of_countries = 0
    for column in x[1:]:
        if column[1] == year:
            if column[4] != 0:
                total_suicide_no += column[4]
                number_of_countries += 1
    average_suicide_no = total_suicide_no/number_of_countries
    average_suicide_no = round(average_suicide_no)
    print(average_suicide_no)


def population(entry):
    return entry[5]

def percentage_of_suicide_no(country, year, gender, age):
    print("Percentage of suicide rates")
    suicide_number = 0
    population = 0
    for row in x[1:]:
        if row[0] == country:
            if row[1] == year:
                if row[2] == gender:
                    if row[3] == age:
                        suicide_number = row[4]
                        population = row[5]
                        print(row)
    suicide_values = (suicide_number/population) * 100
    suicide_values = round(suicide_values, 5)

    print("{:.5f}%".format(suicide_values))