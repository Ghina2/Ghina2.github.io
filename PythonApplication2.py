#!/usr/bin/env python

# interface for Inputting information ,Creating QR code ,Reading QR code , Searching in database , Deleting Information , and Adding new information for MongoDB database.

#GUI libraries
from Tkinter import *
from ScrolledText import *

#QR code libraries
import qrcode
#from qrcode.image.pure import PymagingImage

#Mongodb libraries
from  pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

from random import randint



class Application (Frame):
    def __init__ (self,master) :
        # Initialize the Frame
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        #InPutFrame = Frame (master)
        #InPutFrame.grid(row = 0, column = 0, sticky = W+E+N+S)
        #ScanningFrame = Frame (master)
        #ScanningFrame.grid(row = 0, column = 4, sticky = W+E+N+S)

    def create_widgets(self) :
        # Create the Buttons , Labels , Picture Box , Text Box
        
       ##########Input Part###########

       #Create Label Input Part
        self.InputLabel = Label(self, text = "Input Part\n")
        self.InputLabel.grid(row = 1 , column = 2 , columnspan = 2 , sticky = W )
       
       ##Create Label Inter Number 
        self.InterNumberLabel= Label(self ,  text =" Inter Number : \n")
        self.InterNumberLabel.grid(row = 3 , column = 0 , columnspan = 2 , sticky = W )
       
       #Create Entry Box Inter Number
        self.InterNumberbox = Entry (self , width = 30 , font=("Helvetica Neue", 14))
        self.InterNumberbox.grid(row = 3 , column = 2 , sticky = W )
        
       ##Create Label Inter Arrival Date 
        self.InterArrivalDateLabel= Label(self ,  text =" Inter Arrival Date :\n")
        self.InterArrivalDateLabel.grid(row = 4, column = 0 , columnspan = 2 , sticky = W )
        
        #Create Entry Box Inter Arrival Date
        self.InterArrivalDateBox = Entry (self , width = 30 , font=("Helvetica Neue", 14))
        self.InterArrivalDateBox.grid(row = 4 , column = 2 , sticky = W )
        
        ##Create Label Inter Batch ID 
        self.InterBatchIDLabel= Label(self ,  text =" Inter Batch ID : \n")
        self.InterBatchIDLabel.grid(row = 5, column = 0 , columnspan = 2 , sticky = W )
        
        #Create Entry Box Inter Batch ID 
        self.InterBatchIDBox = Entry (self , width = 30 , font=("Helvetica Neue", 14))
        self.InterBatchIDBox.grid(row = 5 , column = 2 , sticky = W )
        
        ##Create Label Inter More Information
        self.InterMoreInformationLabel= Label(self ,  text =" Inter More Information : \n")
        self.InterMoreInformationLabel.grid(row = 6, column = 0 , columnspan = 2 , sticky = W )
        
        #Create ScrolledText Box Inter More Information
        self.InterMoreInformationBox = ScrolledText(self ,  width = 40, height = 10 , font = ("Helvetica Neue", 12) )
        self.InterMoreInformationBox.grid(row = 6 , column = 2 , sticky = W )
        
        #Create Image Box For QR Code ( Label )
        #self.ImageBoxForQRCode = PhotoImage (self)
        #self.ImageBoxForQRCode.grid(row = 6 , column = 1 , sticky = W )



        #Create QR Button
        self.QRButton = Button(self , height = 7)
        self.QRButton["text"] = "                             Create New QR Code                             "
        self.QRButton.grid(row = 8 , column = 2 , sticky = W )
        self.QRButton["command"] = self.CreateNewQR

        #Create Add to Database Button 
        self.AddToDatabaseButton = Button (self,height = 7)
        self.AddToDatabaseButton["text"] = "                                Add to Database                                 "
        self.AddToDatabaseButton.grid(row = 7 , column = 2 , sticky = W)
        self.AddToDatabaseButton["command"] = self.AddToDatabase
        
        
         ########Scanning Part############

        #Create Label Scanning Part
        self.ScanningLabel = Label(self, text = "     Scanning Part\n")
        self.ScanningLabel.grid(row = 1 , column = 6 , columnspan = 2 , sticky = W )

        #Create Label QR Scann code 
        self.QRScannCodeLabel = Label (self , text = "     QR Scann Code : \n")
        self.QRScannCodeLabel.grid(row = 3 , column = 4 , columnspan = 2 , sticky = W)

        #Create Entry Box QR Scann code
        self.ScanBox = Entry (self , width = 30 , font=("Helvetica Neue", 14))
        self.ScanBox.grid(row = 3 , column = 6 , sticky = W )

        ##Create Label Arrival Date 
        self.ArrivalDateLabel= Label(self ,  text = "     Arrival Date : \n")
        self.ArrivalDateLabel.grid(row = 4, column = 4 , columnspan = 2 , sticky = W )

        #Create Text Box Arrival Date
        self.ArrivalDateBox = Text (self , width = 30,  height = 1 , font=("Helvetica Neue", 14))
        self.ArrivalDateBox.grid(row = 4 , column = 6 , sticky = W )
        
        ##Create Label Batch ID 
        self.BatchIDLabel= Label(self ,  text ="     Batch ID : \n")
        self.BatchIDLabel.grid(row = 5, column = 4 , columnspan = 2 , sticky = W )

        #Create Text Box Batch ID 
        self.BatchIDBox = Text (self , width = 30 ,height = 1, font = ("Helvetica Neue", 14))
        self.BatchIDBox.grid(row = 5 , column = 6 , sticky = W )
        
        ##Create Label More Information
        self.MoreInformationLabel= Label(self ,  text ="     More Information : \n")
        self.MoreInformationLabel.grid(row = 6, column = 4 , columnspan = 2 , sticky = W )
        
        #Create Text Box More Information
        #self.MoreInformationBox = Entry (self , width = 30, font=("Helvetica Neue", 12))
        self.MoreInformationBox = Text (self ,  width = 40, height = 10 , font = ("Helvetica Neue", 12) )
        self.MoreInformationBox.grid(row = 6 , column = 6 , sticky = W )

        #Create Label Add More Information 
        self.AddMoreInformationLabel= Label(self ,  text ="Add More Information : \n")
        self.AddMoreInformationLabel.grid(row = 7, column = 4 , columnspan = 2 , sticky = W )

        #Create ScrolledText Box Add More Information
        self.AddMoreInformationBox = ScrolledText(self ,  width = 40, height = 10 , font = ("Helvetica Neue", 12) )
        self.AddMoreInformationBox.grid(row = 7 , column = 6 , sticky = W )

        #Create Button Bring Information
        self.BringInformationButton = Button (self , height = 2)
        self.BringInformationButton["text"] = "Bring \nInformation"
        self.BringInformationButton.grid(row = 3 , column = 7 , sticky = W )
        self.BringInformationButton["command"] = self.BringInformation

        #Create Add New to Database Button 
        self.AddNewToDatabaseButton = Button (self , height = 7)
        self.AddNewToDatabaseButton["text"] = "Add\n New \n Information \n to Database"
        self.AddNewToDatabaseButton.grid(row = 7 , column = 7 , sticky = W)
        self.AddNewToDatabaseButton["command"] = self.AddNewToDatabase

        #Create Button Delete The Information for this QR code 
        self.DeleteTheInformationForThisQRCodeButton = Button (self , height = 5)
        self.DeleteTheInformationForThisQRCodeButton["text"] = "      Delete The Information For This QR Code      "
        self.DeleteTheInformationForThisQRCodeButton.grid(row = 8 , column = 6 , sticky = W)
        self.DeleteTheInformationForThisQRCodeButton["command"] = self.DeleteTheInformationForThisQRCode


    
       ############ Buttones Programes ################
	 ##get entry data function
	def get_input_entry_data (self):
		self.QRNumberM = self.InterNumberbox.get()
		self.ArraivalDateM = self.InterArrivalDateBox.get()
        self.BatchIDM = self.InterBatchIDBox.get()
        self.MoreInformationM = self.MoreInformationBox.get("1.0", "end-1c")
		
	def get_scan_entry_data (self):
		self.ScanBoxM = self.ScanBox.get()
		self.AddMoreInformationBoxM = self.AddMoreInformationBox.get("1.0", "end-1c")
		
		
		
     ##Create New QR Code Bottun Function . It will create the QR code and shows it as bmp Image
    def CreateNewQR(self):
        #self.qrimg = qrcode.make(self.QRNumberM)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10 , border=4,)
        qr.add_data(self.QRNumberM)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.show()
        
    
    ##Add to Database Bottun Function
    def AddToDatabase (self):
        #client = MongoClient(port=27017) # Establishing a Connection with Mongo
        #db=client.QRCodeCollection       #Accessing Database
        #QRCode = db.QRCode
		client = pymongo.MongoClient("mongodb://ghina:QR-15-glucoset@cluster0-shard-00-00-usqui.mongodb.net:27017,cluster0-shard-00-01-usqui.mongodb.net:27017,cluster0-shard-00-02-usqui.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	#	db = client.test
	#	QRCodeCollection=0
    #   QRCodeCollection = { 'QRNumber' : self.QRNumberM , 'ArraivalDate' : self.ArraivalDateM , 'BatchID' : self.BatchIDM , 'MoreInformation' : self.MoreInformationM }
    #   InsertNewDocument = db.QR.insert_one(QRCodeCollection)

    
    ##Bring Information Bottun Function
    def BringInformation (self): pass
#        client = MongoClient(port=27017) # Establishing a Connection with Mongo
#        db=client.QRCodeCollection       #Accessing Database
#        QRCode = db.QRCode
	#   	client = pymongo.MongoClient("mongodb://ghina:QR-15-glucoset@cluster0-shard-00-00-usqui.mongodb.net:27017,cluster0-shard-00-01-usqui.mongodb.net:27017,cluster0-shard-00-02-usqui.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	#	db = client.test
    #    QRCodeData = db.QR.find_one({'QRNumber': self.ScanBoxM })
    #    for ArraivalDate in QRCodeData :
    #        self.ArrivalDateBox.insert(0.0,ArraivalDate)
    #    for BatchID in QRCodeData :
    #        self.BatchIDBox.insert(0.0,BatchID)
    #    for MoreInformation in QRCodeData :
    #        self.MoreInformationBox.insert(0.0,MoreInformation)
       

    ##Add New Information to Database Button Function 
    def AddNewToDatabase (self) : pass
#        client = MongoClient(port=27017) # Establishing a Connection with Mongo
#        db=client.QRCodeCollection       #Accessing Database
#        QRCode = db.QRCode
    #   	client = pymongo.MongoClient("mongodb://ghina:QR-15-glucoset@cluster0-shard-00-00-usqui.mongodb.net:27017,cluster0-shard-00-01-usqui.mongodb.net:27017,cluster0-shard-00-02-usqui.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	#	db = client.test
	#	self.AddNewToDatabaseM = [self.AddMoreInformationBoxM , self.MoreInformationM ]
    #    UpdateMoreInfo = db.QR.update_one ({'QRNumber' : self.ScanBoxM},{ '$set':{'QRNumber' : self.QRNumberM ,
    #                                                                                  'ArraivalDate' : self.ArraivalDateM ,
    #                                                                                  'BatchID' : self.BatchIDM ,
    #                                                                                  'MoreInformation' : self.AddNewToDatabaseM }})
    
    ##Delete The Information For This QR Code Button Function
    def DeleteTheInformationForThisQRCode (self) : pass
#        client = MongoClient(port=27017) # Establishing a Connection with Mongo
#        db=client.QRCodeCollection       #Accessing Database
#		QRCode = db.QRCode
    #    client = pymongo.MongoClient("mongodb://ghina:QR-15-glucoset@cluster0-shard-00-00-usqui.mongodb.net:27017,cluster0-shard-00-01-usqui.mongodb.net:27017,cluster0-shard-00-02-usqui.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	#	db = client.test
    #    DeleteDocument = db.QR.delete_mange('QRNumber' : self.ScanBoxM)


root = Tk()
root.title("QR Code")
root.geometry("1150x650")
app = Application (root)
root.mainloop()



