# Top No Backwards Compatible Xbox 360 Games

Picked up two of these free Xbox 360s from Gamestop:

https://slickdeals.net/f/12318616-xbox-360-s-4gb-console-premium-refurbished-70-visa-gift-card-70-free-shipping

Had to pay tax but eh. It turned out to be like $12 bucks?

Anyway, let's take a look at some 360-exclusive games. What won't run on a Xbox One? 

This little toolset requires Python 3.6 and Rust to be installed. But I'll leave an occasionally updated `csv` around here.

# THE DATA

You might be here for just that. Here's a table. 

Take a look at the output files for :

* [Users](out_user.txt)
* [Critics](out_critic.txt)

Look for stuff without an entry in the 4th column. It's way down. After all that, it'll be sorted by user score.

**There are inaccuracies and non-matches. Please use only as starting point. Eg. GTA IV or Grand Theft Auto IV is compatible, but the differing naming hurts.** 

-------

Anything below here is for regeneration.

# Prerequisites

1. Install `scrapy` from the Git Repository. (e.g. `pip install git+https://github.com/scrapy/scrapy`) This is required otherwise Windows CSVs will have double newlines. If not Windows, simply install from pip with `pip install scrapy`. (IMO, I think `scrapy`'s release process might be a bit weird!)
2. Install `xsv` from Cargo. `cargo install xsv`

## Xbox List

1. Run `scrapy runspider -t csv -o xbox.csv scrape_xbox.py`

Lots of corporatisms here. ® and ™ are to be stripped.

## Metacritic List

This is used to sort high priority games.

1. Run `scrapy runspider -t csv -o metacritic.csv scrape_metacritic.py`

The user scores have the `.` removed so it's just an `int` and more like `0-100`. 

## The sorted list of popular games on 360 but aren't backwards compatible.


```cmd
xsv join --no-case title metacritic.csv title xbox.csv --left | xsv sort -R -s 4,user_score | xsv table > out_user.txt
xsv join --no-case title metacritic.csv title xbox.csv --left | xsv sort -R -s 4,critic_score | xsv table > out_critic.txt
```

This is obviously not 100% accurate. MGS2 and MGS3 HD is supported on Xbox One but it's definitely all over the place in naming.