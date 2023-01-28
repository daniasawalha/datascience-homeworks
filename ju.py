
count=0
class ju:
    def __init__(self):
        print("llllll")
    class medical_colleges:
        
        def doctor(self):
            global count
            doct={}
            if count!=5:
                count +=1
                #doct[name]
                return 1
            else:
               return 0
            
class Dyclass:
    def __init__(self, module_name, class_name):
 
       module = __import__(module_name) # __import__ method used to getmodule
       my_class = getattr(module, class_name) #getting attribute by getattr() 
       my_class.ju()
       
       
d=ju.medical_colleges()
print(d.doctor())
class myClass:
	def __init__(self,val):
		self.val=val
	def getVal(self):
		return self.val
    
import sys
#sys.path.append("ju.py")
sys.path.insert(0,"..")
'from ju import myClass'
print(sys.path)

#newClass = myClass(5)
#val = newClass.getVal()

#print(val)