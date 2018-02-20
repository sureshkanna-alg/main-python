import os, glob, time

path = 'C:/Users/sures/Desktop/All'

date_file_list = []
for folder in glob.glob(path):    
    
    for file in glob.glob(folder + '/*.txt*'):      
        stats = os.stat(file)        
        lastmod_date = time.localtime(stats[8])        
        date_file_tuple = lastmod_date, file
        date_file_list.append(date_file_tuple)    

date_file_list.sort()
for file in date_file_list:   
    folder, file_name = os.path.split(file[1])   
    file_date = time.strftime("%m/%d/%y %H:%M:%S", file[0])


##print [file_name, file_date][0]
f = open(os.path.join(path,file_name))
data = f.read()
print (data)
f.close()









