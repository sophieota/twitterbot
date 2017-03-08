from twython import Twython
import csv

CONSUMER_KEY = '0MRq6YkWA8loR2Ti8cL2xGPJJ'
CONSUMER_SECRET = 'I45NGZEUw36R3ntFc9XE9YJoGll0Zrp7BZW56J2DriKLxGIYsh'
ACCESS_TOKEN = '839153164121174016-6GQd55ajKBwlpG3Y4mlAKAoIPRzOzxr'
ACCESS_TOKEN_SECRET = 'Lx13f9mEdJuneYqt2aKTBeb3myfJRpCbuEWiQOjzVxutJ'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='YOUR SEARCH TERM HERE', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['lucky charms', result['text'].encode('utf-8'), url]]
        a.writerows((text))
