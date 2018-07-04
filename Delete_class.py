#!/usr/bin/env python
# Python Calss for Scan QR code and delete documents in database which have it 

#library for qr code
import qrcode 
#library for mongodb database
from  pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
#from mongothon import Schema
from urllib import quote_plus 

class Delete_From_DataBase:

	def __init__ (self):
		self.qr_delete = 0
		self.count_id = 0 
		self.searching_delete = 0
		self.searching_delete1 = 0
		self.searching_delete2 = 0
		self.searching_delete3 = 0
		
	def Delete_Info (self,db) :
		self.qr_delete = raw_input(" Enter QR scanning which you want to delete : ")
		self.count_id= len(self.qr_delete)
		while (self.qr_delete == "" or self.count_id != 24):
			self.qr_delete = raw_input(" Invalide QRcode . Try agein : ")
			self.count_id= len(self.qr_delete)
		try :
			self.searching_delete = db.QR.find_one({'_id' : ObjectId(self.qr_delete) },{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})
			self.searching_delete1 = db.QR.find_one({'_id' : ObjectId(self.qr_delete) },{'ArraivalDate' : 1 , '_id': 0})
			self.searching_delete2 = db.QR.find_one({'_id' : ObjectId(self.qr_delete) },{'BatchID' : 1, '_id': 0})
			self.searching_delete3 = db.QR.find_one({'_id' : ObjectId(self.qr_delete) },{'MoreInformation' :1, '_id': 0})
			delete_document = db.QR.delete_one ({'_id' : ObjectId(self.qr_delete)})
			if (self.searching_delete != None) :
				print (self.searching_delete1)
				print ( self.searching_delete2)
				print( self.searching_delete3)					
				print ("Succesfully deleted from database called QR")

			else : 
				print (self.searching_delete)
				print ("This Qr is not on the database . Please retry scanning ")				
		except :
			print ("Error on connecting to the database. Please try to reconnect with internet and try agein")

			