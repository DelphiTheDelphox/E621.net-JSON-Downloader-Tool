import requests
import os
import time
import json

from pip._vendor.distlib.compat import raw_input

with open("queue.txt", "w+") as out:
    out.write("allclear")


print("Welcome to E621.net json downloader tool v0.1")
filepath = r""

if(filepath == ""):
    print("Please input directory")
    filepath = raw_input(">>>")

directory = os.listdir(filepath)
temp = directory[0]
temp = temp[:-4]
i = 0
try:
    test = int(temp) % 50
except TypeError:
    print("Error files in incorrect format. \nFiles in directory must be in <ID Number>.<File Extension> ex. 560858.jpg \n If you're using this program you probably have images in this format anyway. Double check if the directory is correct.")

useragent = "delphithedelphox"
login = "delphithedelphox"
api_key = "xxLysKC8fs5UYEnwi4BXrcYc"





if(login == ""):
    print("Please input your E621.net username")
    login = input(">>>")

if(useragent == ""):
    print("Please input the User-Agent name you wish to use (Press enter for default)")
    useragent = input(">>>")
    if(useragent == ""):
        useragent = login + " Using delphithedelphox JSON downloader"

if(api_key == ""):
    print("Please input your E621.net API Key (This can be enabled through your account options, but if you're here you probably know what you're doing")
    login = input(">>>")

url = "http://e621.net"

headers = {
        'User-Agent': useragent,
        'login': login,
        'api_key': api_key,

}

r = requests.get(url, headers=headers)

if(r.status_code == 200):
    print("Login successful...")
else:
    print("Login failed. Error code: " + str(r.status_code))




with open("queue.txt", "r") as out:
    value = out.read()
    if(value !="allclear"):
        i = int(value)
        print("Recovering from improper shut down... \nRestarting from file number: " + value)


def poll_api(postid):
    url = 'https://e621.net/posts.json?tags=id:' + str(postid)

    headers = {
        'User-Agent': useragent,
        'login': login,
        'api_key': api_key,

    }

    r = requests.get(url, headers=headers)
    count = 0
    while r.status_code != 200:
        time.sleep(10)
        r = requests.get(url, headers=headers)
        if (count > 10):
            time.sleep(600)

    with open(str(postid) + ".json", "w") as outfile:
        json.dump(r.json(), outfile)
    return r.status_code


#poll_api(2731661)
base = time.time()
avlist = [1, 1, 1, 1, 1, 1, 1, 1, 1]
lasttime = 0
while(i != len(directory)):
    directory[i] = directory[i][:-4]
    statc = poll_api(directory[i])
    time.sleep(0.8)
    t = time.time() - base
    avlist.append(t-lasttime)
    if (len(avlist) == 11):
        del avlist[0]
    if (i%100==0):
        with open("queue.txt", "w") as out:
            out.write(str(i))
            print("Queue backup saved, current backup location: " + str(i))




    average = (avlist[0]+avlist[1]+avlist[2]+avlist[3]+avlist[4]+avlist[5]+avlist[6]+avlist[7]+avlist[8]+avlist[9])/10
    average = round(average, 3)
    print("Iteration:" + str(i) + " ||| Posts Remaining: " + str((len(directory) - i)) + " ||| Time Passed: " + str(int(t)) + " ||| Average Time: " + str(average) + " ||| Estimated Time Remaining: " + str(int((len(directory) - i) * average)) + " Seconds ||| E621 ID: " + str(directory[i]) + " ||| Status Code: " + str(statc))
    lasttime = t
    i = i + 1
    if(i==len(directory)):
        with open("queue.txt", "w") as out:
            out.write("allclear")
        print("Image queue complete, writing status to file. \nPress any key to continue...")
        input()




#print(directory)
