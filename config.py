import os

server = '192.168.10.6'
RPI_ID = 1

global_topic = "pro1/rpi/"
pub_topic = "{}RPI{}".format(global_topic, RPI_ID)
sub_topic = "{}#".format(global_topic)


dataBase_name = 'Data.db'

ROOT = os.getcwd()
path = f'{ROOT}/Images/'