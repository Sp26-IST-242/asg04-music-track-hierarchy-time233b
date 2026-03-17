"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""

class Album:
    def __init__ (self, title, active: bool, years: list[int]):
        if not years:
            raise ValueError("Years list cannot be empty.")
        self._title = title
        self._active = active
        self._years = years.copy()  # Defensive copy

    @property
    def title(self):
        return self._title

    @property
    def active(self):
        return self._active

    @property
    def years(self):
        return self._years.copy()  # Defensive copy
    @property
    def debut_year(self) -> int:
        return self._years[0]
    def __str__(self):
        return f"{self._title} active = {self._active}, debut year: {self.debut_year}"