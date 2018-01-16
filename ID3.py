import math
import csv
def my_all_data_list(file_path):
        with open(file_path,'r') as f:
                reader = csv.reader(f)
                my_list = list(reader)
        return my_list
def target_attr(all_data):
        target_attr_list=[]
        for i in range(0,len(all_data)):
                target_attr_list.append(all_data[i][len(all_data[0])-1])
        return target_attr_list
  
def target_attr_entropy(all_data):
        target_attr_list=target_attr(all_data)
        #print(target_attr_list)
        s=entropy(target_attr_list)
        return s
def merged_classes(attr,target_attr):
        #merged_class=[]
        merged_class=zip(attr,target_attr)
        #print(entropy(list(merged_class)))
        return merged_class
def unique_attr_clases(attr_list):
        class_count={}
        class_attr_list=set(attr_list)#get number of unique classes in attribute
        all_classes=list(class_attr_list)#convert back to list
        for x in all_classes:
                class_count[x]=attr_list.count(x)
        return class_count
def entropy(attr_list):
	entropy=0
	class_attr_list=set(attr_list)#get number of unique classes in attribute
	all_classes=list(class_attr_list)#convert back to list
	#print(all_classes)
	for x in all_classes:
		probability=attr_list.count(x)/len(attr_list)
		entropy-=(probability*math.log2(probability))
		#print(len(attr_list))
	print("Target Attribute Entropy: ",entropy, "\n")
	return entropy
def inner_entropy(attr_list,target_attr):
        #print(attr_list)
        merged_class=list(merged_classes(attr_list,target_attr))
        entropy=0
        class_attr_list=set(merged_class)#get number of unique classes in attribute
        all_classes=list(class_attr_list)#convert back to list
        uniq_list=unique_attr_clases(attr_list)
        #print(all_classes)
        for x in all_classes:
                
                probability=merged_class.count(x)/attr_list.count(x[0])
                #print(attr_list.count(x[0]),len(attr_list),probability,math.log2(probability))
                entropy-=(attr_list.count(x[0])/len(attr_list))*(probability*math.log2(probability))
        print("Entropy: ",entropy, "\n")
        return entropy
def info_gain(t_entropy,all_list_data,all_data):
        a_entropy=[]
        t_attr=target_attr(all_data)
        #a_ig=t_entropy-a_entropy
        t_entropy=target_attr_entropy(all_data)
        for i in range(0,len(all_list_data)):
                print(all_list_data[i],t_attr)
                a_entropy.append(t_entropy-(inner_entropy(all_list_data[i],t_attr)))
        if len(a_entropy)>0:
                return max(a_entropy),"-->",a_entropy.index(max(a_entropy))
def root_node(all_data):
        #tree_structure=[]#list to store tree structure
        #print("Length: ",len(all_data))
        all_list_data=all_data_format(all_data)
        t_entropy=target_attr_entropy(all_data)
        #print("Target Entropy: ",t_entropy)
        #for k in range(0,len(all_list_data)):
        if t_entropy!=1:
                tree_structure=info_gain(t_entropy,all_list_data,all_data)
                delete_column=tree_structure[2]
                csv_rewrite(delete_column,all_data)#new reduced table
                print("New Root Node IG",tree_structure[1], tree_structure[0], "\n")
        #detach from data
        #run algorithm again until no more data is left
def csv_rewrite(delete_key,all_data):
        #create new csv file with delted column choosen as root node
        n=0
        all_list_data=all_data_format(all_data)
        #print(all_list_data)
        full_list=[]
        del all_list_data[delete_key]
        #print(dict(all_list_data))
        all_list_data=dict((i,all_list_data[k]) for i,k in enumerate(sorted(all_list_data.keys())))#write a new dictionary
        print(all_list_data)
        with open("C:\\Users\\emenya\\Desktop\\id3_data.csv",'w', newline='') as newcsv:
                filewriter=csv.writer(newcsv,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                
                for k in range(0,len(all_data)):
                        for j in range(0,len(all_list_data)):
                                #filewriter.writerow(all_list_data[j][k])
                                full_list.append(all_list_data[j][k])
                #print(full_list)
                for l in range(n,len(all_data)):
                        #current_list[t]=full_list[n:(n+len(all_list_data))]
                        filewriter.writerow(full_list[n:(n+len(all_list_data))])
                        #print(current_list)
                        n+=len(all_list_data)
                        #t+=1
                #for w in range(0,len(current_list)):
                        #filewriter.writerow(current_list[w])
                        
def all_data_format(all_data):
        full_attr_list=[]
        n=0
        dict_attr_list={}
        for i in range(0,len(all_data[0])-1):
                for j in range(0,len(all_data)):
                        full_attr_list.append(all_data[j][i])              
        for k in range(n,len(all_data[0])-1):
                #print(n)
                dict_attr_list[k]=full_attr_list[n:n+round(len(full_attr_list)/(len(all_data[0])-1))]
                n+=round(len(full_attr_list)/(len(all_data[0])-1))
        return dict_attr_list

#program starts here
all_data=my_all_data_list("C:\\Users\\emenya\\Desktop\\id3_data.csv")#change file path to trace data file
all_list_data=all_data_format(all_data)
#print(len(all_list_data))
while len(all_list_data)>0:
        all_data=my_all_data_list("C:\\Users\\emenya\\Desktop\\id3_data.csv")#re-reading data everytime table is reduced
        all_list_data=all_data_format(all_data)
        #print(len(all_list_data))
        if len(all_data)>0:
                root_node(all_data)

