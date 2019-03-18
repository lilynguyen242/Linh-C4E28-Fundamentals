from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf-8")
soup = BeautifulSoup(html_content, "html.parser")
list_song = soup.find("section", "section chart-grid").find_all("li")
in_list = []
for song in list_song:
    h3 = song.h3
    a3 = h3.a
    h4 = song.h4
    a4 = h4.a
    song_name = a3.string
    artist = a4.string
    play_list = {
        "Song name": song_name,
        "Artist": artist
    }
    in_list.append(play_list)
# pyexcel.save_as(records=in_list, dest_file_name="music_list.xlsx")
    # PART 2
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([song_name + artist])
