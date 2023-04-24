from classes import player, game_master


_MASTER_: game_master.GameMaster =  None
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


def play_card(card_player: player.Player, card: str):
    # Can only run if initialised
    if not _INIT_:
        return

    match card:
        case "Monopoly":
            resource = card_player.monopoly_select_resource()
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
            return