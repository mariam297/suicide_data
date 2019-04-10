from openpyxl import load_workbook


class BudgetFileReader:
    def __init__(self, file_name_and_path):
        self.workbook = load_workbook(file_name_and_path, read_only=True)
        self.worksheet = self.workbook.active

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def print_all_cell_data(self):
        list = []
        for i in self.worksheet.values:
            list.append(i)
        return list

    def print_all_data_cells_coordinates(self):
        for i in self.worksheet.rows:
            for p in i:
                print(p.coordinate)


reader = BudgetFileReader("suicide_rate_data.xlsx")   #make an instance
x = reader.print_all_cell_data()  #running the method

# print("Top 10 suicide rates:")
# print("-----------------------")
# for column in x[1:]:
#     if column[0] <= 10:
#         print(column[1] + " " + str(column[2]) + " " + str(column[4]) + " " + str(column[5]))
#
# print("Lowest 10 suicide rates:")
# print("-------------------------")
# for column in x[1:]:
#     if column[0] >= 27811:
#         if column[5] != 0:
#             print(column[1] + " " + str(column[2]) + " " + str(column[4]) + " " + str(column[5]))

def suicide_no(entry):
    return entry[4]

def population(entry):
    return entry[5]

list2 = sorted(x[1:], key= population)


def top_10(year, number):
    list1 = sorted(x[1:], key=suicide_no, reverse=True)
    counter = 0
    for row in list1:
        if counter < number:
            if row[1] == year:
                print(row)
                counter += 1


top_10(1995, 1)




#
# for item in x[1:]:
#     if item[0] >= 214:
#         print(item[1] + " " + str(item[2]))
#
#
# total_life_expectancy = 0                #Set to zero because we are doing some calculation on it so it needs to have a value
# number_of_countries = 0
# for item in x[1:]:                #the [1:] does not take into account headers. The item shows the row of the excel file
#     total_life_expectancy += item[2]    #add each cell in column 3(life expectancy)
#     number_of_countries += 1            #adds the total number of countries
# average_life_expectancy = total_life_expectancy/number_of_countries
#
#
# print("-----------------------------------")
# print("Average Life expectancy")
# print("-----------------------------------")
# print(average_life_expectancy)
#
# def country_and_life_expectancy(rank):
#     for item in x[1:]:
#         if item[0] == rank:         #The item is a tuple because you cant change or add values whereas in a list you can. The [0] represents the first column which is rank in execel file
#             print(item[1] + " " + str(item[2]))  #the item[1] means printing the 2nd column (country) and item[2] means printing third column (life expectancy)
#
# print("                             ")
# print("Rank:")
# country_and_life_expectancy(6)