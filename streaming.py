from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import gmtime, strftime

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="ocs321EUeX4NeX0n9pQ8Jjnd5"
consumer_secret="6R2Dyy94yWBmrf5mWl5ehn0KlOyMuYhZsfVeWMPYH8F8P12Fyk"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2866987462-UKM99XIUpGwoZWVTwW4gkByGHxnF1yRlLqtK4bz"
access_token_secret="J6IvbtTK1i4g2Iqs1dXEVXNwcSvyqK65pQuLg6DmEgAsk"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        # print("==============================================")
        print(data)
        f.write(data)
        # print("==============================================")
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    output_file = strftime("%Y-%m-%d", gmtime())
    output_file += ".json"
    f = open(output_file,"w")
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#RussianHacking'])
