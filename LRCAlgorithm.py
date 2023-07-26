class LRCAlgoritm:
    value=''
    DataInBinaryFormat=[]
    NewDataInBinaryFormat=[]
    def ConvertOriginalData(self,OriginalData):
        for i in range(len(OriginalData)):
            AsciData=ord(OriginalData[i])
            binaryAsciCodeofString=bin(AsciData)
            self.DataInBinaryFormat.append(binaryAsciCodeofString)

    def Delete0bFromData(self):
        for i  in self.DataInBinaryFormat:
             self.NewDataInBinaryFormat.append(i[2:])
        print(self.NewDataInBinaryFormat)  

    def Calculate_LRC(self):
      self.value=''
      for i in range(len(self.NewDataInBinaryFormat)):
          count=0
          for j in range(len(self.NewDataInBinaryFormat)):
              if self.NewDataInBinaryFormat[j][i]=='1':
                  count=count+1
          #print(count)
          if count%2==0:
             self.value=self.value+'0'
          else:
             self.value=self.value+'1'
      
OriginalData=input("\n Enter Data ? \n")
ReceivedData=input("\n Enter Received Data ? \n")
#=== Original Data ===#
algorithm=LRCAlgoritm()
algorithm.ConvertOriginalData(OriginalData)
algorithm.Delete0bFromData()
algorithm.Calculate_LRC()
sendData=algorithm.NewDataInBinaryFormat
LRC_sendData=algorithm.value
print(LRC_sendData)
print(sendData)
#=== Recived Data Data ===#
algorithm.DataInBinaryFormat=[]
algorithm.NewDataInBinaryFormat=[]
algorithm.ConvertOriginalData(ReceivedData)
algorithm.Delete0bFromData()
algorithm.Calculate_LRC()
reciveData=algorithm.NewDataInBinaryFormat
LRC_receivedData=algorithm.value
print(LRC_receivedData)
print(reciveData)
if sendData==reciveData and LRC_sendData==LRC_receivedData:
    print("Accepted")
else:
    print("Rejected")
