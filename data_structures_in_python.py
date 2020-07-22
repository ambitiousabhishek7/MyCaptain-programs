list1=[]
list2=[]
for i in (3,2,'dk',9,'msi','rnld',2):  #assigning elements to lists
    if(isinstance(i,int)):
        list1.append(i)
    else:
        list2.append(i)
print('list1='+str(list1),'\n','list2='+str(list2))
def get_tuple(x,tuple): #accessing tuple elements
    return tuple[x]

tuple_=('mandeep','maanas','amal')
print(get_tuple(1,tuple_))

def del_dict(x,dict1):  #deleting dictionary elements
    del dict1[x]

dict_={
    'messi':6,
    'ronaldo':5,
    'modric':1,
    'dhannu':0
    }
del_dict('modric',dict_)
print(dict_)




