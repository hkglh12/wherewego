import pymysql
import csv
import sys


def CSVReaderR(file_name, CSVContent):
    # fm = File manager
    fm = open(file_name, 'r', encoding="cp949")
    reader = csv.reader(fm)
    for line in reader:
        line[2] = line[2].replace(', ', '/')
        line[2] = line[2].replace('[', '{')
        line[2] = line[2].replace(']', '}')
        CSVContent.append(line)
    fm.close
    return CSVContent


def CSVReaderD(file_name, CSVContent):
    fm = open(file_name, 'r', encoding="cp949")
    reader = csv.reader(fm)
    for line in reader:
        CSVContent.append(line)
    fm.close
    return CSVContent

CSVContent = []
print("Your system encoding:")
print("IN:"+sys.stdin.encoding+"\n")
print("OUT"+sys.stdout.encoding+"\n")

flag = input(
    """Enter r if you are trying to put rawdata into DB\n
Enter d if you are tring to put dic data into DB\n
your input? : """
    )
file_name = input("""Input your .csv file name except .csv\n
your input?: """)
file_name = file_name+".csv"

if flag == "r":
    CSVContent = CSVReaderR(file_name, CSVContent)
    print(CSVContent)
    print(CSVContent[0])
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='aegis1load',
        db='wherewego',
        charset='utf8'
    )
    curs = conn.cursor()
    
    # sql = "INSERT INTO rawdata (title, contents, keywords) VALUES ('%s', '%s', '%s')"
    # sql = """insert into rawdata(title, contents, keywords)
    #         values (%s, %s, %s)"""
    for rawdata in CSVContent:
        # sql = "INSERT INTO rawdata (title, contents, keywords) VALUES (%s, %s, %s)" \
        #     % ("'"+rawdata[0]+"'", "'"+rawdata[1]+"'", "'"+rawdata[2]+"'")
        # curs.execute(sql)
        sql = "INSERT INTO rawdata (title, contents, keywords) VALUES (%s, %s, %s)"
        in_tp = (rawdata[0], rawdata[1], rawdata[2])
        curs.execute(sql, in_tp)
        conn.commit()

    print("insert complete")
    conn.close()

elif flag == "d":
    CSVContent = CSVReaderD(file_name, CSVContent)
    print(CSVContent)
    print(CSVContent[0])
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='aegis1load',
        db='wherewego',
        charset='utf8'
    )
    curs = conn.cursor()
    for dic in CSVContent:

        sql = "INSERT INTO dic (local_index, morpheme, score, coord_latitude, coord_longitude) VALUES(%s, %s, %s, %s, %s)"
        tupe = (int(dic[0]), dic[1], int(dic[2]), dic[3], dic[4])
        print(tupe)
        curs.execute(sql, tupe)
        conn.commit()

    print("insert complete")
    conn.close()

