import random
from typing import List, Tuple

class Player:
    def __init__(self, name: str, position: str, skill_level: int, **kwargs) -> None:
        if skill_level < 0 or skill_level > 100:
            raise ValueError("The skill level is not between 0 and 100")
        self.name = name
        self.position = position
        self.skill_level = skill_level
        self.additional = kwargs  

        for key, value in kwargs.items():
            self.__dict__[key] = value

    def generate_performance_points(self) -> int:
        return max(0, min(100, self.skill_level + random.randint(-5, 5)))

    def update_skill_level(self, adjustment: int) -> None:
        self.skill_level += adjustment
        if self.skill_level < 0:
            self.skill_level = 0
        elif self.skill_level > 100:
            self.skill_level = 100

    def get_player_info(self) -> dict:
        info = {
            'name': self.name,
            'position': self.position,
            'skill_level': self.skill_level
        }
        info.update(self.additional)
        return info

class Team:
    def __init__(self, name: str, players: List['Player'] = None) -> None:
        self.name = name
        if players is None:
            self.players = []
        else:
            self.players = list(players)

    def add_player(self, player: 'Player') -> None:
        if len(self.players) >= 11:
            raise Exception(f"Team {self.name} cannot have more than 11 players.")

        if not isinstance(player, Player):
            raise Exception(f"Object must be an instance of Player.")
        
        for existing_player in self.players:
            if existing_player.name.lower() == player.name.lower():
                raise Exception(f"Player {player.name} is already in the team (case-insensitive).")
        
        self.players.append(player)

    def remove_player(self, player: 'Player') -> None:
        if player in self.players:
            self.players.remove(player)
        else:
            raise Exception(f"Player {player.name} is not in the team.")

    def calculate_total_score(self, simulate: bool = False) -> float:
        total_score = 0
        for player in self.players:
            if simulate:
                total_score += player.generate_performance_points()
            else:
                total_score += player.skill_level
            
        if len(self.players) == 0:
            return 0
        
        average_score = round(total_score / len(self.players), 2)
        return average_score



class FantasyLeague:
    def __init__(self, teams: List['Team'] = None) -> None:
        if teams is None:
            self.teams = []
        else:
            self.teams = list(teams)

        if self.teams:
            player_count = len(self.teams[0].players)
            if not all((len(team.players) == player_count) for team in self.teams):
                raise Exception("All teams must have the same number of players.")

    def add_team(self, team: 'Team') -> None:
        if any(existing_team.name.lower() == team.name.lower() for existing_team in self.teams):
            raise Exception(f"Team {team.name} already exists in the league.")
        
        if not isinstance(team, Team):
            raise Exception(f"Object must be an instance of Team.")
        
        if len(self.teams) > 9: 
            raise Exception("The league cannot have more than 10 teams.")
        
        if len(team.players) == 0:
            raise Exception(f"Team {team.name} has no players.")
            
        if self.teams:
            player_count = len(self.teams[0].players)
            if player_count != len(team.players):  
                raise Exception("All teams must have the same number of players.")

        for existing_team in self.teams:
            if set(player.name.lower() for player in existing_team.players) == set(player.name.lower() for player in team.players):
                raise Exception(f"Team {team.name} has the same set of players as an existing team.")
        
        self.teams.append(team)

    def calculate_team_rankings(self, simulate: bool = False) -> List[Tuple[str, float]]:
        if len(self.teams) < 2:
            raise Exception("At least two teams are required to simulate a season.")
        
        team_score = []
        
        for team in self.teams:
            score = team.calculate_total_score(simulate)
            team_score.append((team.name, score))
            
        sorted_score = sorted(team_score, key=lambda x: (-x[1], x[0]))

        return sorted_score


class Trade:
    def __init__(
        self,
        team1: Team,
        team2: Team,
        players_team1: list[Player],
        players_team2: list[Player],
    ) -> None:
        self.team1 = team1
        self.team2 = team2
        self.players_team1 = players_team1
        self.players_team2 = players_team2

    def propose_trade(self) -> bool:
        for player in self.players_team1:
            if player not in self.team1.players:
                raise Exception(f"Player {player.name} is not part of {self.team1.name}.")

        for player in self.players_team2:
            if player not in self.team2.players:
                raise Exception(f"Player {player.name} is not part of {self.team2.name}.")
                
        if len(self.players_team1) != len(self.players_team2):
            raise Exception("Trade rejected: Players to be traded on both sides do not match.")
        
        skill_team1 = sum(player.skill_level for player in self.players_team1)
        skill_team2 = sum(player.skill_level for player in self.players_team2)

        if abs(skill_team1 - skill_team2) > 10:
            raise Exception("Trade rejected: Unfair trade.")
        
        for player in self.players_team1:
            player.update_skill_level(2)

        for player in self.players_team2:
            player.update_skill_level(2)
        
        for player in self.players_team1:
            self.team1.players.remove(player)
            self.team2.players.append(player)
            
        for player in self.players_team2:
            self.team2.players.remove(player)
            self.team1.players.append(player)
            
        return True
