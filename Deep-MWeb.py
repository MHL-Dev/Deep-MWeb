#python 3.7.1

import sys
import os
import random

os.system("clear")

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

print ('''                                       
                                            .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\               /|//}          ``--._  `.                
                |    |:::||              |////}                `-. \  
                |    |:::||             //'///                    `.
                |    |:::||            //  ||'                      `                
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||             ,     \    /      ,        
       /         /           |        `(   ||            / \    )\__/(     / \       
      /          .           /          )  ||           /   \  (_\  /_)   /   \      
     |            \          |     ________||      ____/_____\__\@  @/___/_____\____ 
    /             |          /     `-------.|     |             |\../|              |
   |\            /          |              ||     |              \VV/               |
   \/`-._       |           /              ||     |       Ｄｅｅｐ - Ｍ Ｗｅｂ      |
    //   `.    /`           |              ||     |_________________________________|
   //`.    `. |             \              ||      |    /\ /      \\       \ /\    | 
  ///\ `-._  )/             |              ||      |  /   V        ))       V   \  | 
 //// )   .(/               |              ||      |/     `       //        '     \| 
 ||||   ,'` )               /              //      `              V                '
 ||||  /                    /             || 
 `\` /`                    |             // 
     |`                     \            || 
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`

''')


print ('''

          }--------------{+} Coded by MHL {+}--------------{
          }-----{+}  GitHub.com/MHL-Dev/Deep-MWeb  {+}-----{

       ''')


print ('''

       {1} --- ProPublica > http://www.propub3r6espa33w.onion/
       {2} --- Facebook > http://www.facebookcorewwwi.onion/
       {3} --- DuckDuckGo > http://3g2upl4pq6kufc4m.onion/
       {4} --- Wasabi Wallet > http://wasabiukrxmkdgve5kynjztuovbg43uxcbcxn6y2okcrsg7gb6jdmbad.onion/
       {5} --- Riseup > http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion/
       {6} --- Archive.today > http://archivecaslytosk.onion/
       {7} --- The CIA > http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/
       {8} --- Keybase > http://fncuwbiisyh6ak3i.onion/
       {9} --- The Hidden Wiki > http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/
       {10} -- Mail2Tor > http://mail2tor2zyjdctd.onion/
       {11} -- SoylentNews > http://7rmath4ro2of2a42.onion/
       {12} -- TorLinks > http://torlinksd6pdnihy.onion/
       {13} -- SecureDrop > https://secrdrop5wyphb5x.onion/
       {14} -- Hidden Answers > http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/
       {15} -- The Dark Lair > http://vrimutd6so6a565x.onion/
       {16} -- Galaxy3 > http://galaxy3m2mn5iqtn.onion/
       {17} -- Sci-Hub > http://scihub22266oqcxt.onion/
       {18} -- Smartmixer.io > http://smrtmxdxognxhv64.onion/
       {19} -- Torch Search Engine > http://xmh57jrzrnw6insl.onion/
       {20} -- Candle > http://gjobqjj7wyczbqie.onion/
       {21} -- Not Evil > http://hss3uro2hsxfogfq.onion/
       {22} -- SearX > http://ulrn6sryqaifefld.onion/
       {23} -- Onion Wallet > http://ow24et3tetp6tvmk.onion/
       {24} -- GreenAddress > http://s7a4rvc6425y72d2.onion/
       {25} -- BBC Tor Mirror > http://bbcnewsv2vjtpsuy.onion/
       {26} -- Tor Metric > http://rougmnvswfsmd4dq.onion/
       {27} -- ProtonMail > https://protonirockerxow.onion/
       {28} -- SecMail > http://secmailw453j7piv.onion/
       {29} -- Comic Book Library > http://r6rfy5zlifbsiiym.onion/
       {30} -- Deep Web Radio > http://76qugh5bey5gum7l.onion/
       {100} - Coming Soon !
''')