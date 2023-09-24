from base import Crawler
from moviestowatch import Moviestowatch

url = "https://123chill.to/nandor-fodor-and-the-talking-mongoose/"
slug = "nandor-fodor-and-the-talking-mongoose"
post_type = "series"
# post_type = "series"
# post_type = "single"


def main():
    film_data, episodes_data = Crawler().crawl_film(
        slug=slug,
        href=url,
        post_type=post_type,
    )

    Moviestowatch(film=film_data, episodes=episodes_data).insert_film()


if __name__ == "__main__":
    main()
