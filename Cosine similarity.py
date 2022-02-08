import csv, math

def write_file(names, data, file_name):
    data2 = list()
    with open('normalized ' + file_name,'w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(names)
        for index in range(len(data[0])):
            data2.append(list())
            for each in data:
                data2[index].append(each[index])
            writer.writerow(data2[index])
    print('Finish!')


def normalize(data):
    for posi in range(len(data)):
        square_nums = list()
        if (data[posi][0].isdigit()):
            for index in range(len(data[posi])):
                num = int(data[posi][index])
                data[posi][index] = num
                square_nums.append(num*num)   
            base = math.sqrt(sum(square_nums))
            for index in range(len(data[posi])):
                data[posi][index] /= base

def read_file(file_name):
    data = list()
    with open(file_name, encoding='utf-8') as f:
        reader = list(csv.reader(f)) 
        name_list = reader[0]      
        length = len(name_list)
        for i in range(length):
            data.append(list())

        for column in reader[1:]:
            for i in range(length):
                data[i].append(column[i])
    
    normalize(data)
    write_file(name_list, data, file_name)

def main():
    file_name = input("Please enter the Term Frequency csv file you would like to analyze: ")
    read_file(file_name)

main()