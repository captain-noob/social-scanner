import requests
import json , os
import multiprocessing
import time
from .utils import list_contains

class Instagram():

    def __init__(self, username ,config):
        self.username =username
        self.config = config
        self.headers = {'User-agent':config['user-agent'] ,'Cookie': 'sessionid='+config['sessionid']}
        self.url = 'https://www.instagram.com/'+username+'/?__a=1'

    def validate(self):
        authCheckUrl = 'https://www.instagram.com/accounts/edit/?__a=1'
        try:
            resp = requests.get(authCheckUrl,headers=self.headers)
            resp.json()
            return True
        except:
            return False

    
    def checkOnComments(self,comments,wordlist):
        comments = comments.split()
        contains = list_contains(comments,wordlist)
        return contains
        

    #ectract Post
    def extractPost(self, shortcode,wordlist):
        
        try:
            text = f'\n\n_______________ POST INFO ___________________\n\n'
            domain = 'https://www.instagram.com/p/'+shortcode+'/?__a=1' #api
            displayUrl = 'https://www.instagram.com/p/'+shortcode+'/' #url
            filePath = self.username+'/'+'Offensive-post-'+shortcode+'.txt' #path
            chk_caption = False
            chk_comment = False 


            #request
            resp = requests.get(domain,headers=self.headers)
            ighql = resp.json()['graphql']['shortcode_media']


            #checking comments enabled or disabled 
            comments_disabled =ighql['comments_disabled']
            comments_disabled_viewers =ighql['commenting_disabled_for_viewer']

            #list of comments
            comments = ighql['edge_media_to_parent_comment']
            
            #caption
            caption=[]
            for node in ighql['edge_media_to_caption']['edges']:
                caption.append(str(node['node']['text']).replace('\n',' ').lower())
            caption = ''.join(caption)

            
            
            # output text
            text += '• ID                   : '+  str(ighql['id']) +'\n'
            text += '• Short Code           : '+  str(shortcode) +'\n'
            text += '• Post URL             : '+  str(displayUrl) +'\n'
            text += '• Video                : '+  str(ighql['is_video']) +'\n'
            text += '• Caption              : '+  caption  +'\n'
            text += '\n\n_______________ OFFENSIVE CONTENTS ___________________\n\n'


            #check offensive in caption
            if len(caption)>0:
                caption = caption.split()
                contains = list_contains(caption,wordlist)

                if contains: # if present
                    text += '• Offensive content in caption : '+  str(contains)  +'\n'
                    chk_caption = True


            text += "Comments : \n"
            if not comments_disabled_viewers and not comments_disabled :
                for comment in comments['edges']:
                    contains = self.checkOnComments(str(comment['node']['text']).lower(),wordlist)
                    if contains :
                        text += '• '+ str(comment['node']['owner']['username'])+' : '+  str(comment['node']['text']).replace('\n',' ')  +'\n'
                        chk_comment =True
            
            
            if chk_caption or chk_comment:
                print(text)
                file = open(filePath,'w+',encoding='utf-8')
                file.write(text)
                file.close()
            # else:
            #     print(f'[Info ] Unable to find offensive in this post , Try manually!')

              

        except ValueError as e:
            print('Error Post')
            print(e)






    #extract user
    def extract(self):
        try:
            # claculated time 

            

            #request
            resp = requests.get(self.url,headers=self.headers)
            resp = resp.json()['graphql']
            
            # User info
            if not os.path.isdir(self.username):
                os.mkdir(self.username)
            file = open(self.username+'/'+self.username+'.txt','w+',encoding='utf-8')

            text = '\n\n_______________PROFILE INFO___________________\n\n'
            text += '• ID           : '+  str(resp['user']['id'])                           +'\n'
            text += '• User Name    : ' + str(resp['user']['username'])                     +'\n'
            text += '• Full Name    : ' + str(resp['user']['full_name'])                    +'\n'
            text += '• FacebookId   : ' + str(resp['user']['fbid'])                         +'\n'
            text += '• Profile Pic  : ' + str(resp['user']['profile_pic_url_hd'])           +'\n'
            text += '• Verified     : ' + str(resp['user']['is_verified'])                  +'\n'
            text += '• Private      : ' + str(resp['user']['is_private'])                   +'\n'
            text += '• Website      : ' + str(resp['user']['external_url'])                 +'\n'
            text += '• Followers    : ' + str(resp['user']['edge_followed_by']['count'])    +'\n'
            text += '• Followings   : ' + str(resp['user']['edge_follow']['count'])         +'\n'
            text += '• Biography    : ' + str(resp['user']['biography']).replace('\n',' ')  +'\n'
            text += '• Posts        : ' + str(resp['user']['edge_owner_to_timeline_media']['count'])  +'\n'
            file.writelines(text )

            #log
            print('User Info : saved to '+self.username+'/'+self.username+'.txt')
            print(text) 
            file.close()

            #user info end

            #wordlist 
            wordfile = open('conf/wordlist.txt')
            wordlist = wordfile.read().split('\n')
            wordfile.close()
            #end


            
            #mapping user post
            posts = resp['user']['edge_owner_to_timeline_media']['edges']
            process =[]
            #end

            #multi processing.

            for node in posts:
                shortcode = str(node['node']['shortcode'])
                p = multiprocessing.Process(target=self.extractPost,args=[shortcode,wordlist])
                p.start()
                process.append(p)

            for proc  in process:
                proc.join()

            # ends

            

        except ValueError as e:
            print('[ Error ] No such user fount')
            # print(e)

        