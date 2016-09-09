########################################
# population.py
#
# Written by: John Craver
# Exhibit Technician, Science World British Columbia
#
# Created: 2016-08-24
#
# Hardware:
# CST-E1000 bi-colour dot-matrix LED message display
# has about 7000 characters of message memory (according to the manufacturer)
# RS232 over RJ45, 19200 baud

import font     # separate file stores all of the text appearance parameters
import requests # for HTTP GET requests to obtain population data from online
import serial   # to communicate with the CST-E1000 LED display
import datetime
import time     # for program control and population calculations

ser = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)        # set baudrate to port

# URL to obtain population data from:
url = 'http://api.population.io:80/1.0/population/World/today-and-tomorrow/'

# CST-E1000 delay between messages
incrementInterval = 2333 # 2.333 seconds, verified with scope
numberOfMessages = 300   # max number of messages to store in memory: 7000/(20ish characters per message) = 350, use 300 to be safe;

updateInterval = int(incrementInterval*numberOfMessages/1000) # how long to wait between sending each batch of messages
updateTimer = time.time()       # the time at which to send the next batch of messages

def SendHeader():
        ser.write(serial.to_bytes([0x00,0xFF,0xFF,0x00,0x0B,0x01,0x02,0x03,0x04,0x05,0xFF,0x01,0x30,0x31,font.transition,0xEF,font.textColour,0xEF,font.textSize,0xEF,font.t$
        print("Header")
        return

def SendNewLine():
        ser.write(serial.to_bytes([0xFF,font.transition,0xEF,font.textColour,0xEF,font.textSize,0xEF,font.transitionSpeed]))
        print("NewLine")
        return

def SendFooter():
        ser.write(serial.to_bytes([0xFF,0xFF,0x30,0x31,0xFF,0x00]))
        print("Footer")
        return

def SendTest():
        ser.write(serial.to_bytes([0x00,0xFF,0xFF,0x00,0x0B,0x03,0xFF,0x0A,0x01,0xFF,0x00]))
        return

while True:
        if updateTimer < time.time():
                updateTimer = time.time()+updateInterval

#               SendHeader()
#               ser.write("connecting to:".encode())
#               ser.write(url.encode())
#               SendFooter()

                # get population data
                response = requests.get(url=url)
                data = response.json()
                today = data['total_population'][0]['date']
                tomorrow = data['total_population'][1]['date']
                populationToday = data['total_population'][0]['population']
                populationTomorrow = data['total_population'][1]['population']
                print(populationToday,today)
                print(populationTomorrow,tomorrow)

                # update population variable


                dttimeStartOfDay = datetime.datetime.now()
                dttimeStartOfDay = dttimeStartOfDay.replace(hour = 0, minute = 0, second = 0)
#               dttimeStartOfDay = datetime.datetime.today()
                timeStartOfDay = dttimeStartOfDay.timestamp()

                print(time.time())
#               print(time.mktime(timeStartOfDay.timetuple()))

                timeStartCalculation = time.time()
                timeSinceStartOfDay = timeStartCalculation-timeStartOfDay

                # write next  or so numbers to Serial
                SendHeader()
                for i in range(0,numberOfMessages):
                        population = int(round(populationToday+(populationTomorrow-populationToday)*((timeSinceStartOfDay+i*incrementInterval/1000)/86400) ) )
                        ser.write(str(format(population,",d")).encode())
                        print(format(population,",d"))
                        SendNewLine()
                SendFooter()


