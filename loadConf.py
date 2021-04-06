import json

class LoadConfig():
    
        

    def instagram():
        conf = json.load(open('conf/instaconfig.json'))
        if len(conf['sessionid'])  < 3:
            return ''
        if len(conf['user-agent'])  < 3:
            return ''
        return conf

    def gmail():
        conf = json.load(open('conf/gmailconf.json'))
        if len(conf['email'])  < 3:
            return ''
        if len(conf['password'])  < 3:
            return ''
        return conf