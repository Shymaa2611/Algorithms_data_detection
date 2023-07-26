class VRCAlgoritm:
    DataInBinaryFormat=[]
    NewDataInBinaryFormat=[]
    number_of_one=[]
    def ConvertOriginalData(self,OriginalData):
        for i in range(len(OriginalData)):
            AsciData=ord(OriginalData[i])
            binaryAsciCodeofString=bin(AsciData)
            self.DataInBinaryFormat.append(binaryAsciCodeofString)

    def Delete0bFromData(self):
        for i  in self.DataInBinaryFormat:
             self.NewDataInBinaryFormat.append(i[2:])
        print(self.NewDataInBinaryFormat)  

    def CalCulateNumberOFOnes(self):
        for i in range(len(self.NewDataInBinaryFormat)):
            m=0
            for j in range(len(self.NewDataInBinaryFormat[i])):
                if self.NewDataInBinaryFormat[i][j]=='1':
                    m=m+1
            self.number_of_one.append(m)
        print(self.number_of_one)
    def DetermineAlgoritmType(self,Algorithm_type):
        for i in range(len(self.number_of_one)):
            if Algorithm_type=="ECP" or Algorithm_type=="ecp":
                if self.number_of_one[i]%2==0:
                    self.NewDataInBinaryFormat[i]='0'+self.NewDataInBinaryFormat[i]
                else:
                    self.NewDataInBinaryFormat[i]='1'+self.NewDataInBinaryFormat[i]
            else:
                if self.number_of_one[i]%2==0:
                    self.NewDataInBinaryFormat[i]='1'+self.NewDataInBinaryFormat[i]
                else:
                    self.NewDataInBinaryFormat[i]='0'+self.NewDataInBinaryFormat[i]
        print(self.NewDataInBinaryFormat)

OriginalData=input("\n Enter Data ? \n")
ReceivedData=input("\n Enter Received Data ? \n")
Algorithm_type=input("\n Enter Type Of Algorithm Of VRC ? \n") 
#=== Original Data ===#
algorithm=VRCAlgoritm()
algorithm.ConvertOriginalData(OriginalData)
algorithm.Delete0bFromData()
algorithm.CalCulateNumberOFOnes()
algorithm.DetermineAlgoritmType(Algorithm_type)
sendData=algorithm.NewDataInBinaryFormat
print(sendData)
#=== Recived Data Data ===#
algorithm.DataInBinaryFormat=[]
algorithm.NewDataInBinaryFormat=[]
algorithm.number_of_one=[]
algorithm.ConvertOriginalData(ReceivedData)
algorithm.Delete0bFromData()
algorithm.CalCulateNumberOFOnes()
algorithm.DetermineAlgoritmType(Algorithm_type)
reciveData=algorithm.NewDataInBinaryFormat
print(reciveData)
if sendData==reciveData:
    print("Accepted")
else:
    print("Rejected")