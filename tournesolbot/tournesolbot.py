import sys
import requests
import getopt

from tournesol_api_functions import get_good_video, get_video_info, get_missing_channel_list
from twitter_api_functions import twitter_authentication, write_tweet, write_response_tweet
from data.utils_dict import ACCEPTED_LANGUAGE, YT_2_TWITTER, CRITERIA_DICT
from data.utils_dict import (
    already_answered_filepath,
    daily_tweet_text,
    video_details_tweet_text,
    not_found_video_tweet_text,
)

# Parameters
FROM_TOP = 70
LAST_N_DAYS = 120


def daily_tweet(api, language="en"):
    # Prepare and tweet the daily video recommandation

    # Get the video id for today's tweet
    video_dict = get_good_video(FROM_TOP, LAST_N_DAYS, language)

    video_id = video_dict["video_id"]
    video_name = video_dict["name"]
    uploader = video_dict["uploader"]
    n_contributors = video_dict["rating_n_contributors"]
    n_ratings = video_dict["rating_n_ratings"]
    crit1 = video_dict["top_crit_1"]
    crit2 = video_dict["top_crit_2"]

    # Set language
    if language == "en":
        lang_idx = 0
    elif language == "fr":
        lang_idx = 1
    else:
        pass

    # Check if the uploader is paired with a Twitter account, if not just use the name
    if uploader in YT_2_TWITTER:
        twitter_accout = YT_2_TWITTER[uploader]
    else:
        twitter_accout = "'" + uploader + "'"

    # Check length and shorten the video title if the tweet is too long
    tweet_len_no_title = sum(len(i) for i in daily_tweet_text[language])
    tweet_len_no_title += sum(
        len(i)
        for i in [
            twitter_accout,
            str(n_ratings),
            str(n_contributors),
            CRITERIA_DICT[crit1][lang_idx],
            CRITERIA_DICT[crit2][lang_idx],
            video_id,
        ]
    )

    # 272 because :
    #     emoji count 2 caracters
    #     + 2 characteres for the youtube link
    #     + a small security in case of emoji in the title
    car_to_del = 272 - tweet_len_no_title - len(video_name)
    if car_to_del < 0:
        car_to_del -= 3
        video_name = video_name[:car_to_del] + "..."

    # Crete the tweet

    tweet = (
        daily_tweet_text[language][0]
        + video_name
        + daily_tweet_text[language][1]
        + twitter_accout
        + daily_tweet_text[language][2]
        + str(n_ratings)
        + daily_tweet_text[language][3]
        + str(n_contributors)
        + daily_tweet_text[language][4]
        + CRITERIA_DICT[crit1][lang_idx]
        + daily_tweet_text[language][5]
        + CRITERIA_DICT[crit2][lang_idx]
        + daily_tweet_text[language][6]
        + video_id
    )

    # Tweet it
    write_tweet(api, tweet, language, video_id, uploader)


def get_video_id_from_tweet(tweet_text):
    # Look for a youtube link in the tweet and return the video id

    tweet_text_list = tweet_text.split(" ")

    # Get the YouTube link from the tweet
    if "youtube.com" in tweet_text:
        # To find normal YouTube link
        link = [s for s in tweet_text_list if "youtube.com" in s]

    elif "youtu.be" in tweet_text:
        # To find shorten link in the form "youtu.be/lG4VkPoG3ko"
        link = [s for s in tweet_text_list if "youtu.be" in s]

    elif "http" in tweet_text:
        # To find shorten link in the form "https://t.co/xoP1b1DwOs"
        short_link = [s for s in tweet_text_list if "http" in s]

        try:
            link = requests.head(short_link[0]).headers["location"]
        except:
            print("The shorten link could not be used.")
            link = ""
    else:
        link = ""
        print("No link found in this tweet.")

    # Get the video id from the link
    if "youtube.com" in link:
        video_id = link.split("watch?v=")[1].split("&")[0]

    elif "youtu.be" in link:
        video_id = link.split("/")[-1]

    else:
        video_id = ""
        print("No YouTube video ID has been found in this tweet!")

    return video_id


