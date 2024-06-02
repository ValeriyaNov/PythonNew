def convert_format(input: list[str] = None) -> list[int]:
    '''Преобразования входных данных в терминале в матрицу'''
    
    array=[]
    m=[]
   
    for i in input:
       
        if i=='a':
            array.append(m)
            m=[]
            
        else:
            m.append(int(i))
    
    return array
    

