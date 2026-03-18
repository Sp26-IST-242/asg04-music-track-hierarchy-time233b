"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""
class Playlist:
    def __init__(self):
        self._tracks = []
    @property
    def tracks(self):
        return self._tracks.copy() #Defensive copy
    def add_track(self, track):
        self._tracks.append(track)
    def clear_playlist(self):
        self._tracks.clear() # clear the list
    def sort_by_release_year(self):
        self._tracks.sort() # sort by release year using Musictrack.
    def __str__(self):
        return "\n".join(str(track) for track in self._tracks)
   