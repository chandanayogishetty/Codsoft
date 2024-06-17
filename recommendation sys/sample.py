# Sample movie data with genres and languages
movies = [
    {'movie_id': 1, 'title': 'Pushpa,  Hanuman', 'genres': ['Action', 'Adventure'], 'language': 'Telugu'},
    {'movie_id': 2, 'title': 'Attack, War, Fighter', 'genres': ['Action'], 'language': 'Hindi'},
    {'movie_id': 3, 'title': 'DJ Tillu, F2', 'genres': ['Comedy'], 'language': 'Telugu'},
    {'movie_id': 4, 'title': 'Bhool Bhulaiyaa 2, Roohi, Laxmii', 'genres': ['Horror', 'Comedy'], 'language': 'Hindi'},
    {'movie_id': 5, 'title': 'Raju Gari Gadhi, Kanchana, Prema Katha Chitram', 'genres': ['Horror', 'Comedy'], 'language': 'Telugu'},
    {'movie_id': 6, 'title': 'RRR, Bahubali', 'genres': ['Action'], 'language': 'Telugu'},
    {'movie_id': 7, 'title': 'Karthikeya 2, Sahasam', 'genres': ['Adventure'], 'language': 'Telugu'},
    {'movie_id': 8, 'title': '3 Idiots, Cirkus, Crew, Good Newwz', 'genres': ['Comedy'], 'language': 'Hindi'},
    {'movie_id': 9, 'title': 'Rudhramadevi, Sye Raa Narasimha Reddy, Gautamiputra Satakarni', 'genres': ['History'], 'language': 'Telugu'},
    {'movie_id': 10, 'title': 'Padmaavat, Kesari, Samrat Prithviraj', 'genres': ['History'], 'language': 'Hindi'},
    {'movie_id': 11, 'title': 'Thugs of Hindostan, Ram Setu, Brahmāstra', 'genres': ['Adventure'], 'language': 'Hindi'},
]

def movies_genre(genre, lang):
    recom_movies = [
        movie['title'] for movie in movies 
        if genre in movie['genres'] and movie['language'] == lang
    ]    
    print(f"\nRecommended {genre} movies in {lang}:")
    if recom_movies:
        for title in recom_movies[:3]:
            print(title)
    else:
        print(f"No {genre} movies available in {lang}.")

lang = input("Enter preferred language (Telugu/Hindi): ").strip()
list_genres = set(genre for movie in movies for genre in movie['genres'])
print("\nAvailable genres:")
for genre in list_genres:
    print(genre)
genre = input("\nSelect a genre from the above list: ").strip()
movies_genre(genre, lang)
print("\n")