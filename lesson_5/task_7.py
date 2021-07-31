import json


def line_parser(line):
    firm_str_data = line[line.find(' ') + 1:]
    firm_name = line[:line.find(' ')]
    firm_entity_type = firm_str_data[:firm_str_data.find(' ')]
    str_totals = firm_str_data[firm_str_data.find(' ') + 1:]

    firm_income = 0
    firm_costs = 0
    numeric_value = 0
    income_iterator = True
    numb = ''
    for i in str_totals:

        if i.isdigit():
            numb += i
        else:
            numeric_value = numeric_value + int(numb) if len(numb) > 0 else numeric_value
            numb = ''
            if income_iterator:
                firm_income = numeric_value
                income_iterator = False
                numeric_value = 0
            else:
                firm_costs = numeric_value

    return firm_name, firm_entity_type, firm_income, firm_costs


with open('task_7.txt', 'r', encoding='utf-8') as firm_data:
    source_lines = firm_data.readlines()

average_profit = 0
total_profit = 0
profitable_firms = 0
firm_data_dictionary = {}
json_list = []
for file_line in source_lines:
    firm_name, firm_entity_type, income, costs = line_parser(file_line)
    profit = income - costs
    if profit >= 0:
        total_profit += profit
        profitable_firms += 1
    firm_data_dictionary.update({firm_name: profit})

if profitable_firms > 0:
    average_profit = round(total_profit / profitable_firms, 2)
    average_profit_dict = {'average_profit': average_profit}

json_list.append(firm_data_dictionary)
json_list.append(average_profit_dict)

with open('task_7_firm_result.json', 'w', encoding='utf-8') as res_file:
    json.dump(json_list, res_file)


