# Tournesol Twitter Bot

TournesolBot is based on the platform [Tournesol.app](https://tournesol.app).

The repository gathers scripts to execute the main functions of the TournesolBot in different languages

The main purpose of the TournesolBot is to:
- Tweet daily a video recommendation from the top ranked video on Tournesol
- Respond to tweet in which it is mentions and ask about the quality of a video

## Installation

Clone this directory somewhere on your computer.

Go into the directory and run the following command:

```
pip install -e .
```


## Usage

```sh
$ tournesolbot [-h] [-l 'en'/'fr'] [-a] [-d] [-m] [-r] [-t 'My tweet']

This is this help of the Tournesol-Twitter-Bot.

Requested arguments:

-l	select the language that will be use to tweet and for the other functions.

Optional arguments:

-h	show this help message and exit
-a	authentication to the Twitter account (access required!)
-d	make the daily recommandation tweet
-m	get the missing twitter account to fill the 'YT_2_TWITTER' dictionnary.
-r	respond to tweets in which Tournesol-Bot has been mentioned.
-t	tweet the corresponding string (e.g. 'My tweet').
```

#### Examples

---
**NOTE!**

If you don't own the TournesolBot twitter account, you can use the following command but without the argument "-a" (authentification) and "-r" (respond to mentions)

---

Write the daily tweet with the french twitter account:

```sh
tournesolbot -l fr -a -d
```

Respond to mention with the english twitter account:

```sh
tournesolbot -l en -a -r
```

Creating a list of missing YouTube channel  not associated yet with a twitter account:

```sh
tournesolbot -l en -m
```
