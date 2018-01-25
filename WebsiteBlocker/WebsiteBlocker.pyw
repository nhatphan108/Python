import time
from datetime import datetime as dt
import ctypes, sys
from admin import run_as_admin
from admin import is_admin
if is_admin():
    hosts_path= r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    with open("websites.txt","r+") as w:
        website_list = w.readlines()
        w.close()
    with open("time.txt","r+") as t:
        timeframe = t.readlines()
        t.close()
    website_list = [i.rstrip("\n") for i in website_list]
    timeframe=[i.rstrip("\n") for i in timeframe]
    while True:
            if dt(dt.now().year,dt.now().month,dt.now().day,int(timeframe[0])) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,int(timeframe[1])):
                print("Working hours...")
                with open(hosts_path,'r+') as file:
                    content = file.read()
                    for website in website_list:
                        if website in content:
                            pass
                        else:
                            file.write(redirect+ " " + website + "\n")
            else:
                with open(hosts_path,'r+') as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
                print("Fun hours")
            time.sleep(5)
else:
    run_as_admin("WebsiteBlocker.pyw")
