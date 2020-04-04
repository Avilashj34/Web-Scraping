import os
import simplejson as json
import pandas as pd

def save(Search_KeyWord, project_name, project_name_link, Image_Link, Image_Link_Name, Project_Location, Project_Location_Redirect_Line
     , price_range, Built_Up_Area, EMI, RERA, Marketed_by, Owner_name,
         Owner_link, Owner_type, Description, NearBy_Facility):
    print("In a file "+ Search_KeyWord)
    count, n_count = 0, 0
    n1 = []
    #NearBy to JSON
    for i in NearBy_Facility:
        n_count = n_count + 1
        n1.append({"N_Id": n_count, "Name": i})
    #print(n1[0])

    if os.path.isfile("./Housing_json/housing_" + Search_KeyWord + ".json") and os.stat("./Housing_json/housing.json").st_size != 0:
        print("Exists")
        #old_file = open("./housing_" + Search_KeyWord + ".json", "r+")
        #d = json.loads(old_file.read())
    else:
        count = 0
        d = []
        old_file = open("./Housing_json/housing_" + Search_KeyWord + ".json", "w+")
        print("Opening the File")
        print("Converting to JSON")
        for i in range(len(project_name)):
            count = count + 1
            print("Appending the " + str(i) + " value")
            d.append({"Id": count,
                      "Project_Name": project_name[i],
                      "Project_Name_Link": project_name_link[i],
                      "Image_Link" : Image_Link[i],
                      "Image_Link_Name": Image_Link_Name[i],
                      "Project_Location": Project_Location[i],
                      "Project_Location_Redirect_Line": Project_Location_Redirect_Line[i],
                      "Price_Range": price_range[i],
                      "Built_Up_Area": Built_Up_Area[i],
                      "EMI": EMI[i],
                      "Rera": RERA[i],
                      "Marketed_by": Marketed_by[i],
                      "Owner_name": Owner_name[i],
                      "Owner_link": Owner_link[i],
                      "Owner_type": Owner_type[i],
                      "Description": Description[i],
                      "NearBy_Facility": n1[i]})

    print("Writing to File")
    old_file.seek(0)
    old_file.write(json.dumps(d))
    print("Sucessfully Completed")
    print("Writing to CSV File")
    df = pd.DataFrame(d)
    df.to_csv("./Housing_csv/housing_" + Search_KeyWord + ".csv", index=False)


