Author: @ilsep93

* How many taxi trips were totally made on January 15?

20689

```SQL
SELECT COUNT(*)
FROM green_taxi_trips
WHERE CAST(green_taxi_trips.lpep_pickup_datetime AS DATE)='2019-01-15'
```

* Which was the day with the largest trip distance?

"2019-01-15 19:27:58"	117.99

```SQL
SELECT lpep_pickup_datetime, trip_distance FROM green_taxi_trips
WHERE trip_distance = (
   SELECT MAX (trip_distance)
   FROM green_taxi_trips
)
```

* In 2019-01-01 how many trips had 2 and 3 passengers?

```SQL
SELECT COUNT(*)
FROM green_taxi_trips
WHERE passenger_count=2 AND CAST(lpep_pickup_datetime AS DATE)='2019-01-01';

SELECT COUNT(*)
FROM green_taxi_trips
WHERE passenger_count=3 AND CAST(lpep_pickup_datetime AS DATE)='2019-01-01';
```

* For the passengers picked up in the Astoria Zone which was the drop up zone that had the largest tip?

```SQL
WITH astoria_max_tip as (
SELECT 
	MAX(tip_amount) as max_tip,
	taxi."DOLocationID",
	zpu."Zone"
FROM green_taxi_trips taxi
LEFT JOIN zones zpu
ON taxi."PULocationID" = zpu."LocationID"
WHERE zpu."Zone"='Astoria'
GROUP BY taxi."DOLocationID", zpu."Zone"
ORDER BY max_tip DESC
LIMIT 1
)
SELECT zpu."Zone", max_tip
FROM astoria_max_tip
JOIN zones zpu
ON astoria_max_tip."DOLocationID" = zpu."LocationID"
```