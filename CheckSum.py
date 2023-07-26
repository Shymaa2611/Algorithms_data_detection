data='1010101011100010'
number_of_bits_segment=8
length_segment=int(len(data)/number_of_bits_segment)
list_of_data=[]
for i in range(len(data)):
    list_of_data.append(data[i])

print(list_of_data)
s=''
count=0
data_d=[]
for i in range(length_segment):
    data_segment=list_of_data[count:count+number_of_bits_segment]
    for j in range(len(data_segment)):
        s=s+data_segment[j]
    data_d.append(s)
    s=''
    count=count+number_of_bits_segment
print(data_d)
count=1
sum_data=[]
ss=''
remainder=0
sum_data.append(data_d[0])

#Sender
for i in range(len(data_d)-1):
    s=bin(int(sum_data[0],2)+int(data_d[count],2))
    print(s)
    s=s[2:]
    length_s=len(s)
    if length_s>8:
        remainder=s[0]
        s=s[1:]
    s=bin(int(s,2)+int(remainder))
    s=s[2:]
    print(s)
    sum_data=[]
    sum_data.append(s)
    count=count+1
    print(sum_data)
checksum=[]
#Reciever
s=''
for i in range(len(sum_data[0])):
    if sum_data[0][i]=='1':
        s=s+'0'
    else:
        s=s+'1'
    if i==len(sum_data[0])-1:
        checksum.append(s)
print(checksum)
print(sum_data)
s=bin(int(sum_data[0],2)+int(checksum[0],2))
s=s[2:]
ss=''
one_complement=[]
for i in range(len(s)):
    if s[i]=='1':
        ss=ss+'0'
    else:
        ss=ss+'1'
    if i==len(s)-1:
       one_complement.append(ss)
print(one_complement)   

if one_complement[0]=='00000000':
    print("There is no error in data")
else:
    print("There is error in data")


























    

# =============================================================================
# sumValue='' 
# for i in range(len(sum_list)):
#     sumValue=sumValue+sum_list[i]
# NewValue='' 
# for i in range(len(sumValue)):
#      if sumValue[i]!='b':
#          NewValue=NewValue+sumValue[i]
# print(NewValue)
# =============================================================================

# print(sum_list)
# checksum=[]
# for i in range(len(sum_list)):
#     if sum_list[i]==0:
#       checksum.append(1)
#     else:
#         checksum.append(0)
