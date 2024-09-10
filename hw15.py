# -----------------------------------------------------
# 1.
#   SELECT COUNT(*)
# 	FROM eurovision_winners
# 	WHERE country = 'Israel';
# -----------------------------------------------------
# 2.
#   SELECT COUNT(*)
# 	FROM eurovision_winners
# 	WHERE country = host_country;
# -----------------------------------------------------
# 3.
#   SELECT year
# 	FROM eurovision_winners
# 	WHERE country = 'Israel';
# -----------------------------------------------------
# 4.
#   SELECT min(song_length_seconds)
# 	FROM song_details
# -----------------------------------------------------
# 5.
#   select *
# 	from eurovision_winners e
# 	join song_details s
# 		on e.year = s.year
# -----------------------------------------------------
# 6.
#   select e.song_name
# 	from eurovision_winners e
# 	join song_details s
# 			on e.year = s.year
# 	WHERE solo_performance = 1
# -----------------------------------------------------
# 7.
#   select count(*)
# 	from song_details s
# 	WHERE language = "English"
# -----------------------------------------------------
# 8.
#   SELECT avg(song_length_seconds)
# 	FROM song_details
# -----------------------------------------------------
# 9.
#   select e.year
# 	from eurovision_winners e
# 	WHERE song_name = "Hallelujah"
# -----------------------------------------------------
# 10.
#   select min(e.year)
# 	from eurovision_winners e
# 	join song_details s
# 			on e.year = s.year
# 	WHERE solo_performance = False
# -----------------------------------------------------
# 11.
#   select e.song_name, max(s.song_length_seconds)
# 	from eurovision_winners e
# 	join song_details s
# 			on e.year = s.year
# -----------------------------------------------------
# 12.
#   SELECT country, COUNT(*) AS win_count
# 	FROM eurovision_winners
# 	GROUP BY country
# 	ORDER BY win_count DESC
# 	LIMIT 1;
# -----------------------------------------------------
# 13.
#   SELECT country, COUNT(*) AS wins
# 	FROM eurovision_winners
# 	GROUP BY country
# 	ORDER BY wins DESC
# -----------------------------------------------------
# 14.
#   select song_name
# 	from eurovision_winners e
# 	join song_details s
# 			on e.year = s.year
# 	WHERE language = "French"
# -----------------------------------------------------
# 15.
#   select min(e.year) First_year, max(e.year) Last_year
# 	from eurovision_winners e
# 	WHERE country = "Israel"
# -----------------------------------------------------
# 16.
#   SELECT song_name, country, e.year, song_length_seconds as order_by_seconds
# 	FROM eurovision_winners e
# 	JOIN song_details s
# 			on e.year = s.year
# 	GROUP BY order_by_seconds
# 	ORDER BY max(song_length_seconds) DESC
# -----------------------------------------------------
# 17.
#   SELECT e.country, s.song_length_seconds
# 	FROM eurovision_winners e
# 	JOIN song_details s
# 		ON e.year = s.year
# 	WHERE s.song_length_seconds > (SELECT AVG(song_length_seconds)
# 		FROM song_details)
# -----------------------------------------------------
# 18.
#   SELECT e.song_name, s.song_length_seconds AS solo_length
# 	FROM eurovision_winners e
# 	JOIN song_details s
# 			ON e.year = s.year
# 	WHERE solo_performance = 1
# 	ORDER BY solo_length
# 	LIMIT 1;
# -----------------------------------------------------
# 19.
#   SELECT e.country, avg(s.song_length_seconds)
# 	FROM eurovision_winners e
# 	JOIN song_details s
# 			ON e.year = s.year
# 	WHERE solo_performance = 1
# 	GROUP BY e.country;
# -----------------------------------------------------
# 20.
#   SELECT count(*)
# 	FROM song_details s
# 	WHERE s.language NOT LIKE "English";
# -----------------------------------------------------
# 21.
#   SELECT count(DISTINCT(s.genre))
# 	FROM song_details s;
# -----------------------------------------------------
# 22.
#   SELECT e.winner
# 	FROM eurovision_winners e
# 	WHERE e.country LIKE "Israel"
# 	ORDER BY year DESC
# 	LIMIT 1;
# -----------------------------------------------------
