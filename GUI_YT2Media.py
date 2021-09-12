import tkinter as tk
import youtube_dl

window = tk.Tk()
window.geometry("300x175")
window.resizable(False, False)
window.title("YT2Audio")

def select_all(event):
	event.widget.select_range(0, 'end')
	event.widget.icursor('end')

def download_audio(event=None):
    video_info = youtube_dl.YoutubeDL().extract_info(url = ent_URL.get(),download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

def download_video(event=None):
	options = {}
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([ent_URL.get()])

lbl_spacer = tk.Label(text="")
lbl_title = tk.Label(text="YT2Audio", font=("Helvetica 15 bold"))
lbl_URL = tk.Label(text="Paste the video URL:", font=("Helvetica 13 bold"))
ent_URL = tk.Entry()
btn_download_audio = tk.Button(text="Download Audio", command=download_audio, font=("Helvetica 10"))
btn_download_video = tk.Button(text="Download Video", command=download_video, font=("Helvetica 10"))
lbl_btn_spacer = tk.Label(text="     ")
lbl_spacer.pack()
lbl_title.pack()
lbl_URL.pack()
ent_URL.pack()
lbl_btn_spacer.pack(side=tk.LEFT)
btn_download_audio.pack(side=tk.LEFT)
btn_download_video.pack(side=tk.LEFT)

ent_URL.bind('<Control-KeyRelease-a>', select_all)
window.mainloop()