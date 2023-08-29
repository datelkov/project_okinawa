import sys
import playsound_engine
import format_checker
import gui
import threading
import tags_reader
import playlist_gen

def starter():
    if len(sys.argv) > 1:
        tracklist = playlist_gen.save(sys.argv)
        file_path = tracklist[0]
        if format_checker.check_format(file_path) == 'flac':
                    track_name=tags_reader.read(file_path)
                    gui_thread = threading.Thread(target=gui.create,args=('Сейчас играет',track_name,))
                    play_thread = threading.Thread(target=playsound_engine.play_audio,args=(file_path,))
                    gui_thread.start()
                    play_thread.start()
            
        else:
            gui_thread = threading.Thread(target=gui.create,args=('Это не .flac','',))
            gui_thread.start()
    else:
        file_path = 'test.flac'
        track_name=tags_reader.read(file_path)
        gui_thread = threading.Thread(target=gui.create,args=('В режиме без файлов',track_name,))
        play_thread = threading.Thread(target=playsound_engine.play_audio,args=(file_path,))
        gui_thread.start()
        play_thread.start()

if __name__=="__main__":
    starter()