import argparse
import numpy
from sortalgorithm import *

def main(inpArgs):
    AllowedSorts=["BUBBLE","SELECT","INSERTION","QUICK"]
    SpecifiedSort = inpArgs.sortmethod
    SpecifiedSort = SpecifiedSort.upper()
    if SpecifiedSort not in AllowedSorts:
        print("The sort method specified " + SpecifiedSort + "does not exist. Allowed values are"+" ".join(AllowedSorts))
        return 0
    
    InpArray=numpy.random.randint(1,100,size=10)
    
    SortObj = SortAlgorithm()
    
    
    if SpecifiedSort == "BUBBLE":
        SortedArray = SortObj.BubbleSort(InpArray)
        print("SORTING COMPLETE...\n")
        print(SortedArray)
        
    if SpecifiedSort == "SELECT":
        SortedArray = SortObj.SelectSort(InpArray)
        print("SORTING COMPLETE...\n")
        print(SortedArray)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="parser for sorting")
    parser.add_argument("-s","--sortmethod",dest="sortmethod",help="sorting method required",required=True)
    inpArgs = parser.parse_args()
    main(inpArgs)