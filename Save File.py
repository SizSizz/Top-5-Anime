class Anime():
    def __init__(self, name, rating = 'N\A', synopsis = 'N\A', aired_time = 'N\A', season = 'N\A', year = 'N\A', studio = 'N\A', genres = 'N\A', episodes = 'N\A', rank = 'N\A', link = 'N\A'):
        self.name = name
        self.rating = rating
        self.synopsis = synopsis
        self.aired_time = aired_time
        self.season = season
        self.year = year
        self.studio = studio
        self.genres = genres
        self.episodes = episodes
        self.rank = rank
        self.link = link

    def __repr__(self):
        text = '''{name}\nLINK: {link}\nEPISODES: {episodes}    RATING: {rating}    RANK: {rank}    STUDIO: {studio}
AIRED TIME: {aired_time}    PREMIERED: {season} {year}  GENRES: {genres}
SYNOPSIS\n{synopsis}\n'''.format(name = self.name, link = self.link, episodes = self.episodes, rating = self.rating, rank = self.rank, studio = self.studio, aired_time = self.aired_time, season = self.season, year = self.year, genres = self.genres, synopsis = self.synopsis)
        
        return text

class Person():
    def __init__(self, name, ps1, ps2, ps3, ps4, ps5) -> None:
        

the_anime = Anime('joe')
print(the_anime)