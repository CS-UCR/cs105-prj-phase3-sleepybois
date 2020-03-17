from bs4 import BeautifulSoup  # for scraping
import requests  # required for reading the file
import pandas as pd  # (optional) Pandas for dataframes
import json  # (optional) If you want to export json
import os
from collections import deque
import csv

urlPrefix = 'https://www.youtube.com'
q = deque()
count = 0
urlsqueue = ["https://www.youtube.com/watch?v=gF7TSlGv6no&fbclid=IwAR3u-MSia_FTkm1D9hZuQ4w1gxOApAHC08gRv7XFtsfNZ0Z-q-3KiVTmuhk",
             "https://www.youtube.com/watch?v=owURzgtwOSw", "https://www.youtube.com/watch?v=F3aXpa1rQEY", "https://www.youtube.com/watch?v=W26BIFLCWC0"]
while urlsqueue or count < 200:
    # url = input('Enter Youtube Video Url: ')  # user input for the link
    url = urlsqueue.pop(0)
    Vid = {}
    Link = url
    q.append(url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    # Collect all divs
    divs = soup.findAll('div')

    # Try to find video title
    try:
        Title = divs[1].find('span', class_='watch-title').text.strip()
    except:
        print('Title not found')
        Title = 'None'

    # Try to find channel name
    try:
        Channel_name = divs[1].find(
            'a', class_="yt-uix-sessionlink spf-link").text.strip()
    except:
        print('Channel name not found')
        Channel_name = 'None'

    # Try to find channel link
    try:
        Channel_link = (
            'www.youtube.com'+divs[1].find('a', class_="yt-uix-sessionlink spf-link").get('href'))
    except:
        print('Channel link not found')
        Channel_link = 'None'

    # Try to find subscribers
    try:
        Subscribers = divs[1].find(
            'span', class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").text.strip()
    except:
        print('Subscribers not found')
        Subscribers = 'None'

    Category_index = {
        1: 'Film & Animation',
        2: 'Autos & Vehicles',
        10: 'Music',
        15: 'Pets & Animals',
        17: 'Sports',
        19: 'Travel & Events',
        20: 'Gaming',
        22: 'People & Blogs',
        23: 'Comedy',
        24: 'Entertainment',
        25: 'News & Politics',
        26: 'Howto & Style',
        27: 'Education',
        28: 'Science & Technology',
        29: 'Nonprofits & Activism'
    }

    # Find category ID num
    Sp = divs[1].text.split(':')
    subs = 'categoryId'
    value = -1
    for j in range(len(Sp)):
        if subs in Sp[j]:
            value = int(Sp[j+1].split(',')[0])

    try:
        category_id = Category_index[value]
    except:
        print('Category not found')
        category_id = 'None'

    # Try to find video ID
    try:
        Video_ID = divs[1].find(class_='video-link')
        print('Video ID: ', Video_ID)
    except:
        Video_ID = 'None'

    # Try to find view counts
    try:
        View_count = divs[1].find(
            class_='watch-view-count').text.strip().split()[0]
    except:
        print('View counts not found')
        View_count = 'None'

    # Try to find likes
    try:
        Likes = divs[1].find('button', class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target yt-uix-tooltip").text.strip()
    except:
        print('Likes not found')
        Likes = 'None'

    # Try to find dislikes
    try:
        Dislikes = divs[1].find('button', class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target yt-uix-tooltip").text.strip()
    except:
        print('Dislikes not found')
        Dislikes = 'None'

    # Try to find related videos
    related_vids = divs[1].findAll(
        'a', class_='content-link spf-link yt-uix-sessionlink spf-link')

    Link_Related = []
    for i in range(len(related_vids)):
        Link_Related.append(urlPrefix + related_vids[i].get('href'))
        urlsqueue.append(urlPrefix + related_vids[i].get('href'))

    if len(Link_Related) == 0:
        print('No related videos found')
    else:
        print('# Related Videos: ', len(Link_Related))

    # Set Vid dict values
    Vid['Title'] = Title
    Vid['Link'] = url
    Vid['Channel'] = Channel_name
    Vid['Channel_link'] = Channel_link
    Vid['Channel_subscribers'] = Subscribers
    Vid['Category'] = category_id
    Vid['Video_ID'] = Video_ID
    Vid['Views'] = View_count
    Vid['Likes'] = Likes
    Vid['Dislikes'] = Dislikes

    # with open('vfile.json', 'w', encoding='utf8') as ou:
    # json.dump(Vid, ou, ensure_ascii=False)
    with open('data.csv', mode='a') as data_file:
        fieldnames = ['Title', 'Link', 'Channel Name', 'Channel Link',
                      'Subscriber Count', 'Category', 'Views', 'Likes', 'Dislikes']
        data_writer = csv.writer(
            data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # data_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        # data_writer.writeheader()
        # data_writer.writerow({'Title': Title, 'Link': Link, 'Channel Name': Channel_name, 'Channel Link': Channel_link,
        #                     'Subscriber Count': Subscribers, 'Category': Video_category, 'Views': View_count, 'Likes': Likes, 'Dislikes': Dislikes})
        data_writer.writerow([Title, Link, Channel_name, Channel_link,
                              Subscribers, category_id, View_count, Likes, Dislikes])

    count += 1

    #df = pd.DataFrame(Vid, index=[0])
    # print(df)
