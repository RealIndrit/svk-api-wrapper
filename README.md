# SVK API Wrapper
API wrapper for Svenska Kraftnät, accesses the same api endpoints as "kontrollrummet" (Swedish Electricity grid status website)

## FlowHelper
Info: Grid flow at specific time instance (updated in 1 minute intervals) 
Returns Float  (MW)
Params:
   1. ticks: UnixMillisecondSecond type (XXXXXXXXXX000)
   
## FrequencyHelper
Info: Local (swedish) grid frequency health at specific time scope (updated in 1 minute intervals, with 60 datapoints for each interval cycle) 
Returns: Float (Hz)
Params:
   1. lower_unix: UnixMillisecondSecond type (XXXXXXXXXX000)
   2. upper_unix: UnixMillisecondSecond type (XXXXXXXXXX000)

## PriceHelper
Info: Price of production zones at specific time instance (updated in 1 minute intervals)
Returns Float (euro/MWh)
Params:
   1. ticks: UnixMillisecondSecond type (XXXXXXXXXX000)

## ProductionHelper
Info: Production of given zone scope (1 minute intervals)
Returns: Int (MW)
Params:
   1. date: DateDay type (YYYY-MM-DD)
   2. countryCode: target zone ("SE", "FI", "NO", etc...)
   
## SituationHelper
Info: Prediction vs actual (Swedish grid zones ONLY) (1 hour intervals)
Returns: Planned: Float (MW), Result: Int (MW)
Params:
   1. date: DateDay type (YYYY-MM-DD)
   2. biddingArea: target region ("SE1", "SE2", "SE3", "SE4", "TO")


## TODO:
   1. Add CountryCode and Region Types