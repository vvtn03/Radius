import requests
import json
with open('HTMLFILE.html', 'r') as f:
    f.read()


from bs4 import BeautifulSoup
f = open('HTMLFILE.html', 'r')
s = f.read()
soup = BeautifulSoup(s,'html.parser')
results=soup.findAll('td')


for idx,item in enumerate(results):
    if "leads@email.realtor.com" in str(item):
        emailidx = idx

        for idx, item in enumerate(results):
            if "Test Lead" in str(item):
                nameidx = idx

                for idx, item in enumerate(results):
                    if "111-222-3333" in str(item):
                        phoneidx = idx


emailrecord=results[emailidx]
email=str(emailrecord.find('a'))


namerecord=results[nameidx]
name=namerecord.find('strong').text


phonerecord=str(results[phoneidx])
phone=phonerecord[390:402]


records=[]
records.append(email[89:112])
records.append(name)
records.append(phone)



jsondict = { "Name": [  records[1]],
             "Email" :  [ records[0] ],
              "Phone": [  records[2]]
           }
print(jsondict)






