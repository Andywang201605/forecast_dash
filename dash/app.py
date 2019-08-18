from flask import Flask
from multipage import Route, MultiPageApp
from pages import Index, Series, Filter, Stats, Methodology, About


class MyApp(MultiPageApp):
    def get_routes(self):

        return [
            Route(Index, "index", "/"),
            Route(Series, "series", "/series/"),
            Route(Filter, "filter", "/filter/"),
            Route(Stats, "stats", "/stats/"),
            Route(Methodology, "methodology", "/methodology/"),
            Route(About, "about", "/about/"),
        ]


server = Flask(__name__)

app = MyApp(name="", server=server, url_base_pathname="")

if __name__ == "__main__":
    server.run(host="0.0.0.0", debug=True)
