if __name__ == '__main__':
    
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name,score])
    
  
    
    a = dict(a)
    
    
    
    a = dict(sorted(a.items(), key=lambda item: item[1]))
    
    

    
    
    val = list(a.values())
    val = set(val)
    val = tuple(val)
    val = list(val)
    keys = list(a.keys())
    
    low_score = val[1]
    result = []
    for i in range(10):
        if low_score in a.values():
            position = val.index(low_score)
            d = keys[position]
            result.append(d)
            result = sorted(result)
            
            element = a.pop(d)
            val = list(a.values())
            keys = list(a.keys())
        
        
        
    print(*result, sep='\n')
    
    
    
    
    
    
   
    
  
    
   
