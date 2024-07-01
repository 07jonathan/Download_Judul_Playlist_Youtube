from googleapiclient.discovery import build
import pandas as pd

# Masukkan API key Anda di sini
API_KEY = 'AIzaSyDAd03CvmZQeTR8ToXs_ZGNZ4-ArxE81bE'
PLAYLIST_ID = 'PLVe7xQpfOlypjR6GOS5ShaBBke5T8YziB'

# Membangun layanan YouTube
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Mengambil data video dari playlist
def get_video_titles(playlist_id):
    titles = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            titles.append(item['snippet']['title'])

        next_page_token = response.get('nextPageToken')
        if next_page_token is None:
            break

    return titles

# Mendapatkan judul video dari playlist
video_titles = get_video_titles(PLAYLIST_ID)

# Menyimpan judul video ke file Excel
df = pd.DataFrame(video_titles, columns=['Video Title'])
df.to_excel('youtube_playlist_titles.xlsx', index=False)

print('Judul-judul video telah disimpan ke youtube_playlist_titles.xlsx')
