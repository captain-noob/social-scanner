#  <center>SocialScanner</center>


[![build status](https://camo.githubusercontent.com/6552ebb68177acd290e11352dcd1541b864c37851a6fbb107e83e4a555fc9480/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275696c642d7061737365642d627269676874677265656e)](https://camo.githubusercontent.com/6552ebb68177acd290e11352dcd1541b864c37851a6fbb107e83e4a555fc9480/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275696c642d7061737365642d627269676874677265656e)  [![Analyze](https://camo.githubusercontent.com/65ca9eb70026b9d54d6299d60473deece39c400f4a21586adb7658424142eb43/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616e616c797a652d7061737365642d7269676874677265656e)](https://camo.githubusercontent.com/65ca9eb70026b9d54d6299d60473deece39c400f4a21586adb7658424142eb43/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616e616c797a652d7061737365642d7269676874677265656e)  [![version](https://camo.githubusercontent.com/40c1056d708aed7ee69b7a04ac356ba119f3c4aca19c0e3872df57c4a09e59d5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f74657374732d343737253230706173736564253243253230322532306661696c65642d726564)](https://camo.githubusercontent.com/40c1056d708aed7ee69b7a04ac356ba119f3c4aca19c0e3872df57c4a09e59d5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f74657374732d343737253230706173736564253243253230322532306661696c65642d726564)  [![Coverage](https://camo.githubusercontent.com/ef00da22678de03e27d778e2ac40ed109f4b3a49aa39e16d9dad2a813955b08f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f7665726167652d37352532352d677265656e)](https://camo.githubusercontent.com/ef00da22678de03e27d778e2ac40ed109f4b3a49aa39e16d9dad2a813955b08f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f7665726167652d37352532352d677265656e)  
[![Test](https://camo.githubusercontent.com/02858648a3df3b26cdab1a6a9e8e42bb39c0e60f3dc315a9f58f80ec1c0c2381/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646570656e64656e636965732d7570253230746f253230646174652d627269676874677265656e)](https://camo.githubusercontent.com/02858648a3df3b26cdab1a6a9e8e42bb39c0e60f3dc315a9f58f80ec1c0c2381/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646570656e64656e636965732d7570253230746f253230646174652d627269676874677265656e)  [![Python V3.7](https://camo.githubusercontent.com/e533214bcf1794f70b127b3802b45d7f49bed4a64c2d1a935cf052b17e129aa6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d76332e372d626c7565)](https://camo.githubusercontent.com/e533214bcf1794f70b127b3802b45d7f49bed4a64c2d1a935cf052b17e129aa6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d76332e372d626c7565)  [](https://camo.githubusercontent.com/029166d85f92969845201e59c3fcd8c8345556036155ff18140f6a9e796173a3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e)  [![status-up](https://camo.githubusercontent.com/0002c2606c231af00f6b4d6faffd1e50a8234213d900c337b4cadc0b9cb63da5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374617475732d75702d627269676874677265656e)](https://camo.githubusercontent.com/0002c2606c231af00f6b4d6faffd1e50a8234213d900c337b4cadc0b9cb63da5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374617475732d75702d627269676874677265656e)
 


**Social Scanner** This tool helps to identify the cyber predators, perverts/ sexualization on social media
The posts, comments and followers on social media are subjected to analysis and categorize using the offensive contents.

This system is currently capable of analyzing all social media platforms like Instagram, and other outlets seeking the same suspect. A set of user_id is used as a key to grab their personal information and their post information(Post ID, Comments, Timestamp, location, Captions) from multiple social platforms using ​ OSINT(Open Source INTelligence). 
  
This tool is designed to be cross-platformed. It could be compiled and run on both Windows and Linux.

  

## Installation
  

    - git clone https://github.com/captain-noob/social-scanner.git
    - cd social-scanner/
    
     add instagram sessionid cookie to`conf/instaconfig.json`
     add gmail id and password to conf/gmailconf.json


    - pip install -r requirements.txt
    - python main.py

For forwarding scan report enable Less secure apps in  [Gmail ](https://www.google.com/settings/security/lesssecureapps) 
    
##  Working

```php
python main.py
usage: main.py [-h] [-U USERFILE] [-u USERNAME] [-i] [-e EMAIL]

The tool intends to identify the cyber predators/child harassers on social
media with a malevolent intend. The posts, comments and followers on social
media are subjected to analysis and categorize using the offensive contents.

arguments:
  -h, --help            show this help message and exit
  -U USERFILE, --userfile USERFILE	User File for Analyzing.
  -u USERNAME, --username USERNAME	Username for Analyzing.
  -i, --instagram       Check in Instagram.
  -e EMAIL, --email EMAIL	Email the results.
```

### Important Notice⚠️

> This tool is for research purposes only. Hence, the developers of this tool won't be responsible for any misuse of data collected using this tool. Used by many researchers and open source intelligence (OSINT) analysts.


## Contacts  

    LinkedIn : https://www.linkedin.com/in/roshancp/
    Twitter : https://twitter.com/captain__noob

  

  

## Contributing


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
