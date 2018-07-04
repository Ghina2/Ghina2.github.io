#!/usr/bin/env python
# Python Code for Inputting information ,Creating QR code ,Reading QR code , Searching in database and Deleting Information from MongoDB database.((( classes ))) 

#library for qr code
import qrcode 
#library for mongodb database
from  pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
#from mongothon import Schema
from urllib import quote_plus 
#library for time.sleep
import time
#Project Classes
from generate_class import generating_code
from Scan_class import Scan_QR
from Delete_class import Delete_From_DataBase

if __name__ == "__main__":
	client = pymongo.MongoClient("mongodb://ghina:QR-15-glucoset@cluster0-shard-00-00-usqui.mongodb.net:27017,cluster0-shard-00-01-usqui.mongodb.net:27017,cluster0-shard-00-02-usqui.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	db = client.test
	which_Scan = raw_input ("Enter Ctrl+c to stop the program in any time. \nEnter your scan number : ")
	while (which_Scan == ""):
		which_Scan = raw_input ("Enter your platform number")
		
	if (which_Scan == "1") :
		while True:
			select = raw_input(" Enter G to generate a new QR .\n Enter S to scan a QR code .\n Enter D to delete to delete one document .\n")
			if (select == "G"):
				GGG = generating_code() # class for generate QR code and insert to database
				GGG.Generate(db)
				time.sleep(3)
			elif (select == "S"):
				SSS = Scan_QR () # class for scan code and search for document on database
 				SSS.Scan(db)
				time.sleep(3)
			elif (select== "D") :
				DDD = Delete_From_DataBase () # class for delete document efter scan 
				DDD.Delete_Info(db)
				time.sleep(3)
			else :
				break
						
	else :
		while True:
			SSS = Scan_QR ()
			SSS.Scan(db)
			time.sleep(3)
		