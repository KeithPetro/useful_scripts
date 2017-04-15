#Created by Keith Petro (c) 2016
#NSID: kdp343
#Student ID: 11139277
#Course: CME 451
#Name: datastream_to_dict
#Purpose: parses datastream and puts information into dictionary

#Dependencies (must be in same directory as this file):
#   standard_functions.py

#Imports
from standard_functions import *

#Definition of function
def datastreamToDict(datastream):
    #Basic dictionary structure
    datastreamDict = {'Source Port': 0, 'Destination Port': 0, \
                      'Sequence Number': 0, 'Acknowledgement Number': 0, \
                      'HLEN': 0, 'Reserved': 0, 'URG': 0, 'ACK': 0, 'PSH': 0, \
                      'RST': 0, 'SYN': 0, 'FIN': 0, 'Window Size': 0, \
                      'Checksum': 0, 'Urgent Pointer': 0, 'Option and Padding': '', \
                      'Data': ''}
    
    #Grab source port address
    src_port = int(datastream[0:4], 16)
    datastreamDict['Source Port'] = src_port

    #Grab destination port address
    dst_port = int(datastream[4:8], 16)
    datastreamDict['Destination Port'] = dst_port

    #Grab sequence number
    sequence_num = int(datastream[8:16], 16)
    datastreamDict['Sequence Number'] = sequence_num

    #Grab acknowledgement number
    acknowledgement_num = int(datastream[16:24], 16)
    datastreamDict['Acknowledgement Number'] = acknowledgement_num

    #Grab header length
    hlen = int(datastream[24:25], 16)
    datastreamDict['HLEN'] = hlen

    #Grab status reserved and status bits
    reserved_and_status = convertHexToBin(datastream[25:28])
    reserved = int(reserved_and_status[0:6], 2)
    datastreamDict['Reserved'] = reserved
    urg = reserved_and_status[6:7]
    datastreamDict['URG'] = urg
    ack = reserved_and_status[7:8]
    datastreamDict['ACK'] = ack
    psh = reserved_and_status[8:9]
    datastreamDict['PSH'] = psh
    rst = reserved_and_status[9:10]
    datastreamDict['RST'] = rst
    syn = reserved_and_status[10:11]
    datastreamDict['SYN'] = syn
    fin = reserved_and_status[11:12]
    datastreamDict['FIN'] = fin

    #Grab window size
    window_size = int(datastream[28:32], 16)
    datastreamDict['Window Size'] = window_size

    #Grab checksum
    checksum = int(datastream[32:36], 16)
    datastreamDict['Checksum'] = checksum

    #Grab urgent pointer
    urgent_pointer = int(datastream[36:40], 16)
    datastreamDict['Urgent Pointer'] = urgent_pointer

    #Grab option and padding
    option_and_padding = datastream[40:hlen*8]
    datastreamDict['Option and Padding'] = option_and_padding

    #Grab data
    data = datastream[hlen*8:]
    datastreamDict['Data'] = data

    return datastreamDict