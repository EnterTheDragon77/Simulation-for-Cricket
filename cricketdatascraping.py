# THIS FILE SCRAPES DATA FROM CRICINFO, TURNS IT INTO READABLE DATA, AND EXPORTS IT TO PLAYERS.TXT

a = 700 #Number of players to read, starting with Cap 1 for the country (doesn't need to be exact, program will end with an error but still execute)
b = 25 # Cricinfo Team ID: 1 = England, 2 = Australia, 3 = South Africa, 4 = West Indies, 5 = New Zealand, 6 = India, 7 = Pakistan, 8 = Sri Lanka, 9 = Zimbabwe, 25 = Bangladesh
c = 'bangladeshplayers.txt' #file to write to

from bs4 import BeautifulSoup
import requests
import re

def scrape (x):

    global ReducedStats
    
    url = str('http://www.espncricinfo.com/ci/content/player/' + str(x) + '.html')
    r = requests.get(url)
    player = r.content

    soup = BeautifulSoup(player, 'html.parser')

 #   ReducedStats = []

    def comprehend (x):
        global ReducedStats
        Name = soup.find(text = x).parent.parent.span.contents
        Name[0] = Name[0].replace(',',' ')
        ReducedStats.append(Name[0])

    #comprehend ('Full name')
    try:
        comprehend ('Bowling style')
    except:
        ReducedStats.append(' ')

    #print (Style)

    #Name = Name[2]
    #Name = Name.span

    #print (Name)

    header = soup.find(text='HS')
    header = header.parent.parent.parent
    header = header.findAll('th')

    HeaderStats = []

    for i in range (1, len(header)):
        header[i] = header[i].contents
        HeaderStats.append(header[i][0])
        
    #print (HeaderStats)

    TestBatData = soup.find(text='Tests')
    TestBatData = TestBatData.parent.parent.parent.parent.parent
    TestBatData = TestBatData.findAll('td')

    TestBatStats = []

    for i in range(1,(len(TestBatData))):
        TestBatData[i] = TestBatData[i].contents
        TestBatData[i][0] = TestBatData[i][0].replace('\n\t\t\t\t\t','')
        try:
            TestBatData[i][0] = int(TestBatData[i][0][3::])
        except:
            try:
                TestBatData[i][0] = float(TestBatData[i][0][3::])
            except:
                1 == 1

        TestBatStats.append(TestBatData[i][0])

    #print (TestBatStats)


    for i in range(0, len(HeaderStats)):
        if HeaderStats[i] == 'Mat':
            ReducedStats.append(TestBatStats[i])
        if HeaderStats[i] == 'Inns':
            Inns = TestBatStats [i]
        if HeaderStats[i] == 'NO':
            NO = TestBatStats [i]
        if HeaderStats[i] == 'Runs':
            ReducedStats.append(TestBatStats[i])
        if HeaderStats[i] == 'BF':
            ReducedStats.append(TestBatStats[i])
    if 'BF' not in HeaderStats:
        ReducedStats.append(' ')

 #       if HeaderStats[i] == 'Ave':
 #           ReducedStats.append(TestBatStats[i])
    try:
        ReducedStats.append ((Inns-NO))
    except:
        ReducedStats.append(0)

    TestBowlStats = []

    TestBowlData = soup.findAll(text='Tests')
    TestBowlData = TestBowlData[1]
    TestBowlData = TestBowlData.parent.parent.parent.parent.parent
    TestBowlData = TestBowlData.findAll('td')

    for i in range(1,(len(TestBowlData))):
        TestBowlData[i] = TestBowlData[i].contents
        TestBowlData[i][0] = TestBowlData[i][0].replace('\n\t\t\t\t\t','')
        try:
            TestBowlData[i][0] = int(TestBowlData[i][0][3::])
        except:
            try:
                TestBowlData[i][0] = float(TestBowlData[i][0][3::])
            except:
                1 == 1
                
        TestBowlStats.append(TestBowlData[i][0])

    bowlheader = soup.find(text='BBM')
    bowlheader = bowlheader.parent.parent.parent
    bowlheader = bowlheader.findAll('th')

    BowlHeaderStats = []

    for i in range (1, len(bowlheader)):
        bowlheader[i] = bowlheader[i].contents
        BowlHeaderStats.append(bowlheader[i][0])
        
    #print (BowlHeaderStats)

    for i in range(0, len(BowlHeaderStats)):
        if BowlHeaderStats[i] == 'Balls':
            ReducedStats.append(TestBowlStats[i])
        if BowlHeaderStats[i] == 'Runs':
            ReducedStats.append(TestBowlStats[i])
        if BowlHeaderStats[i] == 'Wkts':
            ReducedStats.append(TestBowlStats[i])
 #       if BowlHeaderStats[i] == 'Ave':
 #           ReducedStats.append(TestBowlStats[i])

    try:
        FirstTest = soup.find(text='Test debut').parent.parent.parent.contents[3].contents[0][-5:-1]
        ReducedStats.append(int(FirstTest))
    except:
        FirstTest = soup.find(text='Only Test').parent.parent.parent.contents[3].contents[0][-5:-1]
        ReducedStats.append(int(FirstTest))

    try:
        LastTest = soup.find(text='Last Test').parent.parent.parent.contents[3].contents[0][-5:-1]
        ReducedStats.append(int(LastTest))
    except:
        LastTest = FirstTest
        ReducedStats.append(int(LastTest))

    FCBatData = soup.find(text='First-class')
    FCBatData = FCBatData.parent.parent.parent
    FCBatData = FCBatData.findAll('td')
    FCBatStats = []

    for i in range(1,(len(FCBatData))):
        FCBatData[i] = FCBatData[i].contents
        FCBatData[i][0] = FCBatData[i][0].replace("\n\t\t\t\t\t\t",'')
        FCBatData[i][0] = FCBatData[i][0].replace("\n\t\t\t\t\t",'')
        FCBatData[i][0] = FCBatData[i][0].replace("\t",'')
        FCBatData[i][0] = FCBatData[i][0].replace('\n','')
        FCBatData[i][0] = FCBatData[i][0][2::]
        try:
            FCBatData[i][0] = int(FCBatData[i][0])
        except:
            try:
                FCBatData[i][0] = float(FCBatData[i][0])
            except:
                1 == 1
        FCBatStats.append(FCBatData[i][0])

    for i in range(0, len(HeaderStats)):
        if HeaderStats[i] == 'Mat':
            ReducedStats.append(FCBatStats[i])
        if HeaderStats[i] == 'Inns':
 #           ReducedStats.append(FCBatStats[i])
            FCInns = FCBatStats[i]
        if HeaderStats[i] == 'NO':
 #           ReducedStats.append(FCBatStats[i])
            FCNO = FCBatStats[i]
        if HeaderStats[i] == 'Runs':
            ReducedStats.append(FCBatStats[i])
        if HeaderStats[i] == 'Ave':
            ReducedStats.append(FCBatStats[i])

 #   ReducedStats.append((FCInns-FCNO))

    #print (FCBatStats)

    # print ('[Name, BowlStyle, Games, Inns, NO, RunsSc, Balls, RunsAg, Wic, FirstTest, LastTest, FCGames, FCRuns, FCBatAve, FCInns, FCWickets, FCBowlAve]')




    FCBowlStats = []

    FCBowlData = soup.findAll(text='First-class')
    FCBowlData = FCBowlData[1]
    FCBowlData = FCBowlData.parent.parent.parent
    FCBowlData = FCBowlData.findAll('td')

    for i in range(1,(len(FCBowlData))):
        FCBowlData[i] = FCBowlData[i].contents
        FCBowlData[i][0] = FCBowlData[i][0].replace('\n\t\t\t\t\t','')
        FCBowlData[i][0] = FCBowlData[i][0].replace('\t','')
        FCBowlData[i][0] = FCBowlData[i][0].replace('\n','')
        try:
            FCBowlData[i][0] = int(FCBowlData[i][0][2::])
        except:
            try:
                FCBowlData[i][0] = float(FCBowlData[i][0][2::])
            except:
                1 == 1
                
        FCBowlStats.append(FCBowlData[i][0])

    #print (FCBowlStats)
    bowlheader = soup.find(text='BBM')
    bowlheader = bowlheader.parent.parent.parent
    bowlheader = bowlheader.findAll('th')

    BowlHeaderStats = []

    for i in range (1, len(bowlheader)):
        bowlheader[i] = bowlheader[i].contents
        BowlHeaderStats.append(bowlheader[i][0])
        
    #print (BowlHeaderStats)

    for i in range(0, len(BowlHeaderStats)):
        if BowlHeaderStats[i] == 'Wkts':
            ReducedStats.append(FCBowlStats[i])
        if BowlHeaderStats[i] == 'Ave':
            ReducedStats.append(FCBowlStats[i])

    #print ('Name, BowlStyle, Tests, Runs, BallsFaced WHERE POSSIBLE, TimesOut, Balls, Runs, Wickets, FirstYear, LastYear, FCGames, FCRuns, FCBatAve, FCWickets, FCBowlAve, GamesCaptained, Games WK')
    



