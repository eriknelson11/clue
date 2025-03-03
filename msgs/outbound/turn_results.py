import accusation

# message to be sent out to all players after a players turn has been processed
class TurnResults:
    def __init__(self, suspect, accusation: accusation.Accusation, your_turn: bool, player_locations):
        self.suspect = suspect # the suspect/player whose turn was just processed
        self.accusation = accusation # their accusation
        self.your_turn = your_turn # notifying which player should make a move next
        self.player_locations = player_locations # updated player locations after turn was processed
