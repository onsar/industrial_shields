import subprocess
import time
import os
import paho.mqtt.publish as publish

import configparser

import logging
from logging.handlers import RotatingFileHandler


# Para obtener mas detalle: level=logging.DEBUG
# Para comprobar el funcionamiento: level=logging.INFO
logging.basicConfig(
        level=logging.INFO,
        handlers=[RotatingFileHandler('./logs/log_inputs.log', maxBytes=1000000, backupCount=10)],
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

# Parseo de variables del .ini
parser = configparser.ConfigParser()
parser.read('config_outputs.ini')

# Parseo de las variables de emonCMS
mqtt_topic = parser.get('listener','topic')
listener_name = parser.get('listener','name')
mqtt_ip = parser.get('listener','mqtt_ip')
mqtt_login = parser.get('listener','mqtt_login')
mqtt_password = parser.get('listener','mqtt_password')



a_sensors = ["I0.7","I0.8","I0.9","I0.10","I0.11","I0.12"]
d_sensors = ["I0.0","I0.1","I0.2","I0.3","I0.4","I0.5","I0.6"]


if __name__ == "__main__":
    logging.info("Start entradas")
    while 1:
        for sensor in a_sensors:
            result ="ok"
            xout="no_response"
            try:
                x = subprocess.run(["/home/pi/test/analog/get-analog-input",sensor], stdout=subprocess.PIPE, text=True)
                xout = x.stdout

            except:
                result = "time_out"
                logging.info("time_out get-analog-input")
            
            if result == 'ok':
                logging.info(sensor)
                logging.info(xout)
                publish.single("a_sensor/" + sensor, xout, hostname="localhost")  
                
        for sensor in d_sensors:
            result ="ok"
            x="no_response"
            try:
                x = subprocess.run(["/home/pi/test/analog/get-digital-input",sensor], stdout=subprocess.PIPE, text=True)
                xout = x.stdout
                
            except:
                result = "time_out"
                logging.info("time_out get-digital-input")
                
            if result == 'ok':
                logging.info(sensor)
                logging.info(xout)
                publish.single("d_sensor/" + sensor, xout, hostname="localhost")  
                

        
        time.sleep(4)
            





