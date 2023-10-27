try:
    from dataclasses import dataclass
    import random
    import os
    print("Successfully Imported Libraries")
except ImportError as ie:
    print("Error Importing Libraries: ")
    print("Details: {}".format(ie))
    exit(1)

@dataclass(frozen=True)
class Outcome:
    """ Class for keeping the outcome of different bets """
    name: str
    odds: int

    """ Instance method to calculate payout """
    def winAmount(self, amount: float) -> float:
        return self.odds * amount
    
    def __ne__(self, other: object) -> bool:
        return other.name != self.name 
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other: object) -> bool:
        return other.name == self.name
    
    def __str__(self) -> str:
        return f"{self.name:s} ({self.odds:d}:1)"
    
    def __repr__( self ):
        return f"{self.__class__.__name__:s}(name={self.name!r}, odds={self.odds!r})"


class Bin(frozenset):
    """ 
        Class which contain a collection of Outcome instances 
        which reflect the winning bets that are paid for a particular bin on a Roulette wheel
    """


class Wheel():
    """Adds the given Outcome object to the Bin instance with the given number."""
    def __init__(self) -> None:
        seed_bytes = os.urandom(4)  # You can adjust the number of bytes as needed
        seed_value = int.from_bytes(seed_bytes, byteorder='big')
        self.bins = tuple(Bin() for i in range(38))
        self.rng = random.Random(seed_value)
        
    def addOutcome(self,number: int, outcome: Outcome) -> None:
        current_bin = self.bins[number]
        updated_bin = current_bin | frozenset({outcome})
        self.bins = self.bins[:number] + (updated_bin,) + self.bins[number + 1:]


    def choose(self) -> Bin:
        """ Generates a random number between 0 and 37, and returns the randomly selected Bin instance """
        return self.rng.choice(self.bins)
    
    def get(self, bin: int) -> Bin:
        """ Chooses a Bin selected at random from the wheel. """
        return self.bins[bin]