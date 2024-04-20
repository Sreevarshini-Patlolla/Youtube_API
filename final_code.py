import pandas as pd
import requests


def get_trending_videos():
        api_key = 'AIzaSyAY_NsoxMG4nfldw0LG303Y8Uyi6sGS2iE'
        base_url = 'https://www.googleapis.com/youtube/v3/videos'

        item_list = []

        params = {
                'chart' : 'mostPopular', 
                'part' : 'snippet, statistics',
                'maxResults' : 1,
                'key' : api_key
        }

        list = requests.request('GET', url = base_url, params=params)
        popular_json = list.json()
        item_list.append(popular_json['items'][0])
        next_page = popular_json['nextPageToken']

        i=1

        while i < ((int(popular_json['pageInfo']['totalResults']))):
        

                base_url = 'https://www.googleapis.com/youtube/v3/videos'
                if i < (int(popular_json['pageInfo']['totalResults']))-1:
                        params = {
                                'chart' : 'mostPopular', 
                                'part' : 'snippet, statistics',
                                'maxResults' : 1,
                                'key' : api_key,
                                'pageToken' : f"{next_page}"
                        }
                        list = requests.request('GET', url = base_url, params=params)
                        popular_json = list.json()
                        item_list.append(popular_json['items'][0])
                        # print(item_list)
                        next_page = popular_json['nextPageToken']
                else:
                        params = {
                                'chart' : 'mostPopular', 
                                'part' : 'snippet, statistics',
                                'maxResults' : 1,
                                'key' : api_key
                        }

                        list = requests.request('GET', url = base_url, params=params)
                        popular_json = list.json()
                        item_list.append(popular_json['items'][0])
                        # print(item_list)
                        # print(next_page)
                
                i+=1
        df = pd.DataFrame(item_list)
        df2 = pd.json_normalize(df['snippet'])
        df3 = pd.json_normalize(df['statistics'])
        data = df.join([df2,df3])
        new_data = data.drop(['kind','statistics','snippet','defaultAudioLanguage','defaultLanguage'],axis=1)
        return new_data


# if __init__ == '__main__':
get_trending_videos()
        