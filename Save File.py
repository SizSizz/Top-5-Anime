class Anime():
    def __init__(self, name = 'N\A', rating = 'N\A', synopsis = 'N\A', aired_time = 'N\A', season = 'N\A', year = 'N\A', studio = 'N\A', genres = 'N\A', episodes = 'N\A', rank = 'N\A', link = 'N\A'):
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
    def __init__(self, name = "N\A", ps1 = Anime(), ps2 = Anime(), ps3 = Anime(), ps4 = Anime(), ps5 = Anime()):
        self.name = name
        self.ps1 = ps1
        self.ps2 = ps2
        self.ps3 = ps3
        self.ps4 = ps4
        self.ps5 = ps5
        self.anime_list = [self.ps1, self.ps2, self.ps3, self.ps4, self.ps5]
    
    def __repr__(self):
        text = '{name} - Top 5 Anime:\n'.format(name = self.name)
        for anime_name in self.anime_list:
            text += '* {anime}\n'.format(anime = anime_name.name)
        return text
    
#Anime Synopsis
class anime_synopsis():
    syn_Naruto_Shippuuden = '''It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now Akatsuki, the mysterious organization of elite rogue ninja, is closing in on their grand plan which may threaten the safety of the entire shinobi world.

Although Naruto is older and sinister events loom on the horizon, he has changed little in personality—still rambunctious and childish—though he is now far more confident and possesses an even greater determination to protect his friends and home. Come whatever may, Naruto will carry on with the fight for what is important to him, even at the expense of his own body, in the continuation of the saga about the boy who wishes to become Hokage.'''
synopsis = anime_synopsis()
#Anime Shows
s_Naruto_Shippuuden = Anime('Naruto_Shippuuden', '8.26', synopsis.syn_Naruto_Shippuuden, 'Feb 15, 2007 - Mar 23, 2017', 'Winter', '2007', 'Pierrot', 'Action, Adventure, Fantasy', '500', '288', 'https://myanimelist.net/anime/1735')
s_Steins_Gate = Anime('Steins;Gate', '9.07')

#People
the_anime = Person('tim', s_Naruto_Shippuuden, s_Steins_Gate)
print(the_anime)

