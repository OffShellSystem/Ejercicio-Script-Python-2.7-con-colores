#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands
import time

def rojo(skk): print("\033[91m {}\033[01m" .format(skk))

verde="\x1b[1;32m" 
rojo_var="\x1b[1;31m"
cs_color='\033[0;m'

os.system('sudo apt-get install toilet')
os.system('sudo apt-get install whatweb')

os.system('clear')

time.sleep(0.5)

os.system('toilet -f pagga --gay "OffShell  System"')

print " "

time.sleep(0.5)

print (verde + '-Script de escaneo de dominios-' + cs_color)

time.sleep(0.5)

rojo ('Los dominios albergan información pública\na la que acceder mediante los comandos correctos.')

time.sleep(0.5)

print " "

rojo ('Estescript resume esa información y\nla muestra por pantalla gracias al comando ' + verde + 'WhatWeb.')

time.sleep(0.5)

user = raw_input(verde + 'Analizar ' + rojo_var + '------------ > ' + verde)

whatweb = commands.getoutput('whatweb ' + str(user))

time.sleep(0.5)

print " "

rojo ('Guardando Información  -->  ' + verde + str(user) + cs_color)

time.sleep(0.5)

print " "

rojo ('Procesando ingredientes' + cs_color)

print " "

time.sleep(0.5)

rojo ('WHATWEB \n' + verde + str(whatweb))

print " "

time.sleep(1)

print (rojo_var + 'Estos son los datos públicos resumidos para ' + verde + str(user))
