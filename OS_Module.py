import os
#os.mkdir("Learning")
# for i in range(0,100):
#     #os.mkdir(f"Learning/Day{i+1}")
#      os.rename(f"Learning/Day{i+1}",f"Learning/Tutorial {i+1}")
folders = os.listdir("Learning")
#print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"Learning/{folder}"))