import wikipedia

class Wiki:
    def __init__(self, lang="en"):
        wikipedia.set_lang(lang)

    def get_city_description(self, city):
        try:
            return wikipedia.summary(city, sentences=5)
        except wikipedia.exceptions.PageError:
            return f"Data not found for this {city}"
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Found many variants of pages from wikipedia for {city}, choose first")
            best_match = e.options[0]
            return wikipedia.summary(best_match, sentences=5)
