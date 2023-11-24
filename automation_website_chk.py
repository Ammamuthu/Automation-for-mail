import time
import requests
import logging
import smtplib

# Logg File settup

logging.basicConfig(filename='Shed.log',  format='%(asctime)s - %(message)s' ,datefmt='%d-%m-%y %H:%M:%S')
log =[]

# Mail setup
smtpServer = '121.243.77.117'
smtpPort = 587  # Port for TLS
fromAddr = 'ammamuthu.m@3i-infotech.com'
toAddr = 'ammamuthu.m@3i-infotech.com'
paswrd = 'Aura@123'

server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()

server.login(fromAddr,paswrd )

# Actual setup

while True:
    def check_website_status(websites):
        for website in websites:
            try:
                response = requests.get(website)
            
                if response.status_code == 200:
                    logging.warning(f"{website} is alive (Status Code: {response.status_code})")
                elif response.status_code == 500:
                    logging.warning(f"{website} returned a 500 Internal Server Error")
                    logging.warning(response.text)  # Print the response content for debugging
                else:
                    logging.warning(f"{website} returned an unexpected status code: {response.status_code}")
            except requests.RequestException as e:
                logging.warning(f"{website} is not reachable. Exception: {e}")

# List of websites to check
    websites_to_check = [
    
    "https://www.google.com",
    "http://erpuat.najrancement.local:8012/OA_HTML/AppsLogin",    #17 server
    "http://erptest.najrancement.local:8012/OA_HTML/AppsLogin",   #16 server -R12.2.10
    "http://erpdev.najrancement.local:8000/",                     #78 server
    "http://erpdev.najrancement.local:8028/",                     #16 server iteration2
    ]

# Run the check
    check_website_status(websites_to_check)
    logging.warning("......................................")

    print("Executing the script...")
    time.sleep(1500)

server.quit()