def respond_to_mention(api, language="en"):
    # Prepare and tweet a response when TournesolBot is mention in a tweet (if necessary)

    print("Respond to mention in which TournesolBot was mentioned.")

    # Get already answered tweet id list
    with open(already_answered_filepath[language], "r") as file:
        already_answered = [int(x.strip("\n")) for x in file.readlines()]

    # Get mention in the timeline
    mentions = api.mentions_timeline(tweet_mode="extended")

    for mention in mentions:

        tweet_id = mention.id
        tweet_text = mention.full_text
        tweet_user = mention.user.screen_name

        print("\n-------------------------------------------------")
        print("Tweet id:", tweet_id)
        print("from:", tweet_user)
        print("text:", tweet_text)

        # Pass if this tweet has already been answered
        if tweet_id in already_answered:
            print("Already answered to this tweet!")
            continue

        video_id = get_video_id_from_tweet(tweet_text)

        if not video_id:
            print("Do not need to respond to this tweet.")

            # Add if to the list of already answered tweet
            with open(already_answered_filepath[language], "a") as file:
                file.write(f"{tweet_id}\n")
            print("The tweet id has been added in the list of already answered tweet.")
            continue

        video_dict = get_video_info(video_id)

        if video_dict:

            # Get video main info
            video_name = video_dict["name"]
            uploader = video_dict["uploader"]
            n_contributors = video_dict["rating_n_experts"]
            n_ratings = video_dict["rating_n_ratings"]

            print("Video found in the tweet:")
            print("Title:", video_name)
            print("Channel:", uploader)

            # Create the tweet
            tweet = (
                video_details_tweet_text[language][0]
                + tweet_user
                + video_details_tweet_text[language][1]
                + str(n_ratings)
                + video_details_tweet_text[language][2]
                + str(n_contributors)
                + video_details_tweet_text[language][3]
                + crit1
                + video_details_tweet_text[language][4]
                + crit2
                + video_details_tweet_text[language][5]
                + crit3
            )

        else:
            # Create the tweet for not found video
            tweet = (
                not_found_video_tweet_text[language][0]
                + tweet_user
                + not_found_video_tweet_text[language][1]
            )

        # Tweet the response
        write_response_tweet(api, tweet, language, tweet_id)


def print_help():
    print("Usage: python tournesolbot.py [-h] [-l 'en'/'fr'] [-a] [-d] [-m] [-r] [-t 'My tweet'] ")

    print("\nThis is this help of the Tournesol-Twitter-Bot.")

    print("\nRequested arguments:")
    print("\n-l\tselect the language that will be use to tweet and for the other functions.")

    print("\nOptional arguments:")
    print("\n-h\tshow this help message and exit")
    print("-a\tauthentication to the Twitter account (access required!)")
    print("-d\tmake the daily recommandation tweet")
    print("-m\tget the missing twitter account to fill the 'YT_2_TWITTER' dictionnary.")
    print("-r\trespond to tweets in which Tournesol-Bot has been mentioned.")
    print("-t\ttweet the corresponding string (e.g. 'My tweet').\n")


if __name__ == "__main__":

    # Empty api in the case no autentification is used
    api = ""

    # Get command line arguments
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            argv,
            "l:admrt:h",
            ["language", "authentication", "daily", "missing", "respond", "tweet", "help"],
        )
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    if len(sys.argv) <= 1:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        # Help
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()

        if opt == "-l":
            language = arg.strip()
            if language not in ACCEPTED_LANGUAGE:
                raise ValueError(
                    f"Language not recognize! only {list(ACCEPTED_LANGUAGE.keys())} are valid."
                )
            print("The selected language is: ", ACCEPTED_LANGUAGE[language])

        if opt == "-a":
            api = twitter_authentication(language)

        if opt == "-d":
            daily_tweet(api, language)

        if opt == "-t":
            write_tweet(api, arg, language)

        if opt == "-m":
            get_missing_channel_list(FROM_TOP, LAST_N_DAYS, language)

        if opt == "-r":
            respond_to_mention(api, language)
