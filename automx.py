#!/usr/bin/env python3
import os
import datetime
import getpass

user_name = getpass.getuser()
dir = '/home/%s/memex/content/data.ndtl'%user_name
date = datetime.date.today()

name = input("Name: ")

if name == "":
	print("[!] Invalid name")

else:
	name_convert = name.upper()
	fron = input("From: ")
	src = input("Src: ")
	fle = input("File: ")
	auth = input("Author: ")
	proj = input("Project: ")
	print("TYPES = {music, list, video, article, lecture, image, book, tool, quote, podcast, term}")
	typ = input("Type: ")
	tag = input("Tag: ")
	link = input("url: ")
	note = input("Note: ")
	done = input("DONE(True = y/Y; False = n/N): ")

	with open(dir, 'r+', encoding = "utf-8") as file:
	    file.seek(0, os.SEEK_END)
	    pos = file.tell() - 1
	    while pos > 0 and file.read(1) != "\n":
	        pos -= 1
	        file.seek(pos, os.SEEK_SET)
	    if pos > 0:
	        file.seek(pos, os.SEEK_SET)
	        file.truncate()
	file.close()

	file = open(dir, 'a')
	file.write("\n%s\n"%name_convert)
	if fron == "":
		pass
	else:
		file.write("  PERS : %s\n"%fron)
	if fle == "":
		pass
	else:
		file.write("  FILE : %s\n"%fle)
	if auth == "":
		pass
	else:
		file.write("  AUTH : %s\n"%auth)
	if proj == "":
		pass
	else:
		file.write("  PROJ : %s\n"%proj)
	if src == "":
		pass
	else:
		file.write("  SRCE : %s\n"%src)
	if typ == "":
		pass
	else:
		file.write("  TYPE : %s\n"%typ)
	if tag == "":
		pass
	else:
		file.write("  TAGS : %s\n"%tag)
	if note == "":
		pass 
	else:
		file.write("  NOTE : '%s'\n"%note)
	if link == "":
		pass 
	else:
		file.write("  LINK : %s\n"%link)
	if done == "y" or done == "Y":
		file.write("  DONE : true\n")
	elif done == "n" or done == "N":
		file.write("  DONE : false\n")
	else:
		file.write("  DONE : false\n")

	file.write("  DATE : %s\n"%date)
	file.write("\n`\n")
	file.close()

'''
reference:
	https://pt.stackoverflow.com/questions/360474/apagar-a-ultima-linha-de-um-arquivo-txt

thank you <3

'''
