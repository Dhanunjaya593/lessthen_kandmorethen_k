n,k = list(map(int,input().split())) 
letters  = list(input().split())
se_a = set(letters)
less_then =[]
more_then = [] 

new_list = []
for i in se_a:
    num = i,letters.count(i)
    new_list.append(num)

dict_a = dict(new_list)
for key,value in dict_a.items():
    num_key = key 
    value_v = value 
    if(value_v<=k):
        less_then.append(key) 
    if(value_v> k):
        more_then.append(key) 
print(sorted(less_then))
print(more_then)