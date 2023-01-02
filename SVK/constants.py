API = r"https://www.svk.se/services/controlroom/v2/"

"""
 Returns local (swedish) grid frequency health at specific time scope (1 seconds intervals)
 api function: freq
 fromDateTime: unixtime milliseconds
 toDateTime: unixtime milliseconds
"""
FREQ = "freq?fromDateTime={}&toDateTime={}"

"""
 Returns grid flow at specific time instance (1 minute intervals)
 api function: flow (elctric grid flow import/export)
 ticks: unixtime milliseconds
"""
FLOW = "map/flow?ticks={}"

"""
 Returns price of production zones at specific time instance (1 minute intervals)
 api function: price (euro/MWH)
 ticks: unixtime milliseconds
"""
PRICE = "map/price?ticks={}"

"""
 Returns production of given zone scope (1 minute intervals)
 api function: production (MW)
 date: date format (YYYY-MM-DD)
 countryCode: target zone (SE, FI, NO, etc...)
"""
PRODUCTION = "production?date={}&countryCode={}"

"""
 api function: prediction vs actual (MW) (1 hour intervals)
 date: date format (YYYY-MM-DD)
 biddingArea: target region (SE ONLY) (SE1, SE2, SE3, SE4, TO)
"""
SITUATION = "situation?date={}&biddingArea={}"

COUNTRY_CODES = ("TO", "SE", "NO", "DK", "FI", "EE",
                 "LV", "LT", "RU", "DE", "PL", "EN", "NL", "BY")
