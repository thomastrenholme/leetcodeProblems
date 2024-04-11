
##Problem statement:

## You are a doordash driver atttempting to maximize the profits you can get from deliveries.
## You have a starting and ending hour of working, and cannot accept a job with a starting hour before your start hour
# or an ending hour after your ending hour of working.


## Some considerations: start_time <= end_time,
## len(d_starts) == len(d_ends) ==len(d_pays),
## All d_starts values and all d_ends values and d_pays values are positive integers.

##Fill out this (python3) function that returns the maximum profit you can achieve.


## Time complexity: O(N log N), Space complexity: O(T + N)
## Where:
    ## N is the number of deliveries.
    ## T is the number of hours between start_time and end_time.
def get_max_profit(start_time: int, end_time: int, d_starts: list[int], d_ends: list[int], d_pays: list[int]) -> int:

    ##Define max_profit_at_hour for each hour, each starts at 0.
    numWorkingHours = end_time-start_time+1
    max_profit_at_hour = [0] * numWorkingHours

    ##Sort by delivery end time
    deliveries = []
    for i in range(len(d_starts)):
        deliveries.append((d_starts[i], d_ends[i], d_pays[i]))

    ## Sort = O(nlogn)
    deliveries.sort(key=lambda x : x[1])

    ##Iterate through all working hours and find max profit until that hour
    for workingHour in range(start_time, end_time+1):

        ## Initialize max profit up to current hour as 0
        maxProfitUpToCurrentHour = 0

        ## iterate through all deliveries, examining ones that end at this hour.
        ## We can either keep the previous max profit until that hour from the previous hour OR
        ## consider accepting a delivery that ends at this hour. If we take one that ends at this hour, we will
        ## also take the profit of the max until the hour at which the new delivery we are taking starts at.

        print(max_profit_at_hour)
        for delivery in deliveries:
            deliveryStartHour = delivery[0]
            deliveryEndHour = delivery[1]
            deliveryPayment = delivery[2]

            ## If not ending at this hour, do not examine the delivery
            if deliveryEndHour != workingHour:
                continue

            ## Take the maximum between the potential new max profit of this delivery + the max starting at the
            ## hour of this delivery OR the current value for maxProfitUpToCurrentHour.
            potentialNewMaxProfitUpToCurrentHour = max_profit_at_hour[deliveryStartHour-start_time] + deliveryPayment
            maxProfitUpToCurrentHour = max(maxProfitUpToCurrentHour, potentialNewMaxProfitUpToCurrentHour)

        ## Once we've examined all possibilities for the current hour, set the maxProfitUpToCurrentHour for the
        ## current working hour
        max_profit_at_hour[workingHour-start_time] = maxProfitUpToCurrentHour

        ## Keep the maxProfitUpToCurrentHour from the last hour if no deliveries ended this hour
        if workingHour - start_time > 0 and maxProfitUpToCurrentHour == 0:
            max_profit_at_hour[workingHour-start_time] = max_profit_at_hour[workingHour-start_time-1]


##Return the max_profit_at_hour for the last working hour of the day
    return max_profit_at_hour[-1]



# Example usage:
start_time = 4
end_time = 8
d_starts = [1, 2, 3, 6]
d_ends = [2, 3, 7, 7]
d_pays = [10, 20, 30, 100]

print(get_max_profit(start_time, end_time, d_starts, d_ends, d_pays))  # Output: 60
