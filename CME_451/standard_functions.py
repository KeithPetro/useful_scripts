#Created by Keith Petro (c) 2016
#NSID: kdp343
#Student ID: 11139277
#Course: CME 451
#Name: standard_functions
#Purpose: holds important functions

#Dependencies (must be in same directory as this file):
#   N/A

#Convert from hexadecimal string to binary string
def convertHexToBin(hexString):
    hexVals = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    binString = ''
    for x in hexString:
        binString = binString + hexVals[x]
        
    return binString
##################################################

#Convert from binary to hexadecimal
def convertBinToHex(binString):
    binVals = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    hexString = ''
    for i in range(0, len(binString), 4):
        hexString = hexString + binVals[binString[i:i + 4]]
        
    return hexString
##################################################
    
#Function to create ENTIRE HTML output
def createFullHTMLOutput(datastreamDict, fileName):
    htmlFile = open(fileName, 'w')
    htmlData = ('<!DOCTYPE html>'
               '<html>'
               '<head>'
               '<style>'
               'table, th, td{'
               'border: 1px solid black;'
               'border-collapse: collapse;'
               'text-align: center;'
               '}'
               '</style>'
               '</head>'
               '<body>'
               '<table>'
               '<tr>'
               '<td colspan="32"><b> TCP Segment </b></td>'
               '</tr>'
               '<tr>'
               '<td colspan="16"> Source Port = ' + str(datastreamDict['Source Port']) + '</td>'
               '<td colspan="16"> Destination Port = ' + str(datastreamDict['Destination Port']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="32"> Sequence Number = ' + str(datastreamDict['Sequence Number']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="32"> Acknowledgement Number = ' + str(datastreamDict['Acknowledgement Number']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="4"> HLEN = ' + str(datastreamDict['HLEN']) + '</td>'
               '<td colspan="6"> Reserved = ' + str(datastreamDict['Reserved']) + '</td>'
               '<td colspan="1"> URG = ' + str(datastreamDict['URG']) + '</td>'
               '<td colpsan="1"> ACK = ' + str(datastreamDict['ACK']) + '</td>'
               '<td colspan="1"> PSH = ' + str(datastreamDict['PSH']) + '</td>'
               '<td colspan="1"> RST = ' + str(datastreamDict['RST']) + '</td>'
               '<td colspan="1"> SYN = ' + str(datastreamDict['SYN']) + '</td>'
               '<td colspan="1"> FIN = ' + str(datastreamDict['FIN']) + '</td>'
               '<td colspan="16"> Window Size = ' + str(datastreamDict['Window Size']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="16"> Checksum = ' + str(datastreamDict['Checksum']) + '</td>'
               '<td colspan="16"> Urgent Pointer = ' + str(datastreamDict['Urgent Pointer']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="32"> Option and Padding = ' + str(datastreamDict['Option and Padding']) +  '</td>'
               '</tr>'
               '</table>'
               '<table>'
               '<tr>'
               '<td> Data = ' + str(datastreamDict['Data']) + '</td>'
               '</tr>'
               '</table>'
               '</body>')
    htmlFile.write(htmlData)
    htmlFile.close()
##################################################
