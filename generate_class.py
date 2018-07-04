#!/usr/bin/env python
# Python Calss for insert document on database and generate QR code for it 

#library for qr code
import qrcode 
#library for mongodb database
from  pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
#from mongothon import Schema
from urllib import quote_plus 

class generating_code:
	def __init__ (self): 
		self.arrival_date = 0
		self.batch_id = 0 
		self.qr_information = 0
		self.QRCodeCollection = 0
		self.result = 0 
		self.idnumber = 0 
		self.searching_scan = 0 
		self.qr = 0 
		
	def Generate (self,db):
		self.arrival_date = raw_input(" Enter Arrival Date : ")
		while (self.arrival_date == ''):
			self.arrival_date = raw_input(" Enter Arrival Date : ")
		self.batch_id = raw_input(" Enter Batch ID : ")
		while (self.batch_id == ''):
			self.batch_id = raw_input(" Enter Batch ID : ")
		self.qr_information = raw_input(" Add more Information : ")
		self.QRCodeCollection = {'ArraivalDate' : self.arrival_date ,'BatchID' : self.batch_id,'MoreInformation' : self.qr_information}
		try :
			self.result = db.QR.insert_one(self.QRCodeCollection)
			self.idnumber = self.result.inserted_id
			print ("Succesfully inserted to database called QR")
			self.searching_scan = db.QR.find_one({'_id': ObjectId(self.idnumber)},{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})
			print (self.idnumber)
			try :
				self.qr  = qrcode.QRCode(version=1 , error_correction=qrcode.constants.ERROR_CORRECT_L , box_size=1 , border=2)
				#img = qrcode.make(self.idnumber) # simple QR code
				self.qr.add_data(self.idnumber)
				self.qr.make(fit=True)
				img = self.qr.make_image(fill_color="black", back_color="white")
				img.show() ################################################################ it isn't working in ubuntu
				print ("QR code is ready to print")	
			except : 
				print("There is a problem with Generate New QR . Try again please ")
		except :
			print ("Error on connecting to the database. Please try to reconnect with internet and try again ")
						