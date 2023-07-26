import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("D:\\Matrial\\SimulationProjects\\sheet.xlsx",header=None)

#print(data)
############################3 Arrival Time #####################3
time_Clock=data.iloc[21:28,3:4]
#=============================================================================
print("======================== Arrival Time ==================")
#print(time_Clock)
time_Clock=np.array(time_Clock)
# #============================== End Time ===========================
time_End1=data.iloc[21:28,7:8]
time_End2=data.iloc[21:28,10:11]
time_End3=data.iloc[21:28,13:14]
time_End1=time_End1.values.tolist()
time_End2=time_End2.values.tolist()
time_End3=time_End3.values.tolist()
time_End=[]
for i in range(len(time_End1)):
      time_End.append(time_End1[i])
      time_End.append(time_End2[i])
      time_End.append(time_End3[i])
print(time_End)
      
time_End= [i for i in time_End if np.isnan(i) == False]
print(time_End)
print("======================== End Time ======================")
time_End=np.array(time_End)
# #================================= First Array ======================
ArrivalTime=[]
for i in range(len(time_Clock)):
    ArrivalTime.append(time_Clock[i])
    print(ArrivalTime[i])
#====================== Second Array ===============
EndTime=[]
for i in range(len(time_Clock)):
    EndTime.append(time_End[i])
    print(EndTime[i])
#================= Length Of First Array ===============
timeA=len(ArrivalTime)
print(timeA)
#================= Length Of Second Array ===============
timeE=len(EndTime)
print(timeE)
MergeArraySize=timeE+timeA
print(MergeArraySize)
MergeArray=[]
for i in range(timeA):
   MergeArray.append(ArrivalTime[i])
   for i in range(timeE):
    MergeArray.append(EndTime[i])
print("======================== Merge Array ===============")
unSortedArray=MergeArray
print(unSortedArray)
MergeArray.sort()
print("======================== Merge Sorted Array ===============")
print(MergeArray)
MergeArray=np.array(MergeArray)
Cust_Id=data.iloc[21:28,0:1]
Cust_Id=np.array(Cust_Id)
print("================== Custumer Id ============================== ")
print(Cust_Id)
ChronologicalOrdering=[]
count=0
for i in range(len(Cust_Id)):
     if(MergeArray[count]==ArrivalTime[i]):
                 ChronologicalOrdering.append(["Arrival",Cust_Id[i],MergeArray[count]]) 
     else:
         Cu=Cust_Id[i]-1
         ChronologicalOrdering.append(["Departure",Cu,MergeArray[count]]) 
     count=count+1
     if(MergeArray[count]==EndTime[i]):
                 ChronologicalOrdering.append(["Departure",Cust_Id[i] ,MergeArray[count]])  
                # Cust_Id[i]=round(count/2)
     else:
         Cu=Cust_Id[i]+1
         ChronologicalOrdering.append(["Arrival",Cu,MergeArray[count]])
         #Cust_Id[i]=round(count/2)
     count=count+1
     
    
ChronologicalOrdering=pd.DataFrame(ChronologicalOrdering,columns=["Event Type",
                                                           " Cust_Number"," Clock Time",])
 
 
print("================= Chronological Ordering Of Events ==================")     
print(ChronologicalOrdering)
#==================================================================
#time_Clock=list(time_Clock)
#Cust_Id=list(Cust_Id)
#df = pd.DataFrame({"Time_Clock":time_Clock,"Id":Cust_Id})
#df.plot(x="Time_Clock",y="Id")
#plt.xlabel("Clock Time")
#plt.ylabel("No.of Customers",kind="bar")








