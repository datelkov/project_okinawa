def read(file_path):

    result=[]
    restriced_symb=('/','\\','*')
    flagcount=False
    track_name_find=0

    with open(file_path,'rb') as file:
        f4bts=''
        byte = file.read(1)
        
        index = 0

        while index!=2048:
            #print(index,str(byte))
            byte=file.read(1)
            index+=1
            if index>0 and index<2048:
                flagcount=True
            else:
                flagcount=False
            if flagcount==True:
                if str(byte)[2] in restriced_symb: 
                    f4bts+='~'
                else:
                    f4bts+=str(byte)[2]

        m=f4bts.split('~')

        for i in m:
            if i !='' and (('TITLE' in i) or ('Title' in i) or ('title' in i)):
                result.append(i)
                track_name_find=1
        if track_name_find==1:        
            for j in result:
                title_name=j
            if 'TITLE=' in j:
                j=j.replace('TITLE=','')
            elif 'Title=' in j:
                j=j.replace('Title=','')
            elif 'title=' in j:
                j=j.replace('title=','')   
            return j
        else:
            return "Тэгов не найдено"

        


if __name__=="__main__":
    read('test4.flac')