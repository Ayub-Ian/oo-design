try:
    from dataclasses import dataclass
    import random
    import os
    from typing import Set
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
        if bin < 0 or bin > len(self.bins):
            return None
        
        return self.bins[bin]
    
class BinBuilder:
    """ Creates the Outcome instances for all of the 38 individual Bin on a Roulette wheel. """
    def __init__(self) -> None:
        pass
    
    def buildBins(self, wheel: Wheel) -> None:
        pass

    @staticmethod
    def StraightBet() -> list[Bin]:
        bins_outcomes: Set[Outcome] = []

        for position in range(38):
            if position == 0:
                # Create outcomes for "0"
                outcomes = {Outcome(name="0", odds=35)}
            elif position == 37:
                # Create outcomes for "00"
                outcomes = {Outcome(name="00", odds=35)}
            else:
                # Create outcomes for numbers 1 to 36
                outcomes = {Outcome(name=str(position), odds=35)}

            bins_outcomes.append(outcomes)

        # Create Bin instances using the bins_outcomes list
        bins = [Bin() for _ in range(38)]

        for position, outcomes in enumerate(bins_outcomes):
            bins[position] = Bin(outcomes=outcomes)
        
        return bins
    
    @staticmethod
    def StreetBet() -> list[Bin]:
        street_bets = []

        for r in range(12):
            # calculate the first column number of the row
            n = 3 * r + 1

             # create a set representing the sreet numbers of the current row
            street = {n , n+1, n+2}
            
            # Create an Outcome object for the street with odds of 11:1
            street_outcome = Outcome(name=f"Street {n}, {n+1}, {n+2}", odds=11)

            # Create a Bin for each number in the street and associate the street outcome
            for _ in street:
                bins_outcomes = {street_outcome}
                bin_instance = Bin(outcomes=bins_outcomes)
                street_bets.append(bin_instance)

        return street_bets    
    
    @staticmethod
    def LineBets() -> list[Bin]:

        line_bets = []
        
        for r in range(11):
            # calculate the first column number of the row
            n = 3 * r + 1

            # create a set representing the line numbers of the current row/line
            line_numbers = {n,n + 1, n+2, n+3, n+4, n+5}

            # Create an Outcome object for the line with odds of 5:1
            line_outcome = Outcome(name=f"Line {n} - {n+5}", odds=5)

            # Create a Bin for each number in the line and associate the line outcome
            for _ in line_numbers:
                bin_outcome = {line_outcome}
                bin_instance = Bin(outcomes=bin_outcome)
                line_bets.append(bin_instance)
        
        return line_bets

    @staticmethod
    def DozenBets():
        bins = [Bin() for _ in range(1,37)]
        for d in range(3):

            dozen_outcome = {Outcome(name=f"{d + 1}", odds=2)}
            

            for m in range(12):
                bin_number = 12 * d + m + 1
                bins[bin_number] = Bin(outcomes={dozen_outcome})
        
        return bins
    
    @staticmethod
    def ColumnBets():
        bins = [Bin() for _ in range(1,37)]
        for c in range(3):

            column_outcome = {Outcome(name=f"{c + 1}", odds=2)}
            

            for r in range(12):
                bin_number = 3 * r + c + 1
                bins[bin_number] = Bin(outcomes={column_outcome})
        
        return bins
    
    @staticmethod
    def EvenMoneyBets():
        bins = [Bin() for _ in range(1,37)]
        red_outcome = Outcome("Red", 1)
        black_outcome = Outcome("Black", 1)
        even_outcome = Outcome("Even", 1)
        odd_outcome = Outcome("Odd", 1)
        high_outcome = Outcome("High", 1)
        low_outcome = Outcome("Low", 1)

        for n in range(1,37):
            if n < 19:
                bin[n] = Bin(outcomes=low_outcome)
            else:
                bin[n] = Bin(outcome=low_outcome)

            
