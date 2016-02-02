class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

sut_den = Song(["Sut den op fra slap, kaelling",
                "Jeg loeber ikke med sladder"])

list_lyric = ["I don't want to set the World on fire", "I just want to put a flame in your heart"]

world_on_fire = Song(list_lyric)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sut_den.sing_me_a_song()

world_on_fire.sing_me_a_song()
