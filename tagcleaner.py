import re
import sys 

def cleaner():
    regex = re.compile('<[^>]*>')
    
    with open("html.txt", "w+") as f:
        
        with open(sys.argv[1],"r+") as h:
            for line in h:
                f.write(re.sub(regex,''+'\n',line ) )
            f.close()
    
     
if __name__ == "__main__":
    cleaner()
