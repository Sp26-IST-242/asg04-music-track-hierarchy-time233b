"""
Concrete subclass of MusicTrack representing a podcast episode.

Podcast differs from Song in two ways:
  1. It has one extra field: is_explicit (bool), defaulting to False.
     The default value replaces Java-style constructor overloading — one
     __init__ handles both the explicit and non-explicit cases.
  2. play_time_formatted() returns 'HH:MM:SS' instead of 'MM:SS', because
     podcast episodes are typically longer than an hour.

    Return the duration as 'HH:MM:SS' (all parts zero-padded).

        Examples
        --------
        9000 seconds → '02:30:00'
        5400 seconds → '01:30:00'
        3661 seconds → '01:01:01'

 3. Override __str__ for a human-readable representation.
        Return '(<artist>) <album>, duration: <HH:MM:SS> is explicit: <bool>'.

        Example:
            (Joe Rogan, Comedy) The Joe Rogan Experience active = True,
             debut year: 2009, duration: 02:30:00 is explicit: True
"""
from music_track import MusicTrack


class Podcast(MusicTrack):
    def __init__(self, artist, album, duration_seconds, is_explicit=False):
        super().__init__(artist, album, duration_seconds)
        self._is_explicit = is_explicit

    @property
    def is_explicit(self):
        return self._is_explicit

    def play_time_formatted(self) -> str:
        hours = self.duration_seconds // 3600
        minutes = (self.duration_seconds % 3600) // 60
        seconds = self.duration_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __str__(self):
        return f"({self.artist}) {self.album}, duration: {self.play_time_formatted()} is explicit: {self.is_explicit}"