def BMI(w, h):
    print "BMI = %d / %d" %(h, w)
    return w / h 
    
   
    
weight = int(raw_input("Please input your weight:(kg)"))
height = int(raw_input("Please input your height:(m)"))

U-BMI = BMI(weight, height)
print "Your BMI is: %d" % U-BMI
