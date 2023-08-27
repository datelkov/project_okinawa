def check_format(file_path):
    with open(file_path,'rb') as file:
        f4bts=''
        byte = file.read(1)
        
        index = 0
        while index!=4:
            f4bts+=str(byte)[2]
            byte=file.read(1)
            index+=1
            f4bts=f4bts.lower()           
        return f4bts

if __name__=="__main__":
    check_format('test.flac')