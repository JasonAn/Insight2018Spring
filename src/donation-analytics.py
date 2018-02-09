import numpy as np
import math
import datetime
import os
import sys

# if (len(sys.argv) == 1 or len(sys.argv) != 3) :
#     exit()



## IO, input files and output files

address = os.getcwd()

inputfile = str(address+sys.argv[1][1:])
percentilefile = str(address+sys.argv[2][1:])
outputfile = str(address+sys.argv[3][1:])

## global variables
contri_hash = dict()    # contri_hash, a hash_table, stores the contribution query, key = [NAME, ZIP], value = Contribution
contri_list = list()    # contri_list, a list, stores all contribution data, be used to return the percentile contribution.
       
num = 0                 # total number of repeated contributors
cnt = 0                 # total contribution

## read the percentile from file 

with open(percentilefile) as f:
    line = f.readline()
    per = int(line)/100.0

## 
with open(outputfile, 'w') as the_file:

    with open(inputfile) as f:
        lines = f.readlines()     # read the data file line by line
        
        for line in lines:

            myarray = line.split('|')

            if myarray[15] == str(): # Only read record with OTHER_ID == empty
                CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT = myarray[0], myarray[7], myarray[10], myarray[13], myarray[14]

                if len(NAME) < 2 or len(ZIP_CODE) < 5 or len(TRANSACTION_DT) != 8 or len(CMTE_ID) == 0 or len(TRANSACTION_AMT) == 0: ## conditions of invalid record
                    continue
                
                else:

                    year = int(TRANSACTION_DT[-4:])  
                    month = int(TRANSACTION_DT[0:2])
                    day = int(TRANSACTION_DT[2:4])

                    try:                # verify the record should have a valid date time, valid zip and valid transaction amount
                        newDate = datetime.datetime(year=year, month=month, day=day)

                        ZIP_CODE = ZIP_CODE[:5]
                        TRANSACTION_AMT = int(TRANSACTION_AMT)

                        if (NAME, ZIP_CODE) not in contri_hash:  # if the identity can not be found in previous history, add the record to the hashtable
                            contri_hash[(NAME, ZIP_CODE)] = TRANSACTION_AMT
                        else:                                 # if the identity can be found in previous history, return the result, update the hashtable and list
                            num += 1
                            cnt += TRANSACTION_AMT
                            contri_list.append(TRANSACTION_AMT)
                            order = int(math.ceil(per * len(contri_list))-1)
                            query = "|".join([CMTE_ID, ZIP_CODE[0:5], str(year), str(sorted(contri_list)[order]), str(cnt), str(num)])

                            the_file.write(query+"\n")

                    except ValueError:
                        continue



                

                
