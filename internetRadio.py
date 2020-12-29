import tkinter as tk
import vlc as vlc


url = 'http://s1-webradio.antenne.de/80er-kulthits'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

print("Bevore play")

main = tk.Tk(className="InternetRadio")
main.geometry("800x400")

def startPlayer():
    print("Start Player")
    player.play()

def stopPlayer():
    print("Stop Player")
    player.stop()

def changeUrl(newUrl):
    url = newUrl
    media=instance.media_new(url)
    player.set_media(media)
    print("Url Changed to", newUrl)
    player.play()


buttonBayern3 = tk.Button(main, text ="Bayern 3", width=50, height=3, command = lambda: changeUrl("http://br-edge-30a2-fra-ts-cdn.cast.addradio.de/br/br3/live/mp3/56/stream.mp3?_art=dj0yJmlwPTkxLjEzMi4xNDUuMTE0JmlkPWljc2N4bC02cnFkeHdrbGImdD0xNjA5MjcyMDI3JnM9Nzg2NmYyOWMjMzcxNTFmNTdhODFkOTAzNmRmMGQ0YjcxY2JkZTY2YjA"))
buttonAntenneBayernKH = tk.Button(main, text ="Antenne Bayern KH", width=50, height=3, command = lambda: changeUrl("http://s1-webradio.antenne.de/80er-kulthits"))
buttonRadioEins = tk.Button(main, text ="Radioeins", width=50, height=3, command = lambda: changeUrl("http://rbb-edge-106d-dus-dtag-cdn.cast.addradio.de/rbb/radioeins/live/mp3/mid?_art=dj0yJmlwPTkxLjEzMi4xNDUuMTE0JmlkPWljc2N4bC1qeDVrY3RybmImdD0xNjA5MjkxMTUxJnM9Nzg2NmYyOWMjMGNjZTNlMzJhYjY2MWZkM2UyNjRjMDc5NzNhMDYyZWM"))
buttonB5 = tk.Button(main, text ="B5 Aktuell", width=50, height=3, command = lambda: changeUrl("http://br-edge-3005-fra-ts-cdn.cast.addradio.de/br/b5aktuell/live/mp3/low?_art=dj0yJmlwPTkxLjEzMi4xNDUuMTE0JmlkPWljc2N4bC1jbnFmYW1ub2ImdD0xNjA5MjY4OTU1JnM9Nzg2NmYyOWMjNjBlYWNlZDBmMmEwZmE0ZDVhY2QwNmM3YTcxYTdiN2Y"))
buttonBayern2 = tk.Button(main, text ="Bayern 2", width=50, height=3, command = lambda: changeUrl("http://br-edge-30a2-fra-ts-cdn.cast.addradio.de/br/br2/nord/mp3/low?_art=dj0yJmlwPTkxLjEzMi4xNDUuMTE0JmlkPWljc2N4bC1tb3FmYW1ub2ImdD0xNjA5MjY2MjU2JnM9Nzg2NmYyOWMjZDZmNmU5NDRlZThhMmIyZDNmZTAwZTM4Nzg2NTZkMzA"))
buttonBayernKlassik = tk.Button(main, text ="BR Klassik", width=50, height=3, command = lambda: changeUrl("http://br-edge-2066-fra-lg-cdn.cast.addradio.de/br/brklassik/live/mp3/low?_art=dj0yJmlwPTkxLjEzMi4xNDUuMTE0JmlkPWljc2N4bC01b3FmYW1ub2ImdD0xNjA5MjQ1NDI4JnM9Nzg2NmYyOWMjZWE3NGQ3MDk2OTcwODM0N2RlNTVmOGFlZDQxZWE1ZDA"))
buttonBBC4 = tk.Button(main, text ="BBC 4", width=50, height=3, command = lambda: changeUrl("http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p"))
buttonKISS = tk.Button(main, text ="KISS 102.7", width=50, height=3, command = lambda: changeUrl("http://audio-mp3.ibiblio.org:8000/wncw-128k"))


buttonStart = tk.Button(main, text ="Start Player", bg='green', width=50, height=7, command = startPlayer)
buttonStop = tk.Button(main, text ="Stop Player", bg='red', width=50, height=7, command = stopPlayer)

buttonStart.grid(row=0,column=0)
buttonStop.grid(row=0,column=1)

buttonBayern3.grid(row=1,column=0)
buttonAntenneBayernKH.grid(row=1,column=1)

buttonRadioEins.grid(row=2,column=0)
buttonB5.grid(row=2,column=1)

buttonBayern2.grid(row=3, column=0)
buttonBayernKlassik.grid(row=3, column=1)

buttonBBC4.grid(row=4, column=0)
buttonKISS.grid(row=4, column=1)


tk.mainloop()


