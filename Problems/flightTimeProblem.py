"""

A rocket can have several engines each with different flight times. Engines can be taken off of rockets and stored in another location or be used in flight. 

Database functions: 
changeRocketLocation(rocketId, location)
getRocketEngines(rocketId)  


Write your answer in psuedoCode. Implement a function that returns the current flight time of an engine. 


// scenarios(if provided then copy over and explain how to handle each) 
// this is especially important for more "system design" type challenges
// We are assuming here that changeRocketLocation is only called when a new location is given 
// also we are assuming that the the function wants to return the totalFlight time across several flights
// This is why it is important to think about the problem simply and break it down into scenarios and then confirm with the interviewer

1. start flight for the first time 
    How do we check if its in flight for the first time 
    We need to check if its last location is not in flight
    Then we assign a start time which is current time and assign location to in flight
    
2. engine is no longer in flight 
    Check if last location was in flight and new location is not in flight
    Assign totalFlightTime to the elapsed time from flight start to currentTime 

TABLE Rocket
    rocketId            PRIMARY KEY
    location            STRING          // STORAGE, HANGAR, IN_FLIGHT, etc.

TABLE Engine
    engineId            PRIMARY KEY
    rocketId            FOREIGN KEY -> Rocket.rocketId NULL
    totalFlightTime     NUMBER
    flightStartTime     DATETIME NULL
    
FUNCTION updateRocketLocation(rocketId, newLocation)
oldLocation = getRocketLocation(rocketId)
engines = getRocketEngines(rocketId)

// 1. 
IF oldLocation != "in_flight" AND newLocation == IN_FLIGHT THEN
    FOR EACH engine in engines
        engine.flightStartTime = currentTime()
    END FOR
END IF 

// 2. 
IF oldLocation == "in_flight" AND newLocation = "not_in_flight" THEN 
    FOR EACH engine in engines
        engine.totalFlightTime = currentTime() - engine.flightStartTime + engineTotalFlightTime
        engine.flightStartTime = null; 
    END FOR 
END IF 
 engine.location = newLocation
 
END FUNCTION

FUNCTION getCurrentFlightTime(engineId)
engine = getEngineById(engineId);
RETURN  engine.totalFlightTime






FUNCTION updateRocketLocation(rocketId, newLocation)
oldLocation = getRocketLocation(rocketId)
engines = getRocketEngines(rocketId)
IF oldLocation != IN_FLIGHT AND newLocation == IN_FLIGHT THEN
    FOR EACH engine IN engines
        engine.flightStartTime = currentTime()
        saveEngine(engine)
    END FOR
END IF

IF oldLocation == IN_FLIGHT AND newLocation != IN_FLIGHT THEN
    FOR EACH engine IN engines
        elapsed = currentTime() - engine.flightStartTime
        engine.totalFlightTime = engine.totalFlightTime + elapsed
        engine.flightStartTime = null
        saveEngine(engine)
    END FOR
END IF

changeRocketLocation(rocketId, newLocation)
END FUNCTION


FUNCTION getCurrentFlightTime(engineId)
engine = getEngine(engineId)
IF engine.flightStartTime IS NOT null THEN
    RETURN engine.totalFlightTime
ELSE
    RETURN engine.totalFlightTime
END IF
END FUNCTION
"""
