import thulac, zipfile, os, csv, math

def count(zip_name, folder_path=os.getcwd()):
    """Count the times each word appears in each txt file
    
    Args:

            zip_name: the name of the zip file.

            folder_path: the dictory where stores the zip file, and its default value is current working dictory.
    """
    dic = dict()
    z = zipfile.ZipFile(folder_path + "/" + zip_name, "r")
    for file_name in z.namelist()[0:6000]:
        if (file_name[-1] == "t" and file_name[0] == "T"):
            txt_name = file_name.split("/")[-1]
            print(txt_name)
            for line in z.open(file_name).readlines():
                l = thulac.thu1.cut(line.decode("utf-8-sig"), text = True).split(" ")
                for word in l:
                    dic.setdefault(word, {txt_name: 0})
                    dic[word].setdefault(txt_name, 0)
                    dic[word][txt_name] += 1
    file_names(dic)

def file_names(dic):
    """Get all the txt files' names and from a list

    Args:

            dic: the dictionary that stores the count
    """
    file_name_list = []
    for dics in dic.values():
        file_name_list += dics.keys()
    file_name_list = sorted(list(set(file_name_list)), key=lambda each: int(each.split(".")[0]))
    draw_table(dic.copy(), file_name_list, "tfidf")
    draw_table(dic.copy(), file_name_list, "tf")

def draw_table(dic, field, mode):
    """Draw TF table or the TFIDF table

    Args:

            dic: the dictionary that stores the count

            field: the list of files' names

            mode: TF table or the TFIDF table
    """
    csv_name = mode + " table_Ch.csv"
    with open(csv_name,'w', newline='', encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([""] + field)
        n = len(field)
        for items in list(dic.items()):
            word = items[0]
            each_row = [word]
            for name in field:
                if (mode == "tf"):
                    data = items[1].setdefault(name, 0)
                else:
                    df = len(list(items[1].keys()))
                    idf = math.log(n/(df+1))
                    tf = items[1].setdefault(name, 0)
                    data = tf * idf
                each_row.append(data)
            writer.writerow(each_row)

def main():
    """Main method

    Enter the zip file name in the current working dictory to start analysis
    """
    thulac.thu1 = thulac.thulac(seg_only=True)
    zip_name = input("Please enter the name of the zip file you would like to analyze: ")
    count(zip_name)
    print("Finish!")

main()