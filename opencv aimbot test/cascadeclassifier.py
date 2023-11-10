import os

def generate_negative_description_file():
    with open('neg.txt','w') as f:
        for filename in os.listdir(r'C:\Users\Nicholas\Desktop\opencvtuto\negative'):
            f.write('negative/'+filename+'\n')
generate_negative_description_file()