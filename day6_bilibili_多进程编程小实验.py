import os
import multiprocessing


def copy(file,source_dir,dest_dir):

    source_path=source_dir+'\\'+file
    dest_path=dest_dir+'\\'+file

    with open(source_path,"rb") as sourefile:
        with open(dest_path,"wb") as destfile:
            while True:
                data=sourefile.read()
                if data:
                    destfile.write(data)
                else:
                    break




if __name__ == '__main__':
    source_dir=r"C:\Users\ruchan\PycharmProjects\baiduyunzhi\pythonlearn\day5_1102_正则表达式_Notes"
    dest_dir=r"C:\Users\ruchan\Desktop\multidemo"




    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已存在")

    file_list=os.listdir(source_dir)
    print(file_list)

    for file in file_list:
        sub_process=multiprocessing.Process(target=copy,args=(file,source_dir,dest_dir))
        sub_process.start()

