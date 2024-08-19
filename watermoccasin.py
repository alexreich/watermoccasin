import os
import sys
import requests
from bs4 import BeautifulSoup
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aac import AAC
from humanfriendly import format_timespan

# Default directory
default_dir = 'e:\\npr'

# Check if the user provided a directory argument
if len(sys.argv) > 1:
    download_dir = sys.argv[1]
else:
    download_dir = default_dir

# Ensure the directory exists
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# URLs to download
urls = [
    'https://www.npr.org/rss/podcast.php?id=500005',
    'https://feeds.npr.org/510318/podcast.xml',
    'https://www.omnycontent.com/d/playlist/acc8cc57-ff7c-44c5-9bd6-ab0900fbdc43/6fb6a6fb-9da9-4228-a1fe-ab91017920b8/2c429706-e067-4cd8-aa80-ab91017a4f72/podcast.rss'
]

time_length = 0
# Iterate through the URLs
for idx, url in enumerate(urls):
    if url.strip() == "":  # Skip commented out URLs
        continue

    response = requests.get(url)
    xml_data = response.content

    soup = BeautifulSoup(xml_data, 'xml')
    print (soup.find('channel').find('title').text)

    item = soup.find('item')

    if item:
        enclosure_tag = item.find('enclosure')
        title_tag = item.find('title')
        
        if enclosure_tag:
            mp3_url = enclosure_tag['url']

            # Use the title from the feed or a default if not available
            title = title_tag.text if title_tag else f'episode_{idx + 1}'

            # Sanitize `orig_fn_or_title` to remove or replace any characters not suitable for filenames
            sanitized_title = ''.join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()

            file_path = os.path.join(download_dir, f'podcast_{idx + 1}.mp3')

            response = requests.get(mp3_url)

            with open(file_path, 'wb') as f:
                f.write(response.content)

            ext = os.path.splitext(file_path)[1]

            if ext == '.mp3':
                audio = MP3(file_path)
            elif ext == '.mp4':
                audio = MP4(file_path)
            elif ext == '.aac':
                audio = AAC(file_path)
            else:
                print('{0} format not found!'.format(ext))

            print (f'podcast_{idx + 1} from {sanitized_title} for {format_timespan(audio.info.length)}')
            time_length += audio.info.length

print(f"Downloaded {len(urls)} files to {download_dir} for {format_timespan(time_length)}")