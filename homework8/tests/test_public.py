import random
from lab8 import FantasyLeague, Player, Team, Trade

# Mock random.randint to control randomness in tests
def mock_random():
    """
    Mock the random.randint function to always return the lower bound for predictability.
    """
    random.randint = lambda a, b: a

# Test Player initialization
def test_player_initialization():
    """
    Test the initialization of a Player object.
    """
    player = Player(name="Alice", position="Striker", skill_level=85)
    assert player.name == "Alice"
    assert player.position == "Striker"
    assert player.skill_level == 85

# Test Player initialization with invalid skill level
def test_player_invalid_skill_level():
    """
    Test Player initialization with skill levels out of bounds.
    """
    try:
        Player(name="Bob", position="Midfielder", skill_level=105)
    except ValueError:
        print("Skill level out of bounds correctly raised an exception.")

    try:
        Player(name="Charlie", position="Defender", skill_level=-5)
    except ValueError:
        print("Negative skill level correctly raised an exception.")

# Test generating performance points
def test_generate_performance_points():
    """
    Test the performance point generation for a Player.
    """
    mock_random()
    player = Player(name="Bob", position="Midfielder", skill_level=80)
    performance_points = player.generate_performance_points()
    print("Performance Points:", performance_points)

# Test updating skill level

def test_update_skill_level():
    """
    Test updating a Player's skill level.
    """
    player = Player(name="Charlie", position="Defender", skill_level=70)
    player.update_skill_level(10)
    assert player.skill_level == 80
    player.update_skill_level(-20)
    assert player.skill_level == 60

# Test skill level constraints
def test_skill_level_constraints():
    """
    Test that skill levels stay within the valid range (0-100).
    """
    player = Player(name="Eve", position="Striker", skill_level=10)
    player.update_skill_level(-15)
    assert player.skill_level == 0

    player = Player(name="Frank", position="Midfielder", skill_level=95)
    player.update_skill_level(10)
    assert player.skill_level == 100

# Test Team functionality
def test_team_operations():
    """
    Test adding, removing, and scoring players in a Team.
    """
    team = Team(name="Dream Team", players=[])
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)

    team.add_player(player1)
    assert player1 in team.players

    try:
        team.add_player(player1)  # Adding the same player again should raise an exception
    except Exception:
        print("Duplicate player correctly raised an exception.")

    team.add_player(player2)
    team.remove_player(player1)
    assert player1 not in team.players

# Test FantasyLeague functionality
def test_fantasy_league():
    """
    Test the FantasyLeague class with team and player operations.
    """
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    team1 = Team(name="Team Alpha", players=[player1])
    team2 = Team(name="Team Beta", players=[player2])

    league = FantasyLeague(teams=[team1, team2])
    assert len(league.teams) == 2

    new_team = Team(name="Team Gamma", players=[])
    league.add_team(new_team)
    assert len(league.teams) == 3

    try:
        league.add_team(new_team)  # Adding a duplicate team should raise an exception
    except Exception:
        print("Duplicate team correctly raised an exception.")

# Test Trades between Teams
def test_trades():
    """
    Test the Trade class for valid and invalid trades.
    """
    player1 = Player(name="Alice", position="Striker", skill_level=85)
    player2 = Player(name="Bob", position="Midfielder", skill_level=78)
    player3 = Player(name="Charlie", position="Defender", skill_level=82)

    team1 = Team(name="Team Alpha", players=[player1])
    team2 = Team(name="Team Beta", players=[player2, player3])

    trade = Trade(team1=team1, team2=team2, players_team1=[player1], players_team2=[player3])
    assert trade.propose_trade() is True

    try:
        invalid_trade = Trade(team1=team1, team2=team2, players_team1=[player2], players_team2=[player1])
        invalid_trade.propose_trade()
    except Exception:
        print("Invalid trade correctly raised an exception.")

# Run tests
test_player_initialization()
test_player_invalid_skill_level()
test_generate_performance_points()
test_update_skill_level()
test_skill_level_constraints()
test_team_operations()
test_fantasy_league()
test_trades()
