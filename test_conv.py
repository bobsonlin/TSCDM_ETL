#!/usr/bin/env python
import csv
import random
from optparse import OptionParser

max_colnum = 4
colnum2colname = {1:'med_ID', 4:'HOSP_ID', 5:'DRUG_DAY', 6:'ID_S'}
colnum2attrnum = {1:1, 4:7, 5:9, 6:10}
comp_col = [4, 5, 6]
random_num = []

def num2col (random_num):
    col = []
    for e in random_num:
        if e == 0:
            col.append(e+1)
        else:
            col.append(e+3)
    return col


def comp_data (raw_file, extract_file, text_file):
    comp_result = False
    read_col = []
    sel_col = []
    count = 1

    with open(text_file, 'r') as f_txt:
        col_data = f_txt.read()
        for e in col_data.split():
            read_col.append(int(e))
    # print 'read_col: ' + str(read_col)

    ## do not compare the data in 1st col (for now)
    ## TODO 1st col data generated from raw data
    for e in comp_col:
        if e in read_col:
            sel_col.append(e)
    # print 'sel_col: ' + str(sel_col)

    with open(raw_file, 'r') as f_raw:
        with open(extract_file, 'r') as f_ext:
            csv_raw = csv.DictReader(f_raw)
            for line in f_ext:
                ext_line = line.split('^')
                row = next(csv_raw)
                for e in sel_col:
                    try:
                        '''
                        print 'ext_line[colnum2attrnum[e]]'
                        print str(ext_line[colnum2attrnum[e]])
                        print 'row[colnum2colname[e]]'
                        print str(row[colnum2colname[e]])
                        '''
                        if ext_line[colnum2attrnum[e]] != row[colnum2colname[e]]:
                            print 'count: ' + str(count)
                            comp_result = False
                            return comp_result
                    except:
                        print 'count: ' + str(count)
                        print 'exit from except'
                        return comp_result
                count += 1

    # print 'count: ' + str(count)
    print 'verify success!'
    comp_result = True
    
    return comp_result


def parse_args():
    parser = OptionParser(usage='%prog -g -n <int number>\n       %prog -c <raw_datafile> <extracted_datafile> -t <col_file>')
    parser.add_option('-g', '--generate', action='store_true', dest='is_gen',
                      default=False,
                      help='generate a csv file with random column numbers')
    parser.add_option('-n', '--num-col', action='store', dest='num_col',
                      default=0,
                      help='assign the total number of available columns')
    parser.add_option('-c', '--compare', action='store', dest='raw_file',
                      default='nofile',
                      help='compare the data between the raw datafile and the generated file')
    parser.add_option('-t', '--text-file', action='store', dest='text_file',
                      default='nofile',
                      help='the csv file with column numbers')
    options, args = parser.parse_args()
    
    # print 'options: ' + str(options)
    # print 'args: ' + str(args)
    
    ## TODO --- check machanism ---
    
    return options, args


def main():
    options, args = parse_args()
    if options.is_gen:
        num_col = int(options.num_col)
        if num_col > 0:
            num_col = min(num_col, max_colnum)
            random_num = random.sample(range(0, max_colnum), num_col)
            col_num = num2col(random_num)
            print 'col_num: ' + str(col_num)
            
            with open('col.txt', 'w') as f_cs:
                for e in col_num:
                    f_cs.write(str(e))
                    f_cs.write('\n')
    elif options.raw_file != 'nofile' and len(args) > 0 and options.text_file != 'nofile':
        raw_file = options.raw_file
        text_file = options.text_file
        extract_file = args[0]
        comp_data(raw_file, extract_file, text_file)

                



if __name__ == '__main__':
    main()