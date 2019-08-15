from jenkinsapi.jenkins import Jenkins
import sys

RemoteInstance=Jenkins(sys.argv[1],sys.argv[2],sys.argv[3]) 
data2= RemoteInstance.plugins._data

# Reading Gold Copy Instance Plugins Information from plugin.csv file and map to other instance
f1 = open("plugin.csv","r")
f = f1.readlines()

# Generating Report to report.csv file 
f2 = open("/root/report.csv","w") 

# Here f[2:] implies to read file from line 3 of plugin.csv file. So that it ignores reading titles[Plugin Name,Version]
print("Total Plugins in Gold Copy Jenkins Instance -- "+str(len(f[2:]))) 
print("-----------------------------------------------------------------")
print("Total Plugins in Remote Jenkins Instance -- "+str(len(data2['plugins'])))
print("-----------------------------------------------------------------")

count = 0            # To get total number of matched plugins
count2 = 0           # To get total number of unmatched plugins due to version
count3 = 0           # To get total number of unavailable plugins

f2.write("------Plugin Matched-------\n")
f2.write("Plugin Name,Version"+"\n\n")
# Loop for matching the plugins along with version
for i in f[2:]:    
    for j in data2['plugins']:
        if (i.split(",")[0] == j['shortName'] and i.split(",")[1].strip() == j['version']):        
            print ("Plugin Matched --- "+ i.split(",")[0]+"  "+i.split(",")[1].strip())
            f2.write(i.split(",")[0]+","+i.split(",")[1].strip()+'\n')
            count+=1
print("-----------------------------------------------------------------")
print("Total Plugins Matched with version is  -- "+ str(count))
print("-----------------------------------------------------------------")

f2.write("\n------Plugin UnMatched due to version-------\n")
f2.write("Plugin Name,Gold Copy Jenkins Instance Version,Remote Jenkins Instance Version"+"\n\n")
# Loop for Unmatched plugins due to version
for i in f[2:]:    
    for j in data2['plugins']:
        if (i.split(",")[0] == j['shortName'] and i.split(",")[1].strip() != j['version']):        
            print("Not Matched due to version---  "+i.split(",")[0] +"   Gold Copy Instance version :-- "+ i.split(",")[1].strip()+ "   Remote Jenkins Instance version :-- "+ j['version'])
            f2.write(i.split(",")[0]+","+i.split(",")[1].strip()+","+j['version']+'\n')
            count2+=1

print("-----------------------------------------------------------------")
print("Total Unmatched Plugins with different version is -- "+str(count2))
print("-----------------------------------------------------------------")

f2.write("\n------Plugin Unavailable-------\n")
f2.write("Plugin Name"+"\n\n")
# Loop for Unavailable Plugins
for i in f[2:]:
    count1=0    
    for j in data2['plugins']:
        if (i.split(",")[0] == j['shortName']):
            count1=1
    if count1 == 0:         
        print ("Not Available on Remote Instance--- "+ i.split(",")[0])
        f2.write(i.split(",")[0]+"\n")
        count3+=1
f1.close()
print("-----------------------------------------------------------------")
print("Total Unavailable Plugins  -- "+str(count3))
print("-----------------------------------------------------------------")


