#!/usr/bin/env python
# Python Calss for Scan QR code and search for documents in database for it 

#library for qr code
import qrcode 
#library for mongodb database
from  pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
from urllib import quote_plus 

class Scan_QR :

	def __init__ (self):
		self.idnumber = 0
		self.count_id = 0
		self.searching_scan = 0
		self.searching_scan1=0
		self.searching_scan2=0
		self.searching_scan3=0

	def Scan (self,db) :
		self.idnumber= raw_input(" Enter QR scanning : ")
		self.count_id= len(self.idnumber)
		while (self.idnumber=="" or self.count_id != 24):
			self.idnumber = raw_input(" Invalide QRcode . Try agein : ")
			self.count_id = len(self.idnumber)
		try :
			self.searching_scan = db.QR.find_one({'_id': ObjectId(self.idnumber)},{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})
			self.searching_scan1 = db.QR.find_one({'_id': ObjectId(self.idnumber)},{'ArraivalDate' : 1 , '_id': 0})
			self.searching_scan2 = db.QR.find_one({'_id': ObjectId(self.idnumber)},{'BatchID' : 1, '_id': 0})
			self.searching_scan3 = db.QR.find_one({'_id': ObjectId(self.idnumber)},{'MoreInformation' :1 ,'_id': 0})
			if (self.searching_scan == None) :
				print(self.searching_scan)
				print ("This QR code is not in database , Please retry ")
			else :
				print(self.searching_scan1)
				print(self.searching_scan2)
				print(self.searching_scan3)			
		except :
			print("Error on connecting to the database or in scanning the QR. Please try to reconnect with internet and try agein")
			
		