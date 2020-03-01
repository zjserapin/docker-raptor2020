import pandas as pd


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-raptor/modern_RAPTOR_by_player.csv'
    df = pd.read_csv(url, error_bad_lines=False)
    df = df[df['season']==2019]


    all_stars = []
    all_stars.append(df[df['player_name']=='James Harden'])
    all_stars.append(df[df['player_name']=='Kemba Walker'])
    all_stars.append(df[df['player_name']=='Anthony Davis'])
    all_stars.append(df[df['player_name']=='LeBron James'])
    all_stars.append(df[df['player_name']=='Giannis Antetokounmpo'])
    all_stars.append(df[df['player_name']=='Kawhi Leonard'])
    all_stars.append(df[df['player_name']=='Trae Young'])
    all_stars.append(df[df['player_name']=='Joel Embiid'])
    all_stars.append(df[df['player_name']=='Pascal Siakam'])
    all_stars.append(df[df['player_name']=='Luka Doncic'])
    all_stars = pd.concat(all_stars)

    #all_stars = ['James Harden', 'Kemba', 'AD', 'LeBron', 'Giannis', 'Kawhi', 'Trae Young', 'Joel Embid', 'Pascal Siakam', 'Luka']

    #source https://projects.raspberrypi.org/en/projects/team-chooser/4



    team1=[]
    team2=[]

    while len(all_stars) > 0:
        playerA = all_stars.sample(n=1)
        team1.append(playerA)
        all_stars.drop(playerA.index, inplace=True)
        #print('Players left:', all_stars)
        
        playerB = all_stars.sample(n=1)
        team2.append(playerB)
        all_stars.drop(playerB.index, inplace=True)
        #print('Players left:', all_stars)

    team1 = pd.concat(team1)
    team2 = pd.concat(team2)
    print('Team 1:', team1['player_name'])
    print('Team 2:', team2['player_name'])


    if team1['war_total'].sum() > team2['war_total'].sum():
        print('Team 1 has a', round((team1['war_total'].sum())/(team1['war_total'].sum()+team2['war_total'].sum()),4), 'chance of winning')
    else:
        print('Team 2 has', round((team2['war_total'].sum())/(team1['war_total'].sum()+team2['war_total'].sum()),4), 'chance of winning')
