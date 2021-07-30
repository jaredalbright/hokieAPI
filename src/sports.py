from sportsreference.ncaaf.schedule import Schedule as FBSchedule
from sportsreference.ncaab.schedule import Schedule as BBSchedule
from sportsreference.ncaaf.teams import Team as FBstats
from sportsreference.ncaab.teams import Team as BBstats

def getSch(sport):
    '''
    uses ncaaf.schedule or ncaab.schedule to get the schedule for the selected year
    '''
    jsonDic = {}
    played = []
    notPlayed = []

    if sport == 'fball':
        vtSched = FBSchedule('virginia-tech')
    else:
        vtSched = BBSchedule('virginia-tech')

    #iterates through each game in the schedules for the curr year
    for game in vtSched:
        gameDic = {}
        gameDic['Opponent'] = game.opponent_name
        gameDic['Date'] = game.date
        gameDic['Time'] = game.time

        #determines which list to add the game to 
        if game.points_against != None:
            gameDic['Result'] = game.result
            gameDic['Score'] = str(game.points_for) + '-' + str(game.points_against)
            played.append(gameDic)
        else:
            notPlayed.append(gameDic)

    jsonDic['Next Game'] = 'Season Complete'
    jsonDic['Completed Games'] = played
    jsonDic['Upcoming Games'] = notPlayed
   
   #optionally includes next game if there is one to be played
    if len(notPlayed) > 0:
        jsonDic['Next Game'] = notPlayed[0]

    return jsonDic

'''
The Teams module does not work according to the documentation
Hopefully this will be fixed later but for now these functions
will be left in the code but no endpoint will be included for 
them in the API
'''
def BasicStats(stats):
    '''
    Gathers stats that apply to both bb and fb
    '''
    jsonDic = {}
    jsonDic['Wins'] = stats.wins
    jsonDic['Losses'] = stats.losses

    return jsonDic

def getFBstats():
    '''
    Gathers football specific stats
    '''
    stats = FBstats('virginia-tech')
    FBstats()
    jsonDic = {}
    jsonDic['Basic Stats'] = BasicStats(stats)

    #stats that only apply to fb
    specialStats = {}
    specialStats['Points Per Game'] = stats.points_per_game
    specialStats['Points Against Per Game'] = stats.points_against_per_game
    specialStats['Yards Per Game'] = stats.yards
    specialStats['Yards Allowed Per Game'] = stats.opponents_yards
    specialStats['Pass Attempts Per Game'] = stats.pass_attempts
    specialStats['Rush Attempts Per Game'] = stats.rush_attempts
    specialStats['Turnovers Per Game'] = stats.turnovers

    jsonDic['Advanced Stats'] = specialStats

    return jsonDic


def getBBstats():
    '''
    Gathers basketball specific stats
    '''
    stats = BBstats('virginia-tech')
    jsonDic = {}
    jsonDic['Basic Stats'] = BasicStats(stats)

    #stats that only apply to fb
    specialStats = {}
    specialStats['Points'] = stats.points
    specialStats['Points Against'] = stats.opp_points
    specialStats['Assists'] = stats.assists
    specialStats['Turnovers'] = stats.turnovers
    specialStats['3pt Field Goals'] = stats.three_point_field_goals

    jsonDic['Advanced Stats'] = specialStats

    return jsonDic
