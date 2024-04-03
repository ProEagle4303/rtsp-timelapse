import datetime
def active(config):
    time = int(datetime.datetime.now().strftime("%H"))
    print(time)
    for x in range(len(config["activeTimes"])):
        if int(config["activeTimes"][x]["start"]) < time and int(config["activeTimes"][x]["end"]) > time:
            return True
    return False





