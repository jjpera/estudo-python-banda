from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)

db = cliente['db-bandapy']