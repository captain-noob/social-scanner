import argparse
from loadConf import LoadConfig
from scripts.emailto import email
from scripts.instagram import Instagram
import time , sys ,os



def main():
    start = time.perf_counter() # timeer

    description = '''The tool intends to identify the cyber predators/child harassers on social media with a 
                    malevolent intend. The posts, comments and followers on social media are subjected to analysis and  categorize
                    using the offensive contents.''' #info

    #arg parcer
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-U','--userfile',help='User File for Analyzing.')
    parser.add_argument('-u','--username',help='Username for Analyzing.')
    parser.add_argument('-i','--instagram',help='Check in Instagram.' ,action='store_true')
    parser.add_argument('-e','--email',help='Email the results.' )

    args = parser.parse_args() #read args

    if args.username or args.userfile: # username or userfile

        if args.instagram : #checking social platorm
            conf = LoadConfig.instagram() #ig conf

            if conf : #checking vaid conf

                if args.username: # run with username

                    ig = Instagram(username=args.username,config=conf)

                    if ig.validate():
                        ig.extract()
                    else:
                        print('[Error] Instagram session id is invalid.')
                        sys.exit()

                elif args.userfile: # run  with userfile
                    if os.path.isfile(args.userfile):
                        file = open(args.userfile,'r',encoding='utf-8')
                        users = file.read()
                        file.close()
                        users = users.split('\n')
                        for user in users:
                            ig = Instagram(username=user,config=conf)
                            if ig.validate():
                                ig.extract()
                            else:
                                print('[Error] Instagram session id is invalid.')
                                sys.exit()

                    else:
                        print('[Error] No such file found.')
                        sys.exit()

            else: #throw error on no  config
                print('[Error] Instagram session config not found.')
                print('[Info ] Try adding sessionid in "conf/instaconfig.json"')
                sys.exit()


            if args.email: #sent email

                conf = LoadConfig.gmail() 
                if conf :
                    if args.username:
                        mail = email(email=args.email,username=args.username,config=conf)
                        if mail.checkEmail():
                            mail.sendEmail()
                        else:
                            print('[Error] Invalid email address.')
                            sys.exit()

                    elif args.userfile: # checking with userfile
                        if os.path.isfile(args.userfile):
                            file = open(args.userfile,'r',encoding='utf-8')
                            users = file.read()
                            file.close()
                            users = users.split('\n')
                            for user in users:
                                mail = email(email=args.email,username=user,config=conf)
                                if mail.checkEmail():
                                    mail.sendEmail()
                                else:
                                    print('[Error] Invalid email address.')
                                    sys.exit()
                        else:
                            print('[Error] No such file found.')
                            sys.exit()



                else:

                    print('[Error] Gmail Login creds not found.')
                    print('[Info ] Try adding creds in "conf/gmailconf.json"')
                    sys.exit()

        
        else: #throw error when no social media platform selected
            print('[Info] Select a target socialmedia platform.')
            sys.exit()


    
    else: # throw help when no username or userfile
        parser.print_help()
        sys.exit()






    # time calculation
    end = time.perf_counter()
    fin = str(round(end-start,2))
    print(f'Finished in '+ fin + ' second(s)') 
    #end

    

if __name__ == '__main__':
    main()
    