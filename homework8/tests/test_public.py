import random

import pytest
from lab8 import FantasyLeague, Player, Team, Trade


# Mock random.randint to control randomness in tests
@pytest.fixture(autouse=True)
def mock_random(monkeypatch):
    def mock_randint(a, b):
        return a  # Always return the lower bound for predictability

    monkeypatch.setattr(random, "randint", mock_randint)


def test_player_initialization():
    player = Player(name="Alice", position="Striker", skill_level=85)
    assert player.name == "Alice"
    assert player.position == "Striker"
    assert player.skill_level == 85


def test_player_initialization_with_skill_level_out_of_bounds():
    with pytest.raises(ValueError):
        Player(name="Bob", position="Midfielder", skill_level=105)
    with pytest.raises(ValueError):
        Player(name="Charlie", position="Defender", skill_level=-5)


def test_generate_performance_points():
    player = Player(name="Bob", position="Midfielder", skill_level=80)
    performance_points = player.generate_performance_points()
    assert performance_points == 75  # Mocked to always return skill_level - 5


def test_update_skill_level_increase():
    player = Player(name="Charlie", position="Defender", skill_level=70)
    player.update_skill_level(10)
    assert player.skill_level == 80


def test_update_skill_level_decrease():
    player = Player(name="David", position="Goalkeeper", skill_level=60)
    player.update_skill_level(-20)
    assert player.skill_level == 40


def test_update_skill_level_below_zero():
    player = Player(name="Eve", position="Striker", skill_level=10)
    player.update_skill_level(-15)
    assert player.skill_level == 0


def test_update_skill_level_above_hundred():
    player = Player(name="Frank", position="Midfielder", skill_level=95)
    player.update_skill_level(10)
    assert player.skill_level == 100


def test_player_creation_with_kwargs():
    player_data = {"name": "Alice", "position": "Striker", "skill_level": 85, "extra": "Extra data"}
    player = Player(**player_data)
    assert player.name == "Alice"
    assert player.position == "Striker"
    assert player.skill_level == 85
    assert player.extra == "Extra data"


def test_player_equality():
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    assert player1.get_player_info() == {
        "name": "Alice",
        "position": "Striker",
        "skill_level": 85,
    }
    player2 = Player(name="Afroin Malice", position="Keeper", skill_level=85, age=29, height=180)
    assert player2.get_player_info() == {
        "name": "Afroin Malice",
        "position": "Keeper",
        "skill_level": 85,
        "age": 29,
        "height": 180,
    }


def test_team_initialization():
    team = Team(name="Dream Team", players=[])
    assert team.name == "Dream Team"
    assert len(team.players) == 0


def test_add_player():
    player = Player(name="Alice", position="Striker", skill_level=85)
    team = Team(name="Dream Team", players=[])
    team.add_player(player)
    assert player in team.players
    assert len(team.players) == 1


def test_add_duplicate_player():
    player = Player(name="Alice", position="Striker", skill_level=85)
    team = Team(name="Dream Team", players=[player])

    with pytest.raises(Exception):
        team.add_player(player)


def test_add_player_exceeds_limit():
    players = [Player(name=f"Player{i}", position="Position", skill_level=80) for i in range(11)]
    team = Team(name="Dream Team", players=players)

    new_player = Player(name="Bob", position="Midfielder", skill_level=78)

    with pytest.raises(Exception):
        team.add_player(new_player)


def test_remove_player():
    player = Player(name="Alice", position="Striker", skill_level=85)
    team = Team(name="Dream Team", players=[player])
    team.remove_player(player)
    assert player not in team.players
    assert len(team.players) == 0


def test_calculate_total_score():
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    player3 = Player(name="Adam", position="Defender", skill_level=91)

    # Mock performance points to control randomness
    player1.generate_performance_points = lambda: 80
    player2.generate_performance_points = lambda: 75
    player3.generate_performance_points = lambda: 86

    team = Team(name="Dream Team", players=[player1, player2, player3])

    total_score = team.calculate_total_score(simulate=False)
    simulated_score = team.calculate_total_score(simulate=True)

    # Expected score is the sum of standard skill points
    assert pytest.approx(total_score, abs=3e-2) == 84.66
    # Expected score is the sum of simulated performance points
    assert pytest.approx(simulated_score, abs=3e-2) == 80.34


def test_fantasy_league_initialization():
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    team1 = Team(name="Team Alpha", players=[player1])
    team2 = Team(name="Team Beta", players=[player2])
    league = FantasyLeague(teams=[team1, team2])

    assert len(league.teams) == 2
    assert league.teams[0].name == "Team Alpha"
    assert league.teams[1].name == "Team Beta"


def test_add_team_to_league():
    player = Player(name="Alice", position="Striker", skill_level=85)
    team1 = Team(name="Team Alpha", players=[player])
    league = FantasyLeague(teams=[team1])

    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    team2 = Team(name="Team Beta", players=[player2])
    league.add_team(team2)

    assert len(league.teams) == 2
    assert league.teams[1].name == "Team Beta"


def test_add_duplicate_team_to_league():
    player = Player(name="Alice", position="Striker", skill_level=85)
    team1 = Team(name="Team Alpha", players=[player])
    league = FantasyLeague(teams=[team1])

    duplicate_team = Team(name="Team Alpha", players=[player])

    with pytest.raises(Exception):
        league.add_team(duplicate_team)


