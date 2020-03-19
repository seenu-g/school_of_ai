import pickle 
from io import StringIO  
class SimpleObject(object): 
  
    def __init__(self, name): 
        self.name = name 
        l = list(name) 
        l.reverse() 
        self.name_backwards = ''.join(l) 
        return
        
def main() :
    data = [ { 'a':'A', 'b':2, 'c':3.0 } ] 
    data_string = pickle.dumps(data) 
    print ('PICKLE:', data_string)
    
    data = [] 
    data.append(SimpleObject('pickle')) 
    data.append(SimpleObject('cPickle')) 
    data.append(SimpleObject('last')) 
    
    filename = 'serialized.native'
    try :
        serialized = pickle.dumps(data)
        with open(filename,'wb') as file_object:
            file_object.write(serialized)
    except :
        print('problem in write operation')
    
    deserialized = []
    try :
        with open(filename,'rb') as file_object:
             raw_data = file_object.read()
        deserialized = pickle.loads(raw_data)     
    except :
        print('problem in write operation')
        
    data1 = deserialized  
    for item in data1 :
        tempObj = item
        print(tempObj.name)
            
if __name__ =='__main__':
    main()