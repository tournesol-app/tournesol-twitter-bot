import requests
import pandas as pd
from datetime import datetime, timedelta

from data.utils_dict import YT_2_TWITTER, CRITERIA_DICT, already_shared_filepath


def remove_already_tweeted_videos_and_channels(df, language="en"):
    """Remove from the top df aready tweeted video and channel tweeted in the last n days"""

    # Get already tweeted video
    with open(already_shared_filepath[language], "r") as file:
        already_tweeted = [x.strip("\n").split(";") for x in file.readlines()]

    already_tweeted_video = [x[0] for x in already_tweeted]

    # Get already tweeted channels in the last n days
    n_days = 7
    already_tweeted_uploader = [x[1] for x in already_tweeted[-n_days:]]

    # Remove already tweeted video
    df = df[~df["video_id"].isin(already_tweeted_video)]

    # Remove channel already twetted in last n days
    df = df[~df["uploader"].isin(already_tweeted_uploader)]

    return df


def get_good_video(from_top, days_ago, language="en"):
    """Get a good video for the daily tweet"""

    date_delta = datetime.now() - timedelta(days=days_ago)
    date_gte = date_delta.strftime("%d-%m-%y-%H-%M-%S")
    response = requests.get(
        f"https://api.tournesol.app/video/?language={language}&date_gte={date_gte}&limit={from_top}"
    ).json()

    df = pd.DataFrame.from_dict(response["results"])

    def get_score(row, crit):
        for item in row["criteria_scores"]:
            if item["criteria"] == crit:
                return item["score"]

    for crit in CRITERIA_DICT.keys():
        df[crit] = df.apply(lambda x: get_score(x, crit), axis=1)

    df["tournesol_score"] = df[CRITERIA_DICT.keys()].sum(axis=1)

    # Keep videos rated by more than n contributors
    n_contributor = 2
    print(
        df[
            [
                "video_id",
                "name",
                "uploader",
                "tournesol_score",
                "rating_n_contributors",
                "reliability",
            ]
        ]
    )
    df = df[df["rating_n_contributors"] > n_contributor]

    df = remove_already_tweeted_videos_and_channels(df, language)

    # Remove video with a reliability lower than average
    df = df[df["reliability"] > 0.0]
    print("\nList of remaining videos :")
    print(df[["video_id", "name", "uploader", "tournesol_score", "reliability"]])  # ,'n_experts'

    # Chose a video randomly (weighted by Tournesol score) in the remaining list
    df_rand = df.sample(weights=df["tournesol_score"])

    video_dict = {}
    video_dict["video_id"] = df_rand["video_id"].item()
    video_dict["name"] = df_rand["name"].item()
    video_dict["uploader"] = df_rand["uploader"].item()
    video_dict["rating_n_contributors"] = df_rand["rating_n_contributors"].item()
    video_dict["rating_n_ratings"] = df_rand["rating_n_ratings"].item()

    # Find the 3 best rated criteria
    filt_criteria_list = list(CRITERIA_DICT.keys())
    filt_criteria_list.remove("largely_recommended")

    for i in range(1, 4):
        criteria = df_rand[filt_criteria_list].idxmax(axis=1).item()
        video_dict[f"top_crit_{i}"] = criteria
        filt_criteria_list.remove(criteria)

    return video_dict


def get_video_info(video_id=""):
    """Get the dictionnary of info (fron Tournesol API) for a video from it's ID"""

    # Get video info dictionary
    print("Call API with video_id: ", video_id)
    response = requests.get(f"https://tournesol.app/api/v2/videos/?video_id={video_id}").json()

    if response["count"]:
        video_dict = response["results"][0]
        print("The video has been found on Tournesol.")
        return video_dict
    else:
        print("The video has not been found on Tournesol!")
        return 0


def get_missing_channel_list(from_top, days_ago, language="en"):
    """To get a list of YouTube channel with not associated Twitter account in utils_dict.py"""

    print(" Get channels with no Twitter account associated.")

    # Get top viedeo from Tournesol API
    response = requests.get(
        f"https://tournesol.app/api/v2/videos/search_tournesol/?backfire_risk=100&better_habits=100&diversity_inclusion=100&engaging=100&entertaining_relaxing=100&importance=100&layman_friendly=100&pedagogy=100&reliability=100&days_ago_lte={days_ago}&language={language}&limit={from_top}"
    ).json()
    df = pd.DataFrame.from_dict(response["results"], orient="columns")

    # Remove channel which are already in the dictionnary
    df = df[~df["uploader"].isin(YT_2_TWITTER.keys())]

    df["n_experts"] = df["n_public_experts"] + df["n_private_experts"]
    df = df[df["n_experts"] > 1]

    # Print the list
    print("\nYouTub channel with no associated twitter account yet:")
    for uploader in df["uploader"].tolist():
        print(f'"{uploader}":"None",')
