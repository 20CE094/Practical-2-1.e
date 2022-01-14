#Name-Nehal Patel
#ID- 20CE094
#Github link: https://github.com/20CE094/Practical-2-1.e.git
#Aim: Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
print(dic4)
#concating dic4 and dic1
dic4.update(dic1)
#concating dic4 and dic2
dic4.update(dic2)
#concating dic4 and dic3
dic4.update(dic3)
#Printing updated dictionary
print (dic4)