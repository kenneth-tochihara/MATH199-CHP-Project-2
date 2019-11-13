import requests

all_dates = ['03/28/2019','03/29/2019','03/30/2019','03/31/2019','04/01/2019','04/02/2019','04/03/2019','04/04/2019','04/05/2019','04/06/2019','04/07/2019','04/08/2019','04/09/2019','04/10/2019','04/11/2019','04/12/2019','04/13/2019','04/14/2019','04/15/2019','04/16/2019','04/17/2019','04/18/2019','04/19/2019','04/20/2019','04/21/2019','04/22/2019','04/23/2019','04/24/2019','04/25/2019','04/26/2019','04/27/2019','04/28/2019','04/29/2019','04/30/2019','05/01/2019','05/02/2019','05/03/2019','05/04/2019','05/05/2019','05/06/2019','05/07/2019','05/08/2019','05/09/2019','05/10/2019','05/11/2019','05/12/2019','05/13/2019','05/14/2019','05/15/2019','05/16/2019','05/17/2019','05/18/2019','05/19/2019','05/20/2019','05/21/2019','05/22/2019','05/23/2019','05/24/2019','05/25/2019','05/26/2019','05/27/2019','05/28/2019','05/29/2019','05/30/2019','05/31/2019','06/01/2019','06/02/2019','06/03/2019','06/04/2019','06/05/2019','06/06/2019','06/07/2019','06/08/2019','06/09/2019','06/10/2019','06/11/2019','06/12/2019','06/13/2019','06/14/2019','06/15/2019','06/16/2019','06/17/2019','06/18/2019','06/19/2019','06/20/2019','06/21/2019','06/22/2019','06/23/2019','06/24/2019','06/25/2019','06/26/2019','06/27/2019','06/28/2019','06/29/2019','06/30/2019','07/01/2019','07/02/2019','07/03/2019','07/04/2019','07/05/2019','07/06/2019','07/07/2019','07/08/2019','07/09/2019','07/10/2019','07/11/2019','07/12/2019','07/13/2019','07/14/2019','07/15/2019','07/16/2019','07/17/2019','07/18/2019','07/19/2019','07/20/2019','07/21/2019','07/22/2019','07/23/2019','07/24/2019','07/25/2019','07/26/2019','07/27/2019','07/28/2019','07/29/2019','07/30/2019','07/31/2019','08/01/2019','08/02/2019','08/03/2019','08/04/2019','08/05/2019','08/06/2019','08/07/2019','08/08/2019','08/09/2019','08/10/2019','08/11/2019','08/12/2019','08/13/2019','08/14/2019','08/15/2019','08/16/2019','08/17/2019','08/18/2019','08/19/2019','08/20/2019','08/21/2019','08/22/2019','08/23/2019','08/24/2019','08/25/2019','08/26/2019','08/27/2019','08/28/2019','08/29/2019','08/30/2019','08/31/2019','09/01/2019','09/02/2019','09/03/2019','09/04/2019','09/05/2019','09/06/2019','09/07/2019','09/08/2019','09/09/2019','09/10/2019','09/11/2019','09/12/2019','09/13/2019','09/14/2019','09/15/2019','09/16/2019','09/17/2019','09/18/2019','09/19/2019','09/20/2019','09/21/2019','09/22/2019','09/23/2019','09/24/2019','09/25/2019','09/26/2019','09/27/2019','09/28/2019','09/29/2019','09/30/2019','10/01/2019','10/02/2019','10/03/2019','10/04/2019','10/05/2019','10/06/2019','10/07/2019','10/08/2019','10/09/2019','10/10/2019','10/11/2019','10/12/2019','10/13/2019','10/14/2019','10/15/2019','10/16/2019','10/17/2019','10/18/2019','10/19/2019','10/20/2019','10/21/2019','10/22/2019','10/23/2019','10/24/2019','10/25/2019','10/26/2019','10/27/2019','10/28/2019','10/29/2019','10/30/2019']
file = open('pitchdata.txt','w')
file.write('Date,Home Team,Away Team,Pitcher,Pitch Type,Call,Balls (after),Strikes (after),Pitch Number,Batter,Is Starter\n')

for thedate in all_dates:
        
    mainurl = 'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date='+thedate

    respa = requests.get(url=mainurl)
    dataa = respa.json()

    try:
        number_of_games = len(dataa['dates'][0]['games'])
    except:
        number_of_games = 0
        print(f'error in number_of_games on {thedate}')

    k = 0
    game_links = []

    while k < number_of_games:
        game_links.append(dataa['dates'][0]['games'][k]['link'])
        k += 1

    for link in game_links:
        url = 'http://statsapi.mlb.com'+link
        url = url.replace('v1','v1.1')
        resp = requests.get(url=url)
        data = resp.json() 
        number_of_pas = len(data['liveData']['plays']['allPlays'])
        home_team = data['gameData']['teams']['home']['name']
        away_team = data['gameData']['teams']['away']['name']
        date = data['gameData']['datetime']['originalDate']
        print(f'{home_team},{away_team},{date}')
        try:
            probable_pitcher_id_away = data['gameData']['probablePitchers']['away']['id']
            probable_pitcher_id_home = data['gameData']['probablePitchers']['home']['id']
            probable_pitcher_home_name = data['gameData']['players']['ID'+str(probable_pitcher_id_home)]['fullName']
            probable_pitcher_away_name = data['gameData']['players']['ID'+str(probable_pitcher_id_away)]['fullName']
            starters = []
            starters.append(probable_pitcher_home_name)
            starters.append(probable_pitcher_away_name)
        except:
            starters = []
            print(f'Error in starters on {date} in {away_team} at {home_team}')
        j = 0
        while j < number_of_pas:
            i = 0
            try:
                pitches_in_pa = max(data['liveData']['plays']['allPlays'][j]['pitchIndex'])
            except:
                pitches_in_pa = -1
                print(f'Error in pitches_in_pa on {date} in {away_team} at {home_team}')
            while i <= pitches_in_pa:
                is_pitch = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['isPitch']
                ibb_tester = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['details']['description']
                if is_pitch == True and ibb_tester != 'Automatic Ball':
                    pitcher_name = data['liveData']['plays']['allPlays'][j]['matchup']['pitcher']['fullName']
                    try:
                        pitch_type = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['details']['type']['code']
                    except:
                        pitch_type = 'Unknown'
                        print(f'Error in pitch_type on {date} in {away_team} at {home_team}')
                    call = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['details']['code']
                    balls = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['count']['balls']
                    strikes = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['count']['strikes']
                    pitch_number = data['liveData']['plays']['allPlays'][j]['playEvents'][i]['pitchNumber']
                    batter_name = data['liveData']['plays']['allPlays'][j]['matchup']['batter']['fullName']
                    if pitcher_name in starters:
                        is_starter = True
                    else:
                        is_starter = False
                    file.write(f'{date},{home_team},{away_team},{pitcher_name},{pitch_type},{call},{balls},{strikes},{pitch_number},{batter_name},{is_starter}\n')
                i += 1
            j += 1
file.close()
