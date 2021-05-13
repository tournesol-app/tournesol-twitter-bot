import requests
import pandas as pd

from data.utils_dict import YT_2_TWITTER, already_shared_filepath


def remove_already_tweeted_videos_and_channels(df, language='en'):
# Remove from the top df aready tweeted video and channel tweeted in the last n days

    # Get already tweeted video
    with open(already_shared_filepath[language], "r") as file:
        already_tweeted = [x.strip('\n') for x in file.readlines()]

    # Get already tweeted channels in the last n days
    n_days = 7
    last_days_channels = df.loc[df['video_id'].isin(already_tweeted),'uploader'].tolist()[-n_days:]

    # Remove already tweeted video
    df = df[~df['video_id'].isin(already_tweeted)]

    # Remove channel already twetted in last n days
    df = df[~df['uploader'].isin(last_days_channels)]

    return df


def get_good_video(from_top,days_ago,language='en'):
# Get a good video for the daily tweet

    # Get the top ranked video from Tournesol (through the API)
    response = requests.get(f"https://tournesol.app/api/v2/videos/search_tournesol/?backfire_risk=100&better_habits=100&diversity_inclusion=100&engaging=100&entertaining_relaxing=100&importance=100&layman_friendly=100&pedagogy=100&reliability=100&days_ago_lte={days_ago}&language={language}&limit={from_top}").json()
    df = pd.DataFrame.from_dict(response['results'], orient='columns')

    # Keep videos rated by more than n contributors
    n_contributor = 2
    df['n_experts'] = df['n_public_experts'] + df['n_private_experts']
    print(df[['video_id','name','uploader','tournesol_score','n_experts','reliability']])
    df = df[df['n_experts']>n_contributor]

    df = remove_already_tweeted_videos_and_channels(df, language)

    # Remove video with a reliability lower than average
    df = df[df['reliability']>1.1]
    print('\nList of remaining videos :')
    print(df[['video_id','name','uploader','tournesol_score','n_experts','reliability']])

    # Chose a video randomly (weighted by Tournesol score) in the remaining list
    df_rand = df.sample(weights=df['score'])
    video_id = df_rand['video_id'].item()

    return video_id


def get_video_info(video_id=''):
# Get the dictionnary of info (fron Tournesol API) for a video from it's ID

    # Get video info dictionary
    print('Call API with video_id: ',video_id)
    response = requests.get(f'https://tournesol.app/api/v2/videos/?video_id={video_id}').json()

    if response['count']:
        video_dict = response['results'][0]
        print('The video has been found on Tournesol.')
        return video_dict
    else:
        print('The video has not been found on Tournesol!')
        return 0


def get_missing_channel_list(from_top,days_ago,language='en'):
# To get a list of YouTube channel with not associated Twitter account in utils_dict.py

    print(' Get channels with no Twitter account associated.')

    # Get top viedeo from Tournesol API
    response = requests.get(f"https://tournesol.app/api/v2/videos/search_tournesol/?backfire_risk=100&better_habits=100&diversity_inclusion=100&engaging=100&entertaining_relaxing=100&importance=100&layman_friendly=100&pedagogy=100&reliability=100&days_ago_lte={days_ago}&language={language}&limit={from_top}").json()
    df = pd.DataFrame.from_dict(response['results'], orient='columns')

    # Remove channel which are already in the dictionnary
    df = df[~df['uploader'].isin(YT_2_TWITTER.keys())]

    # Print the list
    print('\nYouTub channel with no associated twitter account yet:')
    for channel in df['uploader'].tolist():
        print(f'"{channel}":"None",')
