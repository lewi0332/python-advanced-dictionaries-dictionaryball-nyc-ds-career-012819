import pdb

game_dictionary = {
    'home':{
        'team_name': 'Brooklyn Nets',
        'colors': ['Black','White'],
        'players':[{
            'player_name': 'Allen Anderson',
            'number': 0,
            'shoe': 16,
            'points': 22,
            'rebounds': 12,
            'assists': 12,
            'steals':3,
            'blocks':1,
            'slam_dunks':1,
        },
            {
            'player_name': 'Reggie Evans',
            'number': 30,
            'shoe': 14,
            'points': 12,
            'rebounds': 12,
            'assists': 12,
            'steals': 12,
            'blocks': 12,
            'slam_dunks': 7,
        },
            {
            'player_name': 'Brook Lopez',
            'number': 11,
            'shoe': 17,
            'points': 17,
            'rebounds': 19,
            'assists': 10,
            'steals': 3,
            'blocks': 1,
            'slam_dunks': 15,
        },
            {
            'player_name': 'Mason Plumlee',
            'number':1,
            'shoe': 19,
            'points': 26,
            'rebounds': 12,
            'assists': 6,
            'steals': 3,
            'blocks': 8,
            'slam_dunks': 5,
        },
            {
            'player_name': 'Jason Terry',
            'number': 31,
            'shoe': 15,
            'points': 19,
            'rebounds': 2,
            'assists': 2,
            'steals': 4,
            'blocks': 11,
            'slam_dunks':1,
        }]
    },
    'away':{
        'team_name': 'Charlotte Hornets',
        'colors':  ['Turquoise','Purple'],
        'players':[{
            'player_name': 'Jeff Adrien',
            'number':4,
            'shoe':18,
            'points':10,
            'rebounds':1,
            'assists':1,
            'steals':2,
            'blocks':7,
            'slam_dunks':2   
    },
        {
            'player_name': 'Bismak Biyombo',
            'number':0,
            'shoe':16,
            'points':12,
            'rebounds':4,
            'assists':7,
            'steals':7,
            'blocks':15,
            'slam_dunks':10   
    },{
            'player_name': 'DeSagna Diop',
            'number':2,
            'shoe':14,
            'points':24,
            'rebounds':12,
            'assists':12,
            'steals':4,
            'blocks':5,
            'slam_dunks':5
    },{
            'player_name': 'Ben Gordon',
            'number':8,
            'shoe':15,
            'points':33,
            'rebounds':3,
            'assists':2,
            'steals':1,
            'blocks':1,
            'slam_dunks':0    
    },{
            'player_name': 'Brendan Haywood',
            'number':33,
            'shoe':15,
            'points':6,
            'rebounds':12,
            'assists':12,
            'steals':22,
            'blocks':5,
            'slam_dunks':12    
    }]
    }
}

def game_dict():
    return game_dictionary

def num_points_scored():
    for i in game_dict():
        for x in range(len(game_dict()[i]['players'])):
            if game_dict()[i]['players'][x]['player_name'] == name:
                print(game_dict()[i]['players'][x]['points'])

def shoe_size():
    for i in game_dict():
        for x in range(len(game_dict()[i]['players'])):
            if game_dict()[i]['players'][x]['player_name'] == name:
                print(game_dict()[i]['players'][x]['shoe'])

def team_colors():
    for i in game_dict():
        if game_dict()[i]['team_name'] == name:
            print(game_dict()[i]['colors'])

def team_names(dictionary):
    temp=[]
    for i in dictionary:
        print(i)
        temp.append(dictionary[i]['team_name'])
    return temp

def player_numbers():
    pass

def player_stats():
    pass

def good_practices():
  for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    import pdb; pdb.set_trace()
    for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
        for item in data:
            print(item)