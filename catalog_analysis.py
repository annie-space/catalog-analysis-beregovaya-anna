import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Средняя оценка по каталогу, округлённая до 1 знака."""
    total = sum(m["rating"] for m in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """самый старый, самый новый, средний возраст"""
    ages = [current_year - m["year"] for m in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    """Минуты - строка"""
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating):
    """Оценка по рейтингу."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    return "слабо" if rating < 5 else "средне"


def decade_label(year):
    """Метка десятилетия"""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy(movies):
    """Не комедии"""
    for m in movies:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])


def find_first_masterpiece(movies):
    """Фильм с рейтингом выше 9.0"""
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Найден шедевр: {movies[i]['title']}")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold минут"""
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """Title Case вручную, без str.title()."""
    words = title.split()
    return " ".join(w[0].upper() + w[1:] for w in words)


def make_slug(title):
    """С маленькой"""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Единая строка отчёта"""
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, '
        f'жанры: {genres}'
    )


def titles_sorted_by_rating(movies):
    """Фильмы, по убыванию рейтинга"""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Топ-N кортежей (title, rating) по рейтингу"""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]


def count_by_genre(movies):
    """жанр: количество фильмов, через dict.get()"""
    counts = {}
    for m in movies:
        for genre in m["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """актёр: [названия фильмов]"""
    filmography = {}
    for m in movies:
        for actor in m["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(m["title"])
    return filmography


def high_rated_titles(movies):
    """title: rating для фильмов с рейтингом выше среднего"""
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


def all_genres(movies):
    """Множество всех уникальных жанров"""
    genres = set()
    for m in movies:
        genres |= m["genres"]
    return genres


def common_actors(movie1, movie2):
    """Актёры, снимавшиеся в обоих фильмах"""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры из movies_a, которых нет в movies_b"""
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    """Генератор: фильмы с рейтингом >= min_rating."""
    for m in movies:
        if m["rating"] >= min_rating:
            yield m


def total_duration_above_seven(movies):
    """Суммарная длительность фильмов с рейтингом > 7"""
    return sum(m["duration_min"] for m in movies if m["rating"] > 7)