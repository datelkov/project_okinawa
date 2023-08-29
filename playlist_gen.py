def save(tracklist):
    playlist=[]
    index=0
    for i in tracklist:
        if index!=0:
            playlist.append(i)
        index+=1
    print (playlist)
    return playlist

if __name__=="__main__":
    save()