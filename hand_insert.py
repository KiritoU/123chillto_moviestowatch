from moviestowatch import Moviestowatch

film_data = {
    "title": "Only Murders in the Building – Season 3",
    "slug": "only-murders-in-the-building-season-3",
    "description": "Watch Only Murders in the Building Season 3 Online Free. Season three finds Charles, Oliver & Mabel investigating a murder behind the scenes of a Broadway show. Ben Glenroy is a Hollywood action star whose Broadway debut is cut short by his untimely death. Aided by co-star Loretta Durkin, our trio embarks on their toughest case yet, all while director Oliver desperately attempts to put his show back together. Curtain up!",
    "post_type": "series",
    "trailer_id": "zx9-y-U29OI",
    "cover_src": "https://image.tmdb.org/t/p/w300/cV3Qfiv0bTwrnsvSnDnN22i33V0.jpg",
    "extra_info": {
        "TV Status": "Returning Series",
        "Release Year": "2023",
        "First air date": "2023-08-08",
        "Genres": "Comedy,Mystery",
        "Actors": "John Robert Hoffman,Steve Martin",
        "Country": "United States",
        "Starring": "Martin Short,Meryl Streep,Michael Cyril Creighton,Paul Rudd,Selena Gomez,Steve Martin",
        "Created by": "John Robert Hoffman,Steve Martin",
        "Production": "20th Television",
    },
}

episodes_data = {
    "0": {
        "name": "Dood",
        "episodes": {
            "01: The Show Must...": "https://doods.pro/e/8cixe0rg9cgnviguej5sdi5lhbrxzrq1",
            "02: The Beat Goes On": "https://doods.pro/e/j5oon095g6kjt4emob8aq0irqnc3t3yu",
            "03: Grab Your Hankies": "https://doods.pro/e/71xr4vdhkyn6083j11ugqacaefnn7ozg frameborder=",
            "04: The White Room": "https://doods.pro/e/78dktdmt6id6ud9n46r10aeqi2ih387m",
            "05: Ah, Love!": "https://doods.pro/e/5wwze768ohl1iw1dc8vd4aebatckgfuj",
        },
    },
    "1": {
        "name": "Vidsrc",
        "episodes": {
            "01: The Show Must...": "https://vidsrc.me/embed/tt12851524/3-1/",
            "02: The Beat Goes On": "https://vidsrc.me/embed/tt12851524/3-2/",
            "03: Grab Your Hankies": "https://vidsrc.me/embed/tt12851524/3-3/",
            "04: The White Room": "https://vidsrc.me/embed/tt12851524/3-4/",
            "05: Ah, Love!": "https://vidsrc.me/embed/tt12851524/3-5/",
        },
    },
}


def main():
    Moviestowatch(film=film_data, episodes=episodes_data).insert_film()


if __name__ == "__main__":
    main()
