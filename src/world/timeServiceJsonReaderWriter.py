import json
from world.timeService import TimeService

class TimeServiceJsonReaderWriter:
    
        def createJsonFromTimeService(self, timeService):
            return {
                "time": timeService.time,
                "day": timeService.day
            }
    
        def createTimeServiceFromJson(self, timeServiceJson, player, stats):
            timeService = TimeService(player, stats)
            timeService.time = timeServiceJson["time"]
            timeService.day = timeServiceJson["day"]
            return timeService
    
        def writeTimeServiceToFile(self, timeService, jsonFile):
            timeServiceJson = self.createJsonFromTimeService(timeService)
            json.dump(timeServiceJson, jsonFile)
        
        def readTimeServiceFromFile(self, jsonFile):
            timeServiceJson = json.load(jsonFile)
            return self.createTimeServiceFromJson(timeServiceJson)