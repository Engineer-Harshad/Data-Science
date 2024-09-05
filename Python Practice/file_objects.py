# with open("note.txt","r") as f: # file opening with contact manager 
    
                ### READING FROM FILE ### 
    #read contents within file here in contact manager 
    # f_contents = f.read()
    # print(f_contents)
    # f_contents = f.readlines()
    # print(f_contents)
    # f_contents = f.readline()
    # print(f_contents, end = '')
    # f_contents = f.readline()
    # print(f_contents, end = '')

    # for line in f:
    #     print(line, end = '')
    # f_contents = f.read(10) # read first 10 chars 
    # print(f_contents)
    # f_contents = f.read(10)# read another 10 chars
    # print(f_contents)
    # pass 
# print(f.closed)
# print(f.read())

# f = open("note.txt","r") # file opening normally 
# print(f.name)
# f.close()

    # size_to_read = 10
    # f_contents = f.read(size_to_read) 

    # while len(f_contents)>0:
    #     print(f_contents,end='*')
    #     f_contents = f.read(size_to_read)

    # print(f.tell())
    
    # f_contents = f.read(size_to_read) 
    # print(f_contents,end ='')
    # f.seek(0)  # set position back to the beginning of the file 
    # f_contents = f.read(size_to_read) 
    # print(f_contents)

                ### WRITING TO FILE ### 
    
# with open("note2.txt","w") as f: # If this file exists then it will override it else if not exist, it will create new
#       f.write('Test') # When file is open in read mode, we can't write so file should be in write mode only to write 
#       # if don't wanna override file, use 'a' to append in it 
#       f.seek(0) # seek is confusing to use while writing file
#       f.write('R') 
          
                ### Read & Write together ###
# with open("note.txt","r") as rf:
#      with open("note_copy.txt","w") as wf: 
#           for line in rf:
#                wf.write(line) 

with open("vasu.jpeg","rb") as rf:    # Reading & writing img files in python needs to open file in binary mode 
     with open("vasu_copy.jpeg","wb") as wf: 
        #   for line in rf:
        #        wf.write(line) 
          chunk_size = 4096
          rf_chunk = rf.read(chunk_size)
          while len(rf_chunk)>0:
               wf.write(rf_chunk)
               rf_chunk = rf.read(chunk_size)
               