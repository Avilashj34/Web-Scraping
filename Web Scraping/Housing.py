from bs4 import BeautifulSoup
import requests
from Scrapping.Housing.SaveToFile import save

#https://towardsdatascience.com/looking-for-a-house-build-a-web-scraper-to-help-you-5ab25badc83e
#P3a28wnza61239r6o, Plqq7bm2s53fechd, P5oa6tax11cqpt9vh
Search_KeyWord = input("Enter the Search Keyword")
data = requests.get("https://housing.com/in/buy/searches/P3659o4itp2vujkis")
soup = BeautifulSoup(data.text, "html.parser")
print(soup.title)
l = soup.title.text.split(',')
n = len(l)
Search_KeyWord= (Search_KeyWord+l[n-1].replace(" ", "_"))
print(Search_KeyWord)
result = soup.findAll("div", {"class": "css-14dhboj"})
project_name, project_name_link = [], []
price_range = []
Project_Location, Project_Location_Redirect_Line = [], [] #css-pa049
Image_Link, Image_Link_Name = [], []
Built_Up_Area = []
EMI = []
RERA = []
Marketed_by = []
Owner_name, Owner_link, Owner_type = [], [], []
Description = []
NearBy_Facility = [] #css-6hrqu0
#print(result)
name = soup.findAll("article", {"class": "css-h7k7mr"})
#print(name)
print("Extracting Data from "+data.url)
for item in name:
    if item.find("a"):
        pn = item.find("a").text
        project_name.append(pn)
    else:
        project_name.append("None")
    if item.find("img"):
        im = item.find("img")
        Image_Link.append(im["src"])
        Image_Link_Name.append(im["alt"])
    else:
        Image_Link.append("None")
        Image_Link_Name.append("None")
    if item.find("a", {"class": "css-163eyf0"}):
        pn_link = item.find("a", {"class": "css-163eyf0"})
        if pn_link.has_attr('href'):
            project_name_link.append("https://housing.com" + pn_link['href'])
        else:
            project_name_link.append('None')
    else:
        project_name_link.append("None")
    if item.find("h2"):
        pr = item.find("h2").text
        price_range.append(pr)
    else:
        price_range.append("None")
    if item.find("span", {"class": "css-nin1gj"}):
        emi = item.find("span", {"class": "css-nin1gj"}).text
        EMI.append(emi)
    else:
        EMI.append("None")
    if item.find("div", {"class": "css-1ty8tu4"}):
        config = item.find("div", {"class": "css-1ty8tu4"}).text
        Built_Up_Area.append(config)
    else:
        Built_Up_Area.append("None")
    if item.find("div", {"class": "css-10u0itx"}):
        rera = item.find("div", {"class": "css-10u0itx"})
        RERA.append(rera.text)
    else:
        RERA.append("None")
    if item.find("div", {"class": "css-1j62xqm"}):
        market = item.find("div", {"class": "css-1j62xqm"})
        Marketed_by.append(market.text)
    else:
        Marketed_by.append("None")
    if item.find("div", {"class": "css-9ws0sq"}):
        owner_name = item.find("div", {"class": "css-9ws0sq"})
        o = owner_name.find('a')
        if o.has_attr('href'):
            Owner_link.append("https://housing.com"+o['href'])
        else:
            Owner_link.append("None")
        #print(owner_name.find('a'))
    else:
        owner_name = "None"
    Owner_name.append(owner_name.text)
    if item.find("div", {"class": "css-1lrcm0c"}):
        owner_type = item.find("div", {"class": "css-1lrcm0c"}).text
    else:
        owner_type = "None"
    Owner_type.append(owner_type)
    if item.find("div", {"class": "css-9zqt6g"}):
        description = item.find("div", {"class": "css-9zqt6g"}).text
    else:
        description = "None"
    Description.append(description)
    sp_hl = []
    if item.findAll("div", {"class": "css-6hrqu0"}):
        special_highlight = item.findAll("div", {"class": "highlight css-1byt3mr"})
        for i in special_highlight:
            sp_hl.append(i.text)
            #print("New String " + nt)
    else:
        sp_hl.append("None")
    NearBy_Facility.append(sp_hl)
    if item.find("a", {"class": "css-pa049"}):
        project_loc = item.find("a", {"class": "css-pa049"})
        Project_Location.append(project_loc.text)
        if project_loc.has_attr('href'):
            Project_Location_Redirect_Line.append("https://housing.com" + project_loc["href"])
        #
    else:
        Project_Location.append("None")
        Project_Location_Redirect_Line.append("None")


print(len(project_name), project_name)
print(len(project_name_link), project_name_link)
print(len(Image_Link), Image_Link)
print(len(Image_Link_Name), Image_Link_Name)
print(len(Project_Location), Project_Location)
print(len(Project_Location_Redirect_Line), Project_Location_Redirect_Line)
print(len(price_range), price_range)
print(len(Built_Up_Area), Built_Up_Area)
print(len(EMI), EMI)
print(len(RERA), RERA)
print(len(Marketed_by), Marketed_by)
print(len(Owner_name), Owner_name)
print(len(Owner_link), Owner_link)
print(len(Owner_type), Owner_type)
print(len(Description), Description)
print(len(NearBy_Facility), NearBy_Facility)

#writing to file

save(Search_KeyWord, project_name, project_name_link, Image_Link, Image_Link_Name, Project_Location, Project_Location_Redirect_Line, price_range, Built_Up_Area, EMI, RERA, Marketed_by, Owner_name, Owner_link, Owner_type, Description, NearBy_Facility)




