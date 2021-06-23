import subprocess
import time

def str2dec(string):
	return (string[0:-1])

def adc(value):
	return (10*int(str2dec(value)))/4096

sensores = ["I0.7","I0.8","I0.12"]

if __name__ == "__main__":
    print("Start")
    while 1:      
        for sensor in sensores:
            print(sensor)
            try:
                x = subprocess.run(["/home/pi/test/analog/get-analog-input",sensor], stdout=subprocess.PIPE, text=True)
                print(adc(x.stdout))
                time.sleep(4)
            except KeyboardInterrupt:
                print("\nExit")
                break
        


