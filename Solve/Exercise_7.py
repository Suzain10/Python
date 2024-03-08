import os
files = os.listdir("Solve")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Solve/{file}",f"Solve/{i}.png")

        #os.rename(f"Learning/Day{i+1}",f"Learning/Tutorial {i+1}")
        i = i+ 1
       