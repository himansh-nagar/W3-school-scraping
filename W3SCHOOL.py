from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint,webbrowser,json

w3_school_url=urlopen('https://www.w3schools.com/')
soup=BeautifulSoup(w3_school_url,'html.parser')

cources_div=soup.find_all("div",class_="w3-col l6 w3-center")

######## all programing cources abalavble 
cources_list=[]
for cources in cources_div:
    if cources.text not in cources_list:
        cources_list.append(cources.text)
        print(cources.text)
        print("------"*20)

file1=open("cources.json",'w')
json.dump(cources_list,file1)
file1.close()

# ############ ## learn links
learn_links_dict={}
for a_tags in cources_div:
    a_tag=a_tags.find_all("a")
    for a in a_tag:
        learn_links_dict[a.text]="https://www.w3schools.com/"+a['href']
# print(learn_links_dict)

user=input("  \n \n NAME THE COURCE YOU WANT TO ENROLL  \n \t \t").upper()      #### ENTER LEARN BEFORE EVERY LANGUAGE YOU WANT TO LEARN LIKE - LEARN PYTHON
b_neded=user.split()
badd_neded=b_neded[1].lower()


# ##########       going inside the cources

cources_url=urlopen(f'{learn_links_dict[user]}')
soup2=BeautifulSoup(cources_url,'html.parser')
div_of_bar =soup2.find("div",class_='w3-light-grey')
bar_details ={}
h2_bar=div_of_bar.find_all("h2")
atags_bar =div_of_bar.find_all("a")
for h2 in h2_bar:
    new_div=div_of_bar.text.split('h2')
new_div=new_div[0].split('\n')
for new in  new_div:
    if new=='':
        new_div.remove(new)
A_list=[]
for AA in atags_bar:
    A_dic={}
    A_dic[AA.text]=f"https://www.w3schools.com/{badd_neded}/"+AA['href']
    A_list.append(A_dic)
num=1
for dic in A_list:
    for ele in dic:
        print("\t",num,".",ele)
        num+=1

cource_user=int(input(" \n \n \t \t  ENTER THE Number OF TOPIC YOU WANT TO READ :)   \n\t\t"))

neded_url_var=A_list[cource_user-1]
for one_dic in neded_url_var:
    link_to_open=neded_url_var[one_dic]

open_that_link=webbrowser.open(link_to_open)
print("HAPPY LEARNING  ")

