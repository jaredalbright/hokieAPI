from fastapi import FastAPI
import sports
import town

app = FastAPI()

#default route
@app.get("/")
def home():
    return {"message": "Welcome to hokieAPI"}

#sports decision route
@app.get("/api/v1/sports/")
def sportsOptions(sport_name: str = "all"):
    '''
    Picks which sport should be returned with the
    default being both
    '''
    #object that will be returned if counter > 1
    jsonDic = {}

    #counter to determine what is returned
    counter = 0

    #not case sensitive
    sport_name.lower()

    if sport_name == 'fball' or sport_name == "all":
        jsonDic['Football Schedule'] = sports.getSch('fball')
        counter += 1

    if sport_name == 'bball' or sport_name == "all":
        jsonDic['Basketball Schedule'] = sports.getSch('bball')
        counter += 1
    
    if counter == 0:
        return {"message": "Invalid Param"}
    elif counter == 1:
        return list(jsonDic.values())[0]
    else:
        return jsonDic

#town decision route
@app.get("/api/v1/town/")
def townOptions(type_info: str = "all"):
    '''
    Picks which sport should be returned with the
    default being both
    '''
    #object that will be returned if counter > 1
    jsonDic = {}

    #counter to determine what is returned
    counter = 0

    #not case sensitive
    type_info.lower()

    if type_info == 'headline' or type_info == "all":
        jsonDic['Current Headlines'] = town.getHeadlines()
        counter += 1

    if type_info == 'events' or type_info == "all":
        jsonDic['Upcoming Events'] = town.getEvents()
        counter += 1
    
    if counter == 0:
        return {"message": "Invalid Param"}
    elif counter == 1:
        return list(jsonDic)[0]
    else:
        return jsonDic