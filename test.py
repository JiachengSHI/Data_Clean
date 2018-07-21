# -*- coding: utf-8 -*- 
import os
import io
from Check import Check
from Patient import Patient

f = open('data.txt', 'r+')
title = f.readline()
his = f.read()
target = "铂"

p_list = {}
for line in his.split('\n'):
	id = line.split('\t', 1)[0]
	if id not in p_list.keys():
		P = Patient(line)
		p_list[id] = P
	else:
		C = Check(line.split('\t', 1)[1])
		p_list[id].Check_list.append(C)

for key,value in p_list.items():
	#print value.id
	for record in value.Check_list:
		#print record.Treat
		if value.first_treat == False:
			if record.Treat != "None":
				#first treatment
				value.first_treat = True
				if '+' in record.Treat:
					t_ct = 0
					medinces = record.Treat.split('+')
					for m in medinces:
						if target in m:
							t_ct = t_ct + 1
					if t_ct > 0 and t_ct < len(medinces):
						value.treament_line = True
					break
				else:
					break
			else:
				pass
		else:
			break

result = []
"""
for key,value in p_list.items():
	if value.treament_line:
		for record in value.Check_list:
			result.append(value.id + '\t' + record.EGFR + '\t' + record.ALK + '\t' + record.Wrose + '\t' + record.WroseLabel + '\t' + record.Treat + '\tTarget')
	else:
		for record in value.Check_list:
			result.append(value.id + '\t' + record.EGFR + '\t' + record.ALK + '\t' + record.Wrose + '\t' + record.WroseLabel + '\t' + record.Treat + '\tDrop')
"""

for line in his.split('\n'):
	id = line.split('\t', 1)[0]
	if p_list[id].treament_line:
		result.append(line + '\tTarget')
	else:
		result.append(line + '\tDROP')

#Export
with open('Result.txt', 'wb') as file:
	file.write("%s" % title)
	for r in result:
		file.write("%s\n" % r)