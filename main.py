c = {
    "A":"Alpha","B":"Bravo",
    "C":"Charlie","D":"Delta",
    "E":"Echo","F":"Foxtrot",
    "G":"Golf","H":"Hotel",
    "I":"India","J":"Juliet",
    "K":"Kilo","L":"Lima",
    "M":"Mike","N":"November",
    "O":"Oscar","P":"Papa",
    "Q":"Quebec","R":"Romeo",
    "S":"Sierra","T":"Tango",
    "U":"Unifrom","V":"Victor",
    "W":"Whiskey","X":"Xray",
    "Y":"Yankee","Z":"Zulu"
     }

g = input("give me a word")

for i in range(len(g)):
    if i < len(g)-1:
        word = c.get(g[i])
        print(word,"-",end="",sep="")
    else:
        word = c.get(g[i])
        print(word)
