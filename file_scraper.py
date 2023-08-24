import numpy as np
import re 
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression

class file_scraper:
    dates_indep = []
    charge_dep = []

    def __init__(self,file_name):
        file_text = open_file("battery-report.html")
        table_text = find_table(file_text, "Battery capacity history")
        dates_indep = get_date(table_text)
        charge_indep = get_mwh(table_text)

    def get_numbers_only(input_string, mode): 
        '''Used to filter megawatt hours and date and TIME from the html code'''
        if mode == "date":
            mode_code = r'\b\d{4}-\d{2}-\d{2}\b'
        elif mode == "mwh":
            mode_code = r'[\d,]+'
        else: 
            return "incorrect code, please check"

        match = re.search(mode_code, input_string)
        #Check if a match was found
        if match:
            #Remove commas from the matched string and convert it to an integer
            number = match.group().replace(',', '')
            return number
        else:
            print("No number found in the input string.")

    ##################################################################################################################

    def open_file(filename):
        '''opens the file and scrapes all the content'''
        file_object = open(filename, "r")
        html_data = file_object.read()
        file_object.close()
        data = BeautifulSoup(html_data, 'html.parser')
        return data

    def find_table(htmldata, target_text):
        '''locates and returns the appropriate table using target_text parameter'''
        h2_element = htmldata.find("h2", string=lambda text: text and text.strip() == target_text) 
        #addresses the issue of exact matching by stripping the whitespaces and \ns near the target string"

        if h2_element:
            #gets everything between <h2>Heading 2A</h2> and <h2>Heading 2B</h2>
            content = []

            #starts from the next element after the <h2>Heading 2A</h2>
            current_element = h2_element.find_next_sibling()

            while current_element and current_element.name != 'h2':
                content.append(str(current_element))
                current_element = current_element.find_next_sibling()

        # joins the content
            result = '\n'.join(content)
            return result
        else:
            return f"didnt find with {target_text} sed :()"



    def get_date(table, dates_indep):
        '''returns a list of dates provided in the table column'''
        dates = table.find_all("td", class_ = "dateTime") 

        if dates:

            dates_list = []
        
        for date in dates:
            filtered_date = date.prettify()
            dates_list.append(get_numbers_only(filtered_date,"date"))

        else: 
            return "not found the mw class... please double check"

        return dates_list

    def get_mwh(table, charge_dep):
        '''returns a list of megawatthours left(capacity) provided in the table column'''
        table = BeautifulSoup(result,"html.parser")
        charge_capacity_all = table.find_all("td", class_ = "mw")#contains the other column("Original Charge")

        #table.find_all("td", class_ = "dateTime") the dates are in week times and then rest in single days(not a full week)
        if charge_capacity_all:
        
            charge_capacity_new = charge_capacity_all[::2]#with the other column removed

            charge_capacity_list = []
        
            for charge in charge_capacity_new:
                mwh = charge.prettify()
                charge_capacity_list.append(get_numbers_only(mwh,"mwh"))

        else: 
            return "not found the mw class... please double check"


        return charge_capacity_list
    
    def return_date():
        return dates_indep
    def return_charge():
        return charge_indep
        

    