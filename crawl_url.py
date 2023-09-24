from base import Crawler
from moviestowatch import Moviestowatch

urls = [
    {
        "url": "https://123chill.to/nandor-fodor-and-the-talking-mongoose/",
        "slug": "nandor-fodor-and-the-talking-mongoose",
        "post_type": "series",  # series | single
    },
    {
        "url": "https://123chill.to/nandor-fodor-and-the-talking-mongoose/",
        "slug": "nandor-fodor-and-the-talking-mongoose",
        "post_type": "series",  # series | single
    },
]


def main():
    for url in urls:
        film_data, episodes_data = Crawler().crawl_film(
            slug=url.get("slug"),
            href=url.get("url"),
            post_type=url.get("post_type"),
        )

        Moviestowatch(film=film_data, episodes=episodes_data).insert_film()


if __name__ == "__main__":
    main()
