from classes import player, game_master


_MASTER_: game_master.GameMaster = None
_INIT_ = False


def init(master: game_master.GameMaster):
    """
    Must be called before any other function is run (or they will all immediately return). Sets the game master
    :param master:
        The game master
    """
    global _MASTER_, _INIT_
    _MASTER_ = master
    _INIT_ = True


def year_of_plenty(card_player, resource):
    """
    Adds two of a selected resource to the player
    :param card_player: Player
    :param resource: str
    """
    resource = card_player.card_select_resource()
    card_player.resources[resource] += 2


def monopoly(card_player, resource):
    pool = 0
    for p in _MASTER_.turn_queue:
        # Skip the player who called the card
        if p == card_player:
            continue

        # Add to the resource pot
        pool += p.resources[resource]

        # Force this player to discard all of this resource
        p.resources[resource] = 0
    # Grant the original player all the resources pooled
    card_player.resources[resource] += pool


def play_card(card_player: player.Player, card: str):
    """
    Triggers a different sequence of actions depending on which card has been played

    :param card_player:
        The Player who originaly played this card
    :param card:
        The name of the card being played, by convention in 'Title Case'
    :return:
    """
    # Can only run if initialised
    if not _INIT_:
        return

    if card == "Monopoly":
        resource = card_player.card_select_resource()
        monopoly(card_player, resource)
    elif card == "Year of Plenty":
        resource = card_player.card_select_resource()
        year_of_plenty(card_player, resource)
