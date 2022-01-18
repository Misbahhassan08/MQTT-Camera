import os
import sys
import sqlite3
from config import dataBase_name 

class Database:
    
    def __init__(self):
        self.dataBase_name = dataBase_name
        pass # end of __init__ function
    
    def add_entery(self, params):
        try:

            conn = sqlite3.connect(self.dataBase_name)
            cursor = conn.cursor()

            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS Capture
                               (UID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               _image_name TEXT, 
                               _time TEXT,
                               _resolution TEXT,
                               _exp_time INTEGER,
                               _exp_mode TEXT,
                               _white_balance TEXT,
                               _iso INTEGER,
                               _brightness INTEGER,
                               _contrast INTEGER,
                               _saturation INTEGER,
                               _sharpness INTEGER,
                               _output TEXT
                                )""")
            _image_name = str(params['imageName'])
            _time = str(params['time'])
            _resolution = str(params['resolution'])
            _exp_time = params['expose_time']
            _exp_mode = params['exposure_mode']
            _white_balance = params['white_balance']
            _iso = params['iso']
            _brightness = params['brightness']
            _contrast = params['contrast']
            _saturation = params['saturation']
            _sharpness = params['sharpness']
            _output = params['raw']
            
            cursor.execute(""" INSERT INTO Capture
                               ( _image_name,
                               _time,
                               _resolution,
                               _exp_time,
                               _exp_mode,
                               _white_balance,
                               _iso,
                               _brightness ,
                               _contrast,
                               _saturation,
                               _sharpness,
                               _output)
                           VALUES 
                           (?,?,?,?,?,?,?,?,?,?,?,?)
                           """, (_image_name,_time, _resolution, _exp_time, _exp_mode, _white_balance, _iso, _brightness, _contrast, _saturation, _sharpness, _output ))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as error:
            print('Error in Data base: Inserting Values : ', error)
            return False
        pass # end of add_entery function
    
    pass # end of class Database