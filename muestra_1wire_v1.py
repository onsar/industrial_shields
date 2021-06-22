#!/usr/bin/python
# -*- coding: utf-8 -*-


import time

import os
import paho.mqtt.publish as publish

devices_dir = '/sys/bus/w1/devices'

contenido = os.listdir(devices_dir)

sondas = []

for fichero in contenido:
    if os.path.islink(os.path.join(devices_dir, fichero)) and fichero.startswith('28-'):
       # sondas.append(os.path.join(devices_dir, fichero))
       sondas.append(os.path.join(os.path.join(devices_dir, fichero),'w1_slave'))
print(contenido)
print(sondas)

last_exec = time.time()

while 1:
    if time.time()- last_exec > 9:
        last_exec = time.time()
        
        for sonda in sondas:
            result = 'ok'
            try:
                sonda_name = sonda.split("/")[5]
                sonda_name = sonda_name[9:15]
                
                sonda_file = open(sonda,'r')
                sonda_text = sonda_file.read()
                sonda_file.close()
                
                sonda_temper = sonda_text.split("\n")[1].split(" ")[9]
                sonda_temper = float(sonda_temper[2:])
                sonda_temper = sonda_temper/1000
                sonda_temper = round(sonda_temper,1)
                
            except:
                result="time_out"
                
            if result == 'ok':
                print(sonda_name)
                print(sonda_temper)
                publish.single(sonda_name, sonda_temper, hostname="localhost")

    
    
    
    

