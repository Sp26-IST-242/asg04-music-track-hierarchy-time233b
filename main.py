"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""
from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist
from music_track import MusicTrack

def main():
    #create  artists
    Kendrick =Artist("Kendrick Lamar", "Hip-Hop")
    Alanis = Artist("Alanis Morissette","Alternative")
    Joe = Artist("Joe Rogan", "Comedy")
    Sarah = Artist("Sarah Koenig", "Journalism")
    #create albums
    Damn = Album("Damn", True, [2017,2018])
    Jagged = Album("Jagged Little Pill", False, [1995,1996])
    Joe_exp = Album("The Joe Rogan Experience", True, [2009,2010])
    Serial = Album("Serial", False, [2014,2015])
    #create tracks
    Song1 = Song(Kendrick, Damn, 220)
    Song2 = Song(Alanis, Jagged,245)
    Podcast1 = Podcast(Joe, Joe_exp,9000, is_explicit=True)
    Podcast2 = Podcast(Sarah, Serial,5400, is_explicit=False)# default is_explicit is false, but I did it anyway
    #create playlist
    p = Playlist("p")
    p.add_track(Song1)
    p.add_track(Song2)
    p.add_track(Podcast1)
    p.add_track(Podcast2)
    #print before sorting
    print("Before sorting:")
    print(p)
    #sort release year
    p.sort_by_release_year()
    #print after sorting
    print("\nAfter sorting:")
    print(p)
    if __name__ == "__main__":
        main()

    
