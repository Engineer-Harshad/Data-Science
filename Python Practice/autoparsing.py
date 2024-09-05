import os
os.chdir(r"C:\Users\dell\Documents\Python Practice\videos")
print(os.getcwd())
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) # to split the extension mp4 from the file name and getting only file name 
    print(f_name)
    # f_title, f_course, f_num = f_name.split('-')
    # f_title = f_title.strip()
    # f_course = f_course.strip()
    # f_num = f_num.strip()[1:].zfill(2) # zero padding all strings with 2 digits 

    # new_name = ('{}-{}{}'.format(f_num, f_title, f_ext))
    # os.rename(f,new_name) # f: og file, new_name : renaming it decided format 
