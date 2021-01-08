import tkinter as tk
import youtube_dl

def dw(url):
    youtube_info=youtube_dl.YoutubeDL().extract_info(url=url, download=False)
    file_name=f"{youtube_info['title']}.mp3"
    options={
        "format":"bestadio/best",
        "keepvideo":False,
        "outtmpl":file_name,
        "postprocessors":[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([youtube_info['webpage_url']])

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Yout DW")
    root.minsize(300,300)
    tk.Label(root,text="Ingresa el link aquí").pack()
    entrada=tk.Entry()
    entrada.pack()
    tk.Button(text="Descarga", command=lambda : dw(entrada.get())).pack()
    root.mainloop()