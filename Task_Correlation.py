from itertools import groupby
from urllib.request import urlopen
from json import loads

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5' \
      '%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'

edits_count = {}
data = loads(urlopen(url).read().decode('utf8'))
revisions = data['query']['pages']['192203']['revisions']


def function(revision):
    return revision['timestamp'][:revision['timestamp'].index('T')]


for key, elem in groupby(revisions, function):
    edits_count[key] = len(list(elem))

print(max(edits_count, key=edits_count.get))