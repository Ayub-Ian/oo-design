try:
    from dataclasses import dataclass
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