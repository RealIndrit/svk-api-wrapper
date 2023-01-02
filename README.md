# SVK API Wrapper
API wrapper for Svenska Kraftnät, accesses the same api endpoints as "kontrollrummet" (Swedish Electricity grid status website)

## FlowHelper
Returns grid flow at specific time instance (updated in 1 minute intervals) (MW)
Params:
   1. ticks: unixtime milliseconds
## FrequencyHelper
Returns local (swedish) grid frequency health at specific time scope (updated in 1 seconds intervals) (Hz)
Params:
   1. lower_unix: unixtime milliseconds
   2. upper_unix: unixtime milliseconds
## PriceHelper
Returns price of production zones at specific time instance (updated in 1 minute intervals) (euro/MWh)
Params:
   1. ticks: unixtime milliseconds
## ProductionHelper
Returns production of given zone scope (1 minute intervals) (MW)
Params:
   1. date: date format (YYYY-MM-DD)
   2. countryCode: target zone (SE, FI, NO, etc...)
## SituationHelper
Returns prediction vs actual (Swedish grid zones ONLY) (1 hour intervals) (MW)
Params:
   1. date: date format (YYYY-MM-DD)
   2. biddingArea: target region (SE1, SE2, SE3, SE4, TO)