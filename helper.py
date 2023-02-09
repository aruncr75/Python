print("helperstarted")
f = open("demofile.txt", "r")

# //s1
# for x in f:
#     stsplit =x.split("=")
    
#     print("this."+stsplit[0].split(" ")[-1].replace(";","")+",")






# s2

for x in f:
    stsplit =x.split("=")
    
    print(stsplit[0].split(" ")[-1].replace(";","")+":"
    +stsplit[0].split(" ")[-1].replace(";","")+",")
  