def guruscrape (x):
    global ReducedStats
    url = str('http://stats.espncricinfo.com/ci/engine/player/' + str(x) + '.html?class=1;template=results;type=batting')
    r = requests.get(url)
    player = r.content
    soup = BeautifulSoup(player, 'html.parser')

    try:
        CaptainGames = ''
        while CaptainGames == '':
            CaptainGames = soup.find(text='is captain')
            if 'Span' in soup.prettify():
                CaptainGames = CaptainGames.parent.parent.parent.contents[5]
            else:
                CaptainGames = CaptainGames.parent.parent.parent.contents[4]
            CaptainGames = str(CaptainGames)
            CaptainGames = CaptainGames[4:-5]
            ReducedStats.append(int(CaptainGames))
    except:
        ReducedStats.append(0)

    try:
        WKGames = ''
        while WKGames == '':
            WKGames = soup.find(text='is designated keeper')
            if 'Span' in soup.prettify():
                WKGames = WKGames.parent.parent.parent.contents[5]
            else:
                WKGames = WKGames.parent.parent.parent.contents[3]
            WKGames = str(WKGames)
            WKGames = WKGames[4:-5]
            ReducedStats.append(int(WKGames))
    except:
        ReducedStats.append(0)
    try:
        Bat1Inns = ''
        while Bat1Inns == '':
            Bat1Inns = soup.find(text='1st position')
            if 'Span' in soup.prettify():
                Bat1Inns = Bat1Inns.parent.parent.parent.contents[7]
            else:
                Bat1Inns = Bat1Inns.parent.parent.parent.contents[5]
            #print (Bat1Inns.parent.parent.parent.contents)
            Bat1Inns = str(Bat1Inns)
            Bat1Inns = Bat1Inns[4:-5]
            Bat1Inns = int(Bat1Inns)
    except:
        Bat1Inns = 0
    try:
        Bat2Inns = ''
        while Bat2Inns == '':
            
            Bat2Inns = soup.find(text='2nd position')
            if 'Span' in soup.prettify():
                Bat2Inns = Bat2Inns.parent.parent.parent.contents[7]
            else:
                Bat2Inns = Bat2Inns.parent.parent.parent.contents[5]
            #print (Bat2Inns)
            Bat2Inns = str(Bat2Inns)
            Bat2Inns = Bat2Inns[4:-5]
            Bat2Inns = int(Bat2Inns)
    except:
        Bat2Inns = 0
    OpenInns = Bat1Inns + Bat2Inns
    print (CaptainGames, WKGames, OpenInns)
    ReducedStats.append(OpenInns)
        
        
