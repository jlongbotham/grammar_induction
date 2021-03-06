#!/usr/bin/env python

from __future__ import division
import sys
import re

def list_to_txt(xml_list):
    txt = ""
    for item in xml_list:
        txt = txt + item + "\n"
    # have to remove last newline for Giza++
    return txt[:(len(txt)-1)]


def main():
  
    """ EVALUATION """    
    # recall - percentage of test sentences that were correctly translated
    # precision - percentage of translations that were correct
    results_path = sys.argv[1]
    directory = sys.argv[2]
    results = open(results_path, "r").read()
    spr = ""

    spr += results_path + "\t" 
    
    # precision
    match = re.search("Complete\smatch(\s+)=(\s+)([0-9\.]+)", results)
    precision = match.group(3)

    # recall
    valid = re.search("Number\sof\sValid\ssentence(\s+)=(\s+)([0-9\.]+)", results)
    total = re.search("Number\sof\ssentence(\s+)=(\s+)([0-9\.]+)", results)  
    recall = ((float(valid.group(3)) * (float(precision))/100) / float(total.group(3))) * 100
    
    spr += str(round(recall,2)) + "\t"
    spr += precision + "\t"
    
    fscore = (recall + float(precision)) / 2
    spr += str(round(fscore,2)) + "\n"

    full_results = open(directory + "/results", "a")
    full_results.write(spr)
    full_results.close()    

if __name__ == "__main__":
    main()

