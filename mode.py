from collections import Counter
import csv
with open('height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
for i in range (len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))

data=Counter(new_data)
mode_data_for_range={
                        "75-85":0,
                        "85-95":0,
                        "95-105":0,
                        "105-115":0,
                        "115-125":0,
                        "125-135":0,
                        "135-145":0,
                        "145-155":0,
                        "155-165":0,
                        "165-175":0,


                    }
for weight,occrence in data.items():
    if 75 < float (weight)<85:
        mode_data_for_range["75-85"]+=occrence
    elif 85 < float (weight)<95:
        mode_data_for_range["85-95"]+=occrence
    elif 95 < float (weight)<105:
        mode_data_for_range["95-105"]+=occrence
    elif 105 < float (weight)<115:
        mode_data_for_range["105-115"]+=occrence
    elif 115 < float (weight)<125:
        mode_data_for_range[ "115-125"]+=occrence
    elif 125 < float (weight)<135:
        mode_data_for_range["125-135"]+=occrence
    elif 135 < float (weight)<80:
        mode_data_for_range["135-145"]+=occrence
    elif 145 < float (weight)<145:
        mode_data_for_range["145-155"]+=occrence
    elif 155 < float (weight)<155:
        mode_data_for_range["155-165"]+=occrence
    elif 165 < float (weight)<165:
        mode_data_for_range["165-175"]+=occrence
    

mode_range,mode_occrence=0,0
for range, occrence in mode_data_for_range.items():
    if occrence > mode_occrence:
        mode_range,mode_occrence=[int(range.split("-")[0]),int(range.split("-")[1])],occrence
mode=float((mode_range[0]+mode_range[1])/2)
print(f"Mode is ->{mode:2f}")