def PlayerList (x, y):
    global ReducedStats, c
    url = str(str('http://www.espncricinfo.com/ci/content/player/caps.html?country=') +str(y)+ str(';class=1'))
    r = requests.get(url)
    player = r.content
    newsoup = BeautifulSoup(player, 'html.parser')
    Format = ('Name, BowlStyle, Tests, Runs, BallsFaced WHERE POSSIBLE, TimesOut, Balls, Runs, Wickets, FirstYear, LastYear, FCGames, FCRuns, FCBatAve, FCWickets, FCBowlAve, GamesCaptained, GamesWK, InnsOpen')
    f = open('players.txt','w')
    f.write(str(Format))
    f.write('\n')
    f.close()   
    f = open(c,'w')
    for i in range (1, (x+1)):
        ReducedStats = []
        HTMLString = newsoup.find(text=i)
        HTMLString = str(HTMLString.parent.parent.contents[3])
        PlayerNo = HTMLString[75::]
        PlayerNo = PlayerNo.split('.html')
        PlayerNo = PlayerNo[0]
        #print (PlayerNo)
        ShortName = HTMLString.split('middle;">')
        ShortName = ShortName[1][:-9]
        ReducedStats.append(ShortName)
        scrape (PlayerNo)
        guruscrape (PlayerNo)
        print (ReducedStats)
        f.write(str(ReducedStats))
        f.write('\n')
    f.close()
        

#print ('[Name, BowlStyle, Games, Inns, NO, RunsSc, Balls, RunsAg, Wic, FirstTest, LastTest, FCGames, FCRuns, FCBatAve, FCInns, FCWickets, FCBowlAve]')

results =  str(PlayerList (a, b))

print (str('Output sent to ' + str(c)))
