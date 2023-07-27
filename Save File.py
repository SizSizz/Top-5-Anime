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

    def compare_anime(self, other):
        print(self.__repr__() + '= = = = = = = = = = = = = = = = = = = = = = = = = = =')
        return other.__repr__()

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
    syn_Steins_Gate = '''Eccentric scientist Rintarou Okabe has a never-ending thirst for scientific exploration. Together with his ditzy but well-meaning friend Mayuri Shiina and his roommate Itaru Hashida, Rintarou founds the Future Gadget Laboratory in the hopes of creating technological innovations that baffle the human psyche. Despite claims of grandeur, the only notable "gadget" the trio have created is a microwave that has the mystifying power to turn bananas into green goo.

However, when Rintarou decides to attend neuroscientist Kurisu Makise's conference on time travel, he experiences a series of strange events that lead him to believe that there is more to the "Phone Microwave" gadget than meets the eye. Apparently able to send text messages into the past using the microwave, Rintarou dabbles further with the "time machine," attracting the ire and attention of the mysterious organization SERN.

Due to the novel discovery, Rintarou and his friends find themselves in an ever-present danger. As he works to mitigate the damage his invention has caused to the timeline, he is not only fighting a battle to save his loved ones, but also one against his degrading sanity.'''
    syn_Attack_on_Titan = '''Centuries ago, mankind was slaughtered to near extinction by monstrous humanoid creatures called Titans, forcing humans to hide in fear behind enormous concentric walls. What makes these giants truly terrifying is that their taste for human flesh is not born out of hunger but what appears to be out of pleasure. To ensure their survival, the remnants of humanity began living within defensive barriers, resulting in one hundred years without a single titan encounter. However, that fragile calm is soon shattered when a colossal Titan manages to breach the supposedly impregnable outer wall, reigniting the fight for survival against the man-eating abominations.

After witnessing a horrific personal loss at the hands of the invading creatures, Eren Yeager dedicates his life to their eradication by enlisting into the Survey Corps, an elite military unit that combats the merciless humanoids outside the protection of the walls. Eren, his adopted sister Mikasa Ackerman, and his childhood friend Armin Arlert join the brutal war against the Titans and race to discover a way of defeating them before the last walls are breached.'''
    syn_Mob_Pyscho_100 = '''Eighth-grader Shigeo "Mob" Kageyama has tapped into his inner wellspring of psychic prowess at a young age. But the power quickly proves to be a liability when he realizes the potential danger in his skills. Choosing to suppress his power, Mob's only present use for his ability is to impress his longtime crush, Tsubomi, who soon grows bored of the same tricks.

In order to effectuate control on his skills, Mob enlists himself under the wing of Arataka Reigen, a con artist claiming to be a psychic, who exploits Mob's powers for pocket change. Now, exorcising evil spirits on command has become a part of Mob's daily, monotonous life. However, the psychic energy he exerts is barely the tip of the iceberg; if his vast potential and unrestrained emotions run berserk, a cataclysmic event that would render him completely unrecognizable will be triggered. The progression toward Mob's explosion is rising and attempting to stop it is futile.'''
    syn_Fullmetal_Alchemist_Brotherhood = '''After a horrific alchemy experiment goes wrong in the Elric household, brothers Edward and Alphonse are left in a catastrophic new reality. Ignoring the alchemical principle banning human transmutation, the boys attempted to bring their recently deceased mother back to life. Instead, they suffered brutal personal loss: Alphonse's body disintegrated while Edward lost a leg and then sacrificed an arm to keep Alphonse's soul in the physical realm by binding it to a hulking suit of armor.

The brothers are rescued by their neighbor Pinako Rockbell and her granddaughter Winry. Known as a bio-mechanical engineering prodigy, Winry creates prosthetic limbs for Edward by utilizing "automail," a tough, versatile metal used in robots and combat armor. After years of training, the Elric brothers set off on a quest to restore their bodies by locating the Philosopher's Stone—a powerful gem that allows an alchemist to defy the traditional laws of Equivalent Exchange.

As Edward becomes an infamous alchemist and gains the nickname "Fullmetal," the boys' journey embroils them in a growing conspiracy that threatens the fate of the world.'''

synopsis = anime_synopsis()
#Anime Shows
s_Naruto_Shippuuden = Anime('Naruto_Shippuuden', '8.26', synopsis.syn_Naruto_Shippuuden, 'Feb 15, 2007 - Mar 23, 2017', 'Winter', '2007', 'Pierrot', 'Action, Adventure, Fantasy', '500', '#288', 'https://myanimelist.net/anime/1735')
s_Steins_Gate = Anime('Steins;Gate', '9.07', synopsis.syn_Steins_Gate, 'April 6, 2011 - Sep 14, 2011', 'Spring', '2011', 'White Fox', 'Drama, Sci-Fi, Suspense', '47', '#2', 'https://myanimelist.net/anime/9253/Steins_Gate')
s_Attack_on_Titan = Anime('Attack on Titan', '8.54', synopsis.syn_Attack_on_Titan, 'April 7, 2013 - Sep 29, 2013', 'Spring', '2013', 'Wit Studio', 'Action, Award Winning, Drama, Suspense', '99', '#108', 'https://myanimelist.net/anime/16498/Shingeki_no_Kyojin')
s_Mob_Pyscho_100 = Anime('Mob Psycho 100', '8.49', synopsis.syn_Mob_Pyscho_100, 'July 11m 2016 - Sep 27, 2016', 'Summer', '2016', 'Bones', 'Action, Comedy, Supernatural', '37', '#134', 'https://myanimelist.net/anime/32182')
s_Fullmetal_Alchemist_Brotherhood = Anime('Fullmetal Alchemist: Brotherhood', '9.10', synopsis.syn_Fullmetal_Alchemist_Brotherhood, 'April 5, 2009 - July 4, 2010', 'Spring', '2009', 'Bones', 'Action, Drama, Adventure, Fantasy', '64', '#1', 'https://myanimelist.net/anime/5114')

#People
the_anime = Person('Siz', s_Naruto_Shippuuden, s_Steins_Gate, s_Attack_on_Titan, s_Mob_Pyscho_100, s_Fullmetal_Alchemist_Brotherhood)
print(the_anime)

#Program
print('Welcome to Top 5 Anime!\nThis is where you can post your top 5 animes, view other\'s top 5, view anime show information, and compare them! )
menu_choice = input('')
