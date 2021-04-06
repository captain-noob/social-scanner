import os, re ,smtplib


class email():
    def __init__(self,email,username,config):
        self.email = email
        self.username = username
        self.conf = config


    def checkEmail(self):
        regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, self.email)):
            return True
        else:
            return False
        
    
    def sendEmail(self):
        subject = f'Social Scanner - Scan Report for user `{self.username}`'
        to = self.email
        path = self.username
        
        if os.path.isdir(path):
            file = open(path+'/'+path+'.txt',encoding='utf-8')
            text = file.read()
            file.close()

            for _, _, files in  os.walk(path+'/'):
                for file in files:
                    chk = file.split('-')
                    if chk[0].lower() == 'offensive':
                        file = open(path+'/'+file,encoding='utf-8')
                        text += file.read()
                        file.close()

            #drafting email
            email_data  = 'Subject :'+subject+'\n'
            email_data += 'To :'+to +'\n'
            email_data += 'From :' + self.conf['email'] +'\n'
            email_data += text
            # print()

            # sent email
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(self.conf['email'], self.conf['password'])
                server.sendmail(self.conf['email'], to, email_data.encode('utf-8'))
                print('Email sent to '+to)
                server.close()
            except KeyError as e:
                print('Mail error')
                print(e)

            

        
        
        
        