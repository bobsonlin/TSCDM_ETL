#!/usr/bin/env python
import csv
from random import randint
from optparse import OptionParser
import datetime

input_attr = ['FUNC_DATE', 'APPL_DATE', 'FEE_YM', 'HOSP_ID', 'DRUG_DAY', 'ID_S']
col_name = ['pat_ID (necessary)', 'med_ID', 'code (necessary)', 'order_ID (necessary)', 'drug_code', 'days_supply', 'Amount dispense']
datafile = 'nofile'
sel_file = 'nofile'
col = []

def parse_args():
    parser = OptionParser(usage='%prog --rawdata <filename> [--select <csv_filename>]\n                   --list-col')
    parser.add_option('-r', '--rawdata', action='store', dest='datafile',
                      default='nofile',
                      help='csv file with raw data as this program input')
    parser.add_option('-s', '--select', action='store', dest='sel_file',
                      default='nofile',
                      help='txt file that designate which column you want your data to store into')
    parser.add_option('-l', '--list-col', action='store_true', dest='is_list',
                      default=False,
                      help='list all the columns name and corresponding number')
    options, args = parser.parse_args()
    
    ## TODO --- check machanism ---
    
    return options


def conv (datafile, sel_file):
    year = str(datetime.datetime.now().timetuple().tm_year)
    month = str(datetime.datetime.now().timetuple().tm_mon).zfill(2)
    day = str(datetime.datetime.now().timetuple().tm_mday).zfill(2)

    ## for debug
    outputfile = 'epicmed.esp.' + month + day + year
    print 'outputfile: ' + outputfile

    with open(sel_file, 'r') as f_coldata:
        col_data = f_coldata.read()
        for e in col_data.split():
            col.append(int(e))

    with open(datafile, 'r') as rawdata:
        with open(outputfile, 'w') as f_esp:
            reader = csv.DictReader(rawdata)
            count = 0
            for row in reader:

                ## pat_ID -- 0
                if row[input_attr[0]] is None:
                    f_esp.write('111111111')
                else:
                    f_esp.write(row[input_attr[0]])
                

                f_esp.write('^')

                ## med_ID -- 1
                if 1 in col:
                    f_esp.write(str(randint(1, 9)))
                
                f_esp.write('^')
                
                ## code -- 2
                if row[input_attr[1]] is None:
                    f_esp.write('')
                else:
                    f_esp.write(row[input_attr[1]])
                    f_esp.write(row[input_attr[0]])
                    f_esp.write(str(randint(1, 9)))
                


                f_esp.write('^^')



                ## order_ID -- 3
                if row[input_attr[2]] is None:
                    f_esp.write('')
                else:
                    f_esp.write(row[input_attr[2]])
                    f_esp.write('01')
                


                f_esp.write('^^^')


                ## drug_code -- 4
                if 4 in col:
                    if row[input_attr[3]] is None:
                        f_esp.write('')
                    else:
                        f_esp.write(row[input_attr[3]])
                

                f_esp.write('^^')



                ## days_supply -- 5
                if 5 in col:
                    if row[input_attr[4]] is None:
                        f_esp.write('')
                    else:
                        f_esp.write(row[input_attr[4]])
                

                f_esp.write('^')



                ## Amount dispense -- 6
                if 6 in col:
                    if row[input_attr[5]] is None:
                        f_esp.write('')
                    else:
                        f_esp.write(row[input_attr[5]])
                

                f_esp.write('^^^^')
                f_esp.write('\n')


                count += 1
                if count == 100:
                    break


def col_list():
    i=0
    for e in col_name:
        print i, e
        i += 1

def main():
    options = parse_args()
    if options.is_list:
        col_list()
    elif options.datafile != 'nofile' and options.sel_file != 'nofile':
        ## for debug
        print 'datafile: ' + options.datafile
        print 'sel_file: ' + options.sel_file
        
        conv (options.datafile, options.sel_file)

if __name__ == '__main__':
    main()