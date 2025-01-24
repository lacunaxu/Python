import random
from typing import List, Tuple

class Player:
    """
    A class representing a player in the fantasy league.

    Attributes:
        name (str): The name of the player.
        position (str): The position the player plays.
        skill_level (int): The skill level of the player (0-100).
        additional (dict): Additional attributes for the player.
    """

    def __init__(self, name: str, position: str, skill_level: int, **kwargs) -> None:
        """
        Initialize a player with name, position, skill level, and additional attributes.

        Args:
            name (str): Name of the player.
            position (str): Position of the player.
            skill_level (int): Skill level of the player.
            **kwargs: Additional attributes for the player.

        Raises:
            ValueError: If skill_level is not between 0 and 100.
        """
        if skill_level < 0 or skill_level > 100:
            raise ValueError("The skill level is not between 0 and 100")
        self.name = name
        self.position = position
        self.skill_level = skill_level
        self.additional = kwargs

        for key, value in kwargs.items():
            self.__dict__[key] = value

    def generate_performance_points(self) -> int:
        """
        Generate performance points for the player.

        Returns:
            int: Performance points within 0-100 range.
        """
        return max(0, min(100, self.skill_level + random.randint(-5, 5)))

    def update_skill_level(self, adjustment: int) -> None:
        """
        Update the skill level of the player.

        Args:
            adjustment (int): Value to adjust the skill level by.
        """
        self.skill_level += adjustment
        if self.skill_level < 0:
            self.skill_level = 0
        elif self.skill_level > 100:
            self.skill_level = 100

    def get_player_info(self) -> dict:
        """
        Retrieve player information as a dictionary.

        Returns:
            dict: Player information.
        """
        info = {
            'name': self.name,
            'position': self.position,
            'skill_level': self.skill_level
        }
        info.update(self.additional)
        return info


class Team:
    """
    A class representing a team in the fantasy league.

    Attributes:
        name (str): Name of the team.
        players (List[Player]): List of players in the team.
    """

    def __init__(self, name: str, players: List['Player'] = None) -> None:
        """
        Initialize a team with a name and an optional list of players.

        Args:
            name (str): Name of the team.
            players (List[Player], optional): List of players in the team. Defaults to an empty list.
        """
        self.name = name
        self.players = players if players else []

    def add_player(self, player: 'Player') -> None:
        """
        Add a player to the team.

        Args:
            player (Player): The player to add.

        Raises:
            Exception: If the team exceeds 11 players or the player already exists.
        """
        if len(self.players) >= 11:
            raise Exception(f"Team {self.name} cannot have more than 11 players.")

        for existing_player in self.players:
            if existing_player.name.lower() == player.name.lower():
                raise Exception(f"Player {player.name} is already in the team (case-insensitive).")

        self.players.append(player)

    def remove_player(self, player: 'Player') -> None:
        """
        Remove a player from the team.

        Args:
            player (Player): The player to remove.

        Raises:
            Exception: If the player is not in the team.
        """
        if player in self.players:
            self.players.remove(player)
        else:
            raise Exception(f"Player {player.name} is not in the team.")

    def calculate_total_score(self, simulate: bool = False) -> float:
        """
        Calculate the total score of the team.

        Args:
            simulate (bool): Whether to simulate performance points.

        Returns:
            float: Average score of the team.
        """
        total_score = sum(
            player.generate_performance_points() if simulate else player.skill_level
            for player in self.players
        )

        return round(total_score / len(self.players), 2) if self.players else 0


class FantasyLeague:
    """
    A class representing a fantasy league consisting of multiple teams.

    Attributes:
        teams (List[Team]): List of teams in the league.
    """

    def __init__(self, teams: List['Team'] = None) -> None:
        """
        Initialize the fantasy league with a list of teams.

        Args:
            teams (List[Team], optional): List of teams. Defaults to an empty list.

        Raises:
            Exception: If teams have different numbers of players.
        """
        self.teams = teams if teams else []
        if self.teams:
            player_count = len(self.teams[0].players)
            if not all(len(team.players) == player_count for team in self.teams):
                raise Exception("All teams must have the same number of players.")

    def add_team(self, team: 'Team') -> None:
        """
        Add a team to the league.

        Args:
            team (Team): The team to add.

        Raises:
            Exception: If the team already exists or violates constraints.
        """
        if any(existing_team.name.lower() == team.name.lower() for existing_team in self.teams):
            raise Exception(f"Team {team.name} already exists in the league.")

        if len(team.players) == 0:
            raise Exception(f"Team {team.name} has no players.")

        self.teams.append(team)

    def calculate_team_rankings(self, simulate: bool = False) -> List[Tuple[str, float]]:
        """
        Calculate team rankings based on total scores.

        Args:
            simulate (bool): Whether to simulate performance points.

        Returns:
            List[Tuple[str, float]]: Sorted list of team rankings.

        Raises:
            Exception: If fewer than two teams exist in the league.
        """
        if len(self.teams) < 2:
            raise Exception("At least two teams are required to simulate a season.")

        team_scores = [
            (team.name, team.calculate_total_score(simulate)) for team in self.teams
        ]
        return sorted(team_scores, key=lambda x: (-x[1], x[0]))


class Trade:
    """
    A class representing a trade between two teams.

    Attributes:
        team1 (Team): The first team involved in the trade.
        team2 (Team): The second team involved in the trade.
        players_team1 (list[Player]): Players from team1 involved in the trade.
        players_team2 (list[Player]): Players from team2 involved in the trade.
    """

    def __init__(
        self,
        team1: Team,
        team2: Team,
        players_team1: list[Player],
        players_team2: list[Player],
    ) -> None:
        """
        Initialize a trade between two teams.

        Args:
            team1 (Team): First team involved.
            team2 (Team): Second team involved.
            players_team1 (list[Player]): Players from the first team.
            players_team2 (list[Player]): Players from the second team.
        """
        self.team1 = team1
        self.team2 = team2
        self.players_team1 = players_team1
        self.players_team2 = players_team2

    def propose_trade(self) -> bool:
        """
        Execute the trade if valid.

        Returns:
            bool: True if the trade is successful.

        Raises:
            Exception: If the trade is invalid or unfair.
        """
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
            self.team1.players.remove(player)
            self.team2.players.append(player)

        for player in self.players_team2:
            self.team2.players.remove(player)
            self.team1.players.append(player)

        return True
