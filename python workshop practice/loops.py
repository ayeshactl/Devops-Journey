#list => DS which can hold multiple values of multiple type
#array => DS which can hold multiple values of same type


list_of_cloud = ["aws", "gcp", "azure", "digital ocean", "utho", "alibaba", "oracle"]

print(list_of_cloud)   # ['aws', 'gcp', 'azure', 'digital ocean', 'utho', 'alibaba', 'oracle']

# ADD NEW CLOUD SALESFORCE
list_of_cloud.append("Salesforce")
print(list_of_cloud)

# ADD NEW CLOUD IBM
list_of_cloud.append("IBM")
print(list_of_cloud)

# INSERT NAME AT INDEX 1
list_of_cloud.insert(1, "Ayesha")
print(list_of_cloud)


#FIND LENGTH OF LIST
print(len(list_of_cloud))


#ITERATION OF LIST
for cloud in list_of_cloud:
   print (" ")
   print(cloud)


   #PRINT NUMBERS FROM 1 TO 10
for i in range(1,11):  # end mai -1 hota hai thats why we write 11 here to print 10.
    print(i)

for i in range(1, 11):
    print("Hello, Ayesha")