def test_calculate_team_rankings():
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)

    team1 = Team(name="Team Alpha", players=[player1])
    team2 = Team(name="Team Beta", players=[player2])

    # Mock performance points to control randomness
    player1.generate_performance_points = lambda: 80
    player2.generate_performance_points = lambda: 75

    league = FantasyLeague(teams=[team1, team2])

    rankings = league.calculate_team_rankings(simulate=True)

    assert rankings == [("Team Alpha", 80), ("Team Beta", 75)]


def test_calculate_team_rankings_invalid_num_teams():
    players_team1 = [
        Player(name="Alice", position="Striker", skill_level=85),
        Player(name="Bob", position="Midfielder", skill_level=78),
        Player(name="Charlie", position="Defender", skill_level=82),
    ]

    team1 = Team(name="Team Alpha", players=players_team1)

    league = FantasyLeague(teams=[team1])

    with pytest.raises(Exception):
        league.calculate_team_rankings(simulate=False)


def test_calculate_team_rankings_with_insufficient_teams():
    player = Player(name="Alice", position="Striker", skill_level=85)
    team1 = Team(name="Team Alpha", players=[player])
    league = FantasyLeague(teams=[team1])

    with pytest.raises(Exception):
        league.calculate_team_rankings()


def test_add_valid_team():
    player = Player(name="Alice", position="Striker", skill_level=85)
    valid_team = Team(name="Valid Team", players=[player])
    league = FantasyLeague()

    league.add_team(valid_team)

    assert len(league.teams) == 1
    assert league.teams[0].name == "Valid Team"


def test_add_team_with_zero_players():
    empty_team = Team(name="Empty Team", players=[])
    league = FantasyLeague()

    with pytest.raises(Exception):
        league.add_team(empty_team)


def test_add_more_than_ten_teams():
    # Create 10 valid teams
    teams = [
        Team(name=f"Team {i}", players=[Player(name=f"Player{i}", position="Position", skill_level=80)])
        for i in range(10)
    ]

    league = FantasyLeague(teams=teams)

    # Attempt to add an 11th team
    extra_player = Player(name="Extra Player", position="Midfielder", skill_level=70)
    extra_team = Team(name="Extra Team", players=[extra_player])

    with pytest.raises(Exception):
        league.add_team(extra_team)


def test_calculate_team_rankings_before_and_after_simulation():
    # Create players for each team
    players_team1 = [
        Player(name="Alice", position="Striker", skill_level=85),
        Player(name="Bob", position="Midfielder", skill_level=78),
        Player(name="Charlie", position="Defender", skill_level=82),
    ]

    players_team2 = [
        Player(name="David", position="Goalkeeper", skill_level=90),
        Player(name="Eve", position="Striker", skill_level=88),
        Player(name="Frank", position="Midfielder", skill_level=75),
    ]

    players_team3 = [
        Player(name="Grace", position="Defender", skill_level=80),
        Player(name="Heidi", position="Midfielder", skill_level=77),
        Player(name="Ivan", position="Striker", skill_level=83),
    ]

    players_team4 = [
        Player(name="Karl", position="Midfielder", skill_level=79),
        Player(name="Liam", position="Striker", skill_level=84),
        Player(name="Mona", position="Defender", skill_level=81),
    ]

    # Create teams
    team1 = Team(name="Team Alpha", players=players_team1)
    team2 = Team(name="Team Beta", players=players_team2)
    team3 = Team(name="Team Gamma", players=players_team3)
    team4 = Team(name="Team Delta", players=players_team4)

    # Create league and add teams
    league = FantasyLeague(teams=[team1, team2, team3, team4])

    # Calculate rankings before simulation (using skill levels)
    rankings_before_simulation = league.calculate_team_rankings(simulate=False)

    assert pytest.approx(rankings_before_simulation, abs=2e-2) == [
        ("Team Beta", 84.33),
        ("Team Alpha", 81.67),
        ("Team Delta", 81.33),
        ("Team Gamma", 80.0),
    ]

    # Calculate rankings after simulation (using performance scores)
    rankings_after_simulation = league.calculate_team_rankings(simulate=True)

    assert pytest.approx(rankings_after_simulation, abs=2e-2) == [
        ("Team Beta", 79.33),
        ("Team Alpha", 76.67),
        ("Team Delta", 76.33),
        ("Team Gamma", 75.0),
    ]


def test_valid_trade():
    # Create players
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    player3 = Player(name="Charlie", position="Defender", skill_level=82)
    player4 = Player(name="David", position="Goalkeeper", skill_level=90)

    # Create teams
    team1 = Team(name="Team Alpha", players=[player1, player2])
    team2 = Team(name="Team Beta", players=[player3, player4])

    # Create a valid trade
    trade = Trade(team1=team1, team2=team2, players_team1=[player1], players_team2=[player3])

    # Execute the trade and assert it succeeds
    assert trade.propose_trade() is True


def test_invalid_trade_player_not_in_team():
    # Create players
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    player3 = Player(name="Charlie", position="Defender", skill_level=82)

    # Create teams
    team1 = Team(name="Team Alpha", players=[player1])
    team2 = Team(name="Team Beta", players=[player2])

    # Attempt to trade a player not in the team
    trade = Trade(team1=team1, team2=team2, players_team1=[player3], players_team2=[player2])

    with pytest.raises(Exception):
        trade.propose_trade()


def test_unfair_trade_due_to_skill_difference():
    # Create players
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player3 = Player(name="Charlie", position="Defender", skill_level=60)

    # Create teams
    team1 = Team(name="Team Alpha", players=[player1])
    team2 = Team(name="Team Beta", players=[player3])

    # Attempt an unfair trade due to skill level difference
    trade = Trade(team1=team1, team2=team2, players_team1=[player1], players_team2=[player3])

    with pytest.raises(Exception):
        trade.propose_trade()
