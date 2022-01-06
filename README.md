# Twitter Data Mining with Tweepy
 Using Python and tweepy, this project trawls recent tweets (with specific search queries) using Twitter's API V2. Authentication with Bearer Token required. Employed `Tweepy.client` as primary dictionary to search recent tweets and qualify query terms as well as `tweet_fields`.

# Data Visualisation with pandas
 With the pandas framework, the data collected is transferred into a consolidated format - a table - compressed under CSV. Running tweepy.paginator to append dataframe into table form under pandas.  

# Snapshots
## Tweets in txt (unformatted) 
Amassed recent tweets containing the keyword `sustainable`
![This is an image](https://github.com/jolsterr/Working-with-Twitter-Data/blob/main/Snapshots/tweets%20(raw).png)
## Tweets in CSV (formatted as table) 
Organized recent tweets containing the keyword `sustainable` in **a table** with columns 'Time Created', 'User' and 'Tweet Content' 
![This is an image](https://github.com/jolsterr/Working-with-Twitter-Data/blob/main/Snapshots/tweets%20in%20table%20form.png)
