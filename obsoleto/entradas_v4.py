import subprocess
import time
import os
import paho.mqtt.publish as publish

def str2dec(string):
	return (string[0:-1])

def adc(value):
	return (10*int(str2dec(value)))/4096

a_sensors = ["I0.7","I0.8","I0.9","I0.10","I0.11","I0.12"]
d_sensors = ["I0.0","I0.1","I0.2","I0.3","I0.4","I0.5","I0.6"]


if __name__ == "__main__":
    print("Start")
    while 1:
        for sensor in a_sensors:
            result ="ok"
            xout="no_response"
            try:
                x = subprocess.run(["/home/pi/test/analog/get-analog-input",sensor], stdout=subprocess.PIPE, text=True)
                xout = x.stdout

            except:
                result = "time_out"
            
            if result == 'ok':
                print(sensor)
                print(xout)
                publish.single("a_sensor/" + sensor, xout, hostname="localhost")  
                
        for sensor in d_sensors:
            result ="ok"
            x="no_response"
            try:
                x = subprocess.run(["/home/pi/test/analog/get-digital-input",sensor], stdout=subprocess.PIPE, text=True)
                xout = x.stdout
                
            except:
                result = "time_out"
                
            if result == 'ok':
                print(sensor)
                print(xout)
                publish.single("d_sensor/" + sensor, xout, hostname="localhost")  
                

        
        time.sleep(4)
            





