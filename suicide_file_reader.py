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


