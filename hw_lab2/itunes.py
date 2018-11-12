from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode('utf8')

soup= BeautifulSoup(page_content, 'html.parser')

div = soup.find("div", "section-content")
ul = soup.find("ul", div)


li_list = ul.find_all("li")
songs_list=[]

for li in li_list:
    h3 = li.h3
    h4 = li.h4
    a = li.a
    name = h3.string
    artist = h4.string
    link = url + a["href"]
    
    songs = {
        "name": name,
        "artist": artist,
        "link": link,
    }
    songs_list.append(songs)
    

pyexcel.save_as(records=songs_list, dest_file_name = "itunes song.xlsx")

option = {
    'default_search' : 'ytsearch',
    'max_download' : 1,
}
sing = input("Bạn muốn download bài hát nào ?")
dl = YoutubeDL(option)
dl.download(sing)