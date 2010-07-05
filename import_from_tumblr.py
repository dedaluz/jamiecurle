from tumblr import Api
import simplejson

api = Api('jamiecurle.tumblr.com')
posts = api.read()

types = {}
for post in posts:
    if post['type'] not in types:
        types.update({post['type'] : post})
    """if post['type'] == 'link':
        print 'link - got'
    elif post['type'] == 'video':
        print 'video - got'
    elif post['type'] == 'regular':
        print 'regular - got'
    elif post['type'] == 'photo':
        print post
    elif post['type'] == 'quote':
        print 'quote - got'
    else:
        print 'new' + post['type']
    """
attrs = []
for t in types:
    for k in types[t].keys():
        if k not in attrs:
            attrs.append(k)
            

for a in attrs:
    print a

#simplejson.load(fp)
#fp.close()
