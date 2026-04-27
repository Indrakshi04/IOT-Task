# Movie dataset
movies = [
    {"title": "Titanic", "features": ["romance", "drama", "ship"]},
    {"title": "Avatar", "features": ["sci-fi", "adventure", "alien"]},
    {"title": "The Notebook", "features": ["romance", "drama", "love"]},
    {"title": "Avengers", "features": ["action", "superhero", "marvel"]},
    {"title": "Interstellar", "features": ["sci-fi", "space", "future"]},
    {"title": "Iron Man", "features": ["action", "superhero", "tech"]},
]

# Function to calculate similarity score
def calculate_similarity(features1, features2):
    common = set(features1) & set(features2)
    total = set(features1) | set(features2)
    return len(common) / len(total)  # better scoring (ratio)

# Find closest movie if user types wrong name
def find_movie(name):
    name = name.lower()
    for movie in movies:
        if name in movie["title"].lower():
            return movie
    return None

# Recommendation function
def recommend(movie_name):
    selected_movie = find_movie(movie_name)

    if not selected_movie:
        print("❌ Movie not found! Try another name.")
        return

    print(f"\n🎬 You selected: {selected_movie['title']}")

    scores = []

    for movie in movies:
        if movie != selected_movie:
            score = calculate_similarity(
                selected_movie["features"], movie["features"]
            )
            scores.append((movie["title"], score))

    # Sort by highest similarity
    scores.sort(key=lambda x: x[1], reverse=True)

    print("\n🔥 Recommended movies:")
    for title, score in scores[:3]:
        print(f"{title}  (similarity: {round(score, 2)})")

# Run program
movie_name = input("Enter your preferred movie name: ")
recommend(movie_name)