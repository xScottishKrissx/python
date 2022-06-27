#basic for loop
#x = 0 
#for x in range(5,10):
#    print(x)

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
    # if(d == "Thu"): break
    
    # skip over something
    if(d == "Thu"): continue
    print(d)