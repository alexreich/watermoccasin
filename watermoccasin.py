import os
import sys
import requests
from bs4 import BeautifulSoup

# Default directory
default_dir = 'e:\\npr'

# Check if the user provided a directory argument
if len(sys.argv) > 1:
    download_dir = sys.argv[0]
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

# Iterate through the URLs
for idx, url in enumerate(urls):
    if url.strip() == "":  # Skip commented out URLs
        continue

    response = requests.get(url)
    xml_data = response.content

    soup = BeautifulSoup(xml_data, 'xml')
    item = soup.find('item')

    if item:
        enclosure_tag = item.find('enclosure')
        if enclosure_tag:
            mp3_url = enclosure_tag['url']

            response = requests.get(mp3_url)
            file_path = os.path.join(download_dir, f'podcast_{idx + 1}.mp3')

            with open(file_path, 'wb') as f:
                f.write(response.content)

print(f"Downloaded files to {download_dir}")
