import subprocess
import time

def str2dec(string):
	return (string[0:-1])

def adc(value):
	return (10*int(str2dec(value)))/4096

a_sensors = ["I0.7","I0.8","I0.9","I0.10","I0.11","I0.12"]
d_sensors = ["I0.0","I0.1","I0.2","I0.3","I0.4","I0.5","I0.6"]


if __name__ == "__main__":
    print("Start")
    while 1:
        result ="ok"
        try:
            for sensor in a_sensors:
                print(sensor)
                x = subprocess.run(["/home/pi/test/analog/get-analog-input",sensor], stdout=subprocess.PIPE, text=True)
                print(x.stdout)

        except:
            result = "time_out"
        
        result ="ok"
        try:
            for sensor in d_sensors:
                print(sensor)
                x = subprocess.run(["/home/pi/test/analog/get-digital-input",sensor], stdout=subprocess.PIPE, text=True)
                print(x.stdout)
    
        except:
            result = "time_out"
        
        time.sleep(4)
            





