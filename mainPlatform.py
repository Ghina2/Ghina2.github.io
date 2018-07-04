#!/usr/bin/env python
# Code for Inputting information ,Creating QR code ,Reading QR code , Searching in database and Deleting Information from MongoDB database.

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
	user_name = raw_input (" Enter Ctrl+c to stop the program in any time. \n Enter your user name : ")
	while (user_name == ""):
		user_name = raw_input (" Enter your user name : ")
	
	if (user_name == "1") :
		reqest = raw_input(" Enter n for New QR Code and new insert to database. \n Enter s for Scanning QR code. \n Enter d to delet one document . \n Enter any kay else to stop the program. \n")
		while (reqest != " ") :
			arrival_date = 0
			batch_id= 0
			qr_information= 0
			QRCodeCollection= 0
			idnumber = None
			result= 0
			qr= 0
			img= 0
			searching_scan=0
			count_id = 0
			qr_update=0
			searching_update=0
			qr_delete=0
			searching_delete=0
			delete_document=0
			show_all=0
			s=0
			
			##create new collection
			if (reqest == "n") :
				arrival_date = raw_input(" Enter Arrival Date : ")
				while (arrival_date == ''):
					arrival_date = raw_input(" Enter Arrival Date : ")
				batch_id = raw_input(" Enter Batch ID : ")
				while (batch_id == ''):
					batch_id = raw_input(" Enter Batch ID : ")
				qr_information = raw_input(" Add more Information : ")
				QRCodeCollection = {'ArraivalDate' : arrival_date ,'BatchID' : batch_id,'MoreInformation' : qr_information}
				try :
					result = db.QR.insert_one(QRCodeCollection)
					idnumber = result.inserted_id
					print ("Succesfully inserted to database called QR")
					searching_scan = db.QR.find_one({'_id': ObjectId(idnumber)},{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})
					print idnumber
					try :
						qr = qrcode.QRCode(version=1 , error_correction=qrcode.constants.ERROR_CORRECT_L , box_size=1 , border=2)
						#img = qrcode.make(idnumber) # simple QR code							
						qr.add_data(idnumber)
						qr.make(fit=True)
						img = qr.make_image(fill_color="black", back_color="white")
						img.show() ################################################################ it isn't working in ubuntu
						print ("QR code is ready to print")	
						time.sleep(5)
						reqest = raw_input(" Enter n for New QR Code and new insert to database. \n Enter s for Scanning QR code. \n Enter d to delet one document . \n Enter any kay else to stop the program. \n ")

					except : 
						print("There is a problem with Generate New QR . Try agein please ")
						break
				
				except :
					print ("Error on connecting to the database. Please try to reconnect with internet and try agein ")
					break

			##scan QR and read collection from database
			elif (reqest == "s") :
				idnumber= raw_input(" Enter QR scanning : ")
				count_id= len(idnumber)
				while (idnumber=="" or count_id != 24):
					idnumber = raw_input(" Invalide QRcode . Try agein : ")
					count_id = len(idnumber)
				searching_scan1 = db.QR.find_one({'_id': ObjectId(idnumber)},{'ArraivalDate' : 1 , '_id': 0})
				searching_scan2 = db.QR.find_one({'_id': ObjectId(idnumber)},{'BatchID' : 1, '_id': 0})
				searching_scan3 = db.QR.find_one({'_id': ObjectId(idnumber)},{'MoreInformation' :1 ,'_id': 0})
				searching_scan = db.QR.find_one({'_id': ObjectId(idnumber)},{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})

				if searching_scan1 and  searching_scan2 and searching_scan3 :
					print(searching_scan1)
					print(searching_scan2)
					print(searching_scan3)
					time.sleep(5)
					reqest = raw_input(" Enter n for New QR Code and new insert to database. \n Enter s for Scanning QR code. \n Enter d to delet one document . \n Enter any kay else to stop the program. \n ")
						
				elif (searching_scan == None) :
					print (searching_scan1,searching_scan2,searching_scan3)
					print ("This QR code is not in database")
					time.sleep(5)
					reqest = raw_input(" Enter n for New QR Code and new insert to database. \n Enter s for Scanning QR code. \n Enter d to delet one document . \n Enter any kay else to stop the program. \n ")

				else :
					print("Error on connecting to the database or in scanning the QR. Please try to reconnect with internet and try agein")
					break
			
			##Delete collection from database
			elif (reqest == "d") :
				qr_delete = raw_input(" Enter QR scanning which you want to delete : ")
				count_id= len(qr_delete)
				while (qr_delete == "" or count_id != 24):
					qr_delete = raw_input(" Invalide QRcode . Try agein : ")
					count_id= len(qr_delete)
				print qr_delete
				try :
					searching_delete = db.QR.find_one({'_id' : ObjectId(qr_delete) },{'ArraivalDate' : 1 ,'BatchID' : 1,'MoreInformation' :1})
					searching_delete1 = db.QR.find_one({'_id' : ObjectId(qr_delete) },{'ArraivalDate' : 1 , '_id': 0})
					searching_delete2 = db.QR.find_one({'_id' : ObjectId(qr_delete) },{'BatchID' : 1, '_id': 0})
					searching_delete3 = db.QR.find_one({'_id' : ObjectId(qr_delete) },{'MoreInformation' :1, '_id': 0})
					delete_document = db.QR.delete_one ({'_id' : ObjectId(qr_delete)})
					if (searching_delete != None) :
						#print("%s \n , %s \n ,%s \n ". searching_delete1,searching_delete2,searching_delete3 )
						print (searching_delete1)
						print ( searching_delete2)
						print( searching_delete3)
						print ("Succesfully deleted from database called QR")
						time.sleep(5)
						reqest = raw_input(" Enter n for New QR Code and new insert to database. \n Enter s for Scanning QR code. \n Enter d to delet one document . \n Enter any kay else to stop the program. \n")
					else :
						print (searching_delete)
						print ("This Qr is not on the database . Please retry scanning ")
						reqest = raw_input(" Enter n for New QR Code and new insert to database. \n Enter s for Scanning QR code. \n Enter d to delet one document . \n Enter any kay else to stop the program. \n")
				
				except :
					print ("Error on connecting to the database. Please try to reconnect with internet and try agein")
					break
			else :
				break 
				
	else :
		print ("SORRY YOU ARE NOT ALLOWED TO ACCESS")

	
	