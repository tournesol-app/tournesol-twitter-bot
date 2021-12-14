import tweepy
from data.utils_dict import already_shared_filepath, already_answered_filepath


def twitter_authentication(language="en"):
    """To authenticate to the Twitter API"""

    print("Start Twitter autentification")

    # Import from here to avoid error if used withou autentification file
    from data.authentication import twitter_account_en, twitter_account_fr

    # Get corresponding twitter account authentication dictionnary
    if language == "en":
        twitter_auth = twitter_account_en
        print(f"The english Twitter {twitter_auth['ACCOUNT_NAME']} account will be use.")
    elif language == "fr":
        twitter_auth = twitter_account_fr
        print(f"The french Twitter {twitter_auth['ACCOUNT_NAME']} account will be use.")
    else:
        raise ValueError("Language not recognize, no twitter account for this language!")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(twitter_auth["CONSUMER_KEY"], twitter_auth["CONSUMER_SECRET"])
    auth.set_access_token(twitter_auth["ACCESS_TOKEN"], twitter_auth["ACCESS_TOKEN_SECRET"])

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Twitter authentication OK")
        return api

    except:
        raise ValueError("Error during Twitter authentication")


def write_tweet(api, tweet, language, video_id="", uploader=""):
    """To write a tweet through the Twitter API"""

    print("\nThis is your tweet:\n")
    print(tweet)
    print("\n")

    if api:
        # TODO: remove when completly autonomus
        tweet_it = input("\nDo you realy want to tweet that?")

        if tweet_it == "yes":

            # Tweet with the Twitter API
            api.update_status(tweet)

            # Add to the list of tweeted videos
            if video_id:
                with open(already_shared_filepath[language], "a") as file:
                    file.write(f"{video_id};{uploader}\n")
                print("Added to the list of already shared videos.")

            print("Tweeted it!")

        else:
            print("OK, I will not tweet that!!!")


def write_response_tweet(api, tweet, language, tweet_id=""):
    """To respond to a tweet through the Twitter API"""

    print("\nThis is your tweet:\n")
    print(tweet)
    print("\n")

    if api:
        # TODO: remove when completly autonomus
        tweet_it = input("\nDo you realy want to tweet that?")

        if tweet_it == "yes":

            # Tweet with the Twitter API
            api.update_status(
                tweet, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True
            )

            # Add to the list of tweeted videos
            if tweet_id:
                with open(already_answered_filepath[language], "a") as file:
                    file.write(f"{tweet_id}\n")
                print("Added to the list of already shared videos.")

            print("Tweeted it!")

        else:
            print("OK, I will not tweet that!!!")
