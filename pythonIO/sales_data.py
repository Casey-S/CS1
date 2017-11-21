with open('sales_data.txt') as f:
    index = 0
    for index, line in enumerate(f):
        index += 1
print(index)


with open('sales_data.txt') as f:
    feb_list = []
    for index, line in enumerate(f):
        slash_pos = line.index('/')
        if line[slash_pos - 1] is "2" and line[slash_pos - 2] is not "1":
            feb_list.append(line)
    # print(feb_list)
    # print(len(feb_list))

# remove /t
# remove /n
# remove $
# .split = array of strings
# .replace = maintain string

raw_data = open('sales_data.txt')


def clean_up(raw_data):
    cleaned_lines = []
    for line in raw_data:
        cleaned_line = line.replace('$', '')
        cleaned_line = cleaned_line.replace('\n', '')
        cleaned_line = cleaned_line.split('\t')
        cleaned_line[3] = float(cleaned_line[3])
        cleaned_lines.append(cleaned_line)
    return cleaned_lines


cleaned_data = clean_up(raw_data)
cleaned_data_phillies = cleaned_data[:9]
phillies_sales = [i for i in cleaned_data_phillies if i[0] == 'Philadelphia']
print(phillies_sales)

total_sales = sum([i[3] for i in cleaned_data])
print(total_sales)
