import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
												"A story of a boy and his toys that come to life",
												"https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY606_.jpg",
												"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
										 "A Marine on an alien planet",
										 "http://www.impawards.com/2009/posters/avatar.jpg",
										 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
														 "Storyline",
														 "https://images-na.ssl-images-amazon.com/images/I/51v8TQDTF-L.jpg",
														 "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
													"Storyline",
													"https://images-na.ssl-images-amazon.com/images/I/51MJQKcJVFL._SY450_.jpg",
													"https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie("Midnight in Paris",
																"Storyline",
																"https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L.jpg",
																"https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Midnight in Paris",
													 "Storyline",
													 "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",
													 "https://www.youtube.com/watch?v=4S9a5V9ODuY&t=9s")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)