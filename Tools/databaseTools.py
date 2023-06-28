import mysql.connector
from  Tools.ttktools import *


__Connection = None
__Cursor = None


def GetConnection():
    return __Connection

def GetCursor():
    return __Cursor

def isconnect():
    return (__Connection != None)

def Create_conns(DatebaseName = ""):
    try:
        global __Connection
        global __Cursor
        __Connection = mysql.connector.connect(user = "root",passwd = "" ,database =DatebaseName)
        __Cursor = __Connection.cursor(buffered=True)
    except BaseException as ex:
        msg(ex)

def create_db(DatebaseName = ""):
    try:
        if (not isconnect()):
            Create_conns()
        if isconnect():
            __Cursor.execute("CREATE DATABASE IF NOT EXISTS " + DatebaseName + " DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci")    
            __Connection.commit()
            Create_conns(DatebaseName)
    except BaseException as ex:
        msg(ex)

def delete_db(DatebaseName):
    try:    
        if not isconnect():
            Create_conns()
        if isconnect():
            __Cursor.execute("DROP DATABASE " + DatebaseName)
            __Connection.commit()
    except BaseException as ex:
        msg(ex)

def execute(SQL:str):
    try:
        if isconnect():
            __Cursor.execute(SQL)
            __Connection.commit()             
    except BaseException as ex:
        msg(ex)


def GetData(SQL:str):
    try:
        if  isconnect():  
            __Cursor.execute(SQL)
            __Connection.commit()
            return __Cursor.fetchall()
        else:                          
            return []
    except BaseException as ex:
        msg(ex)

def getautonumber(Table , column):
    try:
        if isconnect():  
            __Cursor.execute("SELECT MAX("+column+")+1 FROM " +Table)
            __Connection.commit()
            result = __Cursor.fetchone()[0]
            if result == None:
                return "1"
            else :
                return result
        else:            
            return -1
    except BaseException as ex:
        msg(ex)




            ##########  custom orders   ##############


def create_table(name , primary_key ,type, size):
    execute("""CREATE TABLE IF NOT EXISTS %s (%s %s(%d) PRIMARY KEY);"""
            %(name , primary_key ,type, size)) 

def addcolumn(table , name, type, size):
    execute("""ALTER TABLE %s ADD if not EXISTS %s %s(%d)"""
            %(table , name ,type, size)) 

def delcolumn(table , name):
    execute("""ALTER TABLE %s DROP COLUMN if EXISTS %s"""
            %(table , name)) 
def GetAllTableData(name):
        return GetData("Select * from " + name)     

def isexist(value ,Primary_key , table):    
    list = GetData("select * from %s where %s = '%s'"%(table,Primary_key,str(value)))
    return list != []
