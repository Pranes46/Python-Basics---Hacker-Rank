from collections import Counter
from itertools import chain
if __name__ == '__main__':
    s = input()
    d= Counter(sorted(s)).most_common(3)
    for i,j in d:
        print(i,j,end='\n')
    
    
        
        
