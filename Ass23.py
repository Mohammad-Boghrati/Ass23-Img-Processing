
# imag=[]
# file_name=[]
# #file_name=os.listdir('E:\Python Class (ML)\MNIST_persian')
# for i in range(120):
#     file_name[i]=os.listdir(r'E:\Python Class (ML)\MNIST_persian\\'+str(i+1))
# os.path.join('',file_name)
# print("heloo world")













import os
import shutil
k=0
from random import randrange
for root, dirs, files in os.walk("MNIST_persian"):
    print(dirs)
    for file in files:
        
        for i in range(10):
            if file.endswith(".jpg") and os.path.basename(file)==str(i)+".jpg":
                if not os.path.exists(str(i)+"s"):
                     os.mkdir(str(i)+"s")
                k+=1
                shutil.copy(str(root)+"\\"+file,str(i)+"s"+"\\"+str(i)+str(k)+".jpg")






























        
    #  if file.endswith(".jpg") and os.path.basename(file)=="0.jpg":
    #     if not os.path.exists("0s"):
    #         os.mkdir("0s")
    #     os.replace(str(root)+"\\"+file,"0s")
    # #1
    #  if file.endswith(".jpg") and os.path.basename(file)=="1.jpg":
    #     if not os.path.exists("1s"):
    #         os.mkdir("1s")
    #     os.replace(file,'1s')
    # #2
    #  if file.endswith(".jpg") and os.path.basename(file)=="2.jpg":
    #     if not os.path.exists("2s"):
    #         os.mkdir("2s")
    #     os.replace(file,'2s')
    # #3
    #  if file.endswith(".jpg") and os.path.basename(file)=="3.jpg":
    #     if not os.path.exists("3s"):
    #         os.mkdir("3s")
    #     os.replace(file,'3s')
    # #4
    #  if file.endswith(".jpg") and os.path.basename(file)=="4.jpg":
    #     if not os.path.exists("4s"):
    #         os.mkdir("4s")
    #         os.replace(file,'4s')
    # #5
    #  if file.endswith(".jpg") and os.path.basename(file)=="5.jpg":
    #     if not os.path.exists("5s"):
    #         os.mkdir("5s")
    #     os.replace(file,'5s')
    # #6
    #  if file.endswith(".jpg") and os.path.basename(file)=="6.jpg":
    #     if not os.path.exists("6s"):
    #         os.mkdir("6s")
    #     os.replace(file,'6s')
    # #7
    #  if file.endswith(".jpg") and os.path.basename(file)=="7.jpg":  
    #     if not os.path.exists("7s"):
    #         os.mkdir("7s")
    #     os.replace(file,'7s')
    # #8
    #  if file.endswith(".jpg") and os.path.basename(file)=="8.jpg":
    #     if not os.path.exists("8s"):
    #         os.mkdir("8s")
    #     os.replace(file,'8s')
    # #9
    #  if file.endswith(".jpg") and os.path.basename(file)=="9.jpg":
    #     if not os.path.exists("9s"):
    #         os.mkdir("9s")
    #     os.replace(file,'9s')


