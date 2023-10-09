import csv 
import json
import mysql.connector
import time
import argparse

table = "test1"
def db_setup():
    print("db set up")
    try:
        mydb = mysql.connector.connect(
        host="foo",
        user="user",
        password="password",
        port=3306,
        database="test1")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        exit(1)

    return mydb
def create_table(db):
    return

def create_query(row, tablename:str, colnames, colnames_list):
    str = f"INSERT INTO " + tablename + f" ({colnames}) VALUES ("

    first = True
    for i in colnames_list:
        if(first):
            str = str + row[i]
            first = False
        else:
            str = str + "," + json.dumps(row[i].strip())
    
    str = str + ");"
    return str
#
#
#
def insert_row(row,db, tablename: str, colnames, colnames_list) -> bool:
    sql_stmt = create_query(row, tablename, colnames, colnames_list)
    try:
        db.cursor().execute(sql_stmt)
    except mysql.connector.Error as error:
        print(f"Failed to insert record into table {error}")
        db.rollback()
        db.close()
        exit(1)

    return True
#
#
#
def build_colnames(row):
    colnames = ""
    colnames_list = []

    for keys in row.keys():
        if len(colnames) == 0:
            colnames = keys
            colnames_list = [keys]
        else:
            colnames = colnames + "," + keys
            colnames_list.append(keys)
    return colnames, colnames_list
#
# Check to see if DB connection is working,
#
def test_connection(db):
    cur = db.cursor()
    try:
        cur.execute("SELECT VERSION();")
    except mysql.connector.Error as error:
        db.close()
        print(error)
        exit(1)
    
    myresult = cur.fetchall()

    for x in myresult:
        print(x[0])
    return
#
# 
#     
def main():
    x=0
    
    #
    # Handle args
    #
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="csv filename to load")
    parser.add_argument("tablename", help="table to write to")
    parser.add_argument("numcols", type=int, help="Columns in iput file", default=62)
    
    
    args = parser.parse_args()

    #
    # Get started
    #
    NUMCOLS=args.numcols
    start = time.time()
    db = db_setup()
    test_connection(db)
    try: 
        with open(args.filename, 'r', encoding="ISO-8859-1") as csvfile:
            reader = csv.DictReader(csvfile,delimiter="\t")
            for row in reader:
                if x==0: # its the first row
                    colnames, colnames_list = build_colnames(row)
                    assert len(colnames_list) == NUMCOLS

                x+=1
                if len(row) != NUMCOLS:
                    print(row[0],len(row)) # bad row, not enough items
                    exit(1)
                else:
                    insert_row(row,db, args.tablename, colnames, colnames_list)

                if x % 1000 == 0: 
                    print(x)
                    db.commit()
                
    except FileNotFoundError:
        msg = "Sorry, the file does not exist."
        print(msg) # Sorry, the file John.txt does not exist. 
    db.commit()
    db.close()

    print(x, " rows")
    end = time.time()
    print("Time Elapsed: ",(end - start)/60, " min")

if __name__ == "__main__":
    main()
