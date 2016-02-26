#!/usr/bin/env python
# -*-coding:utf-8-*-

import time
from time import sleep
import random

sus = "_" * 35
depo = ["piedra","papel", "tijeras"]

while True:
	x = raw_input("Que elijes? Piedra, Papel, Tijeras : ")
	if x not in depo:
		print("No hagas trampa!!")
		continue
	
	pc= random.choice(depo)
	sleep(0.5)
	print(("COmputadora eligio {}.").format(pc))
	if x == pc :
		print("\nEmpate.")
	elif x == "piedra" and pc == "tijeras":
		print("\nGanaste.")
	elif x == "papel" and pc == "piedra":
		print("\nGanaste.")
	elif x == "tijeras" and pc == "papel":
		print("\Ganaste.")
	else:
		print("Perdimos. {} gana {}".format(pc,x))
	print sus 