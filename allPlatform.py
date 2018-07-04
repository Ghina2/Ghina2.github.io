#!/usr/bin/env python
#This code is for Reading QR code and Searching in MongoDB database.

#library for qr code
import qrcode 

#library for mongodb database
from  pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

from urllib import quote_plus 

import time 

if __name__ == "__main__":
	client = pymongo.MongoClient("mongodb://ghina:QR-15-glucoset@cluster0-shard-00-00-usqui.mongodb.net:27017,cluster0-shard-00-01-usqui.mongodb.net:27017,cluster0-shard-00-02-usqui.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	db = client.test
	while True:
		idnumber=0
		count_id=0
		searching_scan = None
		idnumber= raw_input("You can enter Ctrl+c in any time to stop the program \n Enter QR scanning : ")
		count_id= len(idnumber)
		while (idnumber=="" or count_id != 24):
			idnumber = raw_input("Invalide QRcode . Try agein : ")
			count_id = len(idnumber)
		searching_scan1 = db.QR.find_one({'_id': ObjectId(idnumber)},{'ArraivalDate' : 1 , '_id': 0})
		searching_scan2 = db.QR.find_one({'_id': ObjectId(idnumber)},{'BatchID' : 1, '_id': 0})
		searching_scan3 = db.QR.find_one({'_id': ObjectId(idnumber)},{'MoreInformation' :1, '_id': 0})
		searching_scan = db.QR.find_one({'_id': ObjectId(idnumber)},{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})

		if searching_scan :
			print(searching_scan1)
			print(searching_scan2)
			print(searching_scan3)
					
			time.sleep(10)
						
		elif (searching_scan == None) :
			print(searching_scan)
			print ("This QR code is not in database")
			time.sleep(10)

		else :
			print("Error on connecting to the database or in scanning the QR. Please try to reconnect with internet and try agein")
			break
			