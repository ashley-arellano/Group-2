#This is the code to a short python script
#that reads files and get the reverse complement of a DNA strand
def checkFile():
    while True:
        try:
            fname = input("Enter the file name: \n")
            iFile = open(fname)
        except IOError:
            print("File not accessible. Try again.\n")
            continue
        else:
            iFile.close()
            print("File accepted. Loading...")
            return fname

def readFile(fname):
    with open(fname, 'r') as iFile:
        for line in iFile:
            singLine = " "
            singLine = line
            REVCline = revComplement(singLine)
            print(REVCline)
    iFile.close()

def revComplement(line):
    revLine = ""
    DNAbase = ""
    count = 0
    start = 1
    end = 0
    while(count < len(line)):
        DNAbaseLoc = slice(len(line)-start, len(line)-end) #problem
       
        DNAbase = line[DNAbaseLoc]
        match DNAbase:
            case 'A':
                DNAbase = DNAbase.replace('A', 'T')
            case 'T':
                DNAbase = DNAbase.replace('T', 'A')
            case 'C':
                DNAbase = DNAbase.replace('C', 'G')
            case 'G':
                DNAbase = DNAbase.replace('G', 'C')

        revLine = revLine + DNAbase

        count += 1
        start += 1
        end += 1
    return revLine

#Main Function
fname = checkFile()
readFile(fname)