import requests
from bs4 import BeautifulSoup
import re




def main():
    user_entry = input("What courses are you looking to register this semester?\n")
    courses = user_entry.split(',')
    print(courses,"\n")
    user_taken = input("What courses have you already finished?\n")
    done = user_taken.split(',')
    print(done,"\n")
    url = 'https://web.uvic.ca/calendar2020-01/CDs'
    for i in courses:
        try:
            subject, num = prerequisites(url, i)
        except:
            print(i,"has no pre-requisites")
    print("DONE")


def prerequisites(url, coursename):
    subject = coursename.split()[0]
    num = coursename.split()[1]
    url = url+"/"+subject+"/"+num+".html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id = "content-main")
    # print(results.prettify())
    try:
        tags = results.find_all('ul', class_ = 'prereq')
        c = tags[0].find_all('li')
    except:
        tags = results.find_all('ul', class_ = 'precoreq')
    finally:
        try:
            c = tags[0].find_all('li')
        except:
            return subject, num
        finally:
            pre_reqs = []
            str_pre = ""
            for i in c:
                pre_reqs.append(i.text)
                str_pre += i.text
                str_pre += " " 
            print("PREREQUISITES for",coursename ,"ARE:\n", str_pre)
            return subject, num
main()