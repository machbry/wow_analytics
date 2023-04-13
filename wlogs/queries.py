from .api import graphQL_client_from_json


CLIENT = graphQL_client_from_json()


def query_item(id: int, client=CLIENT) -> dict:
    query = "query {" +\
                "gameData{" +\
                    "item(id: " + str(id) + "){" +\
                        "id " +\
                        "name}}}"
    return client.post(query)


def query_game_zones_on_page(page: int, client=CLIENT) -> dict:
    query = "query {" +\
                "gameData{" +\
                    "zones(page: " + str(page) + "){" +\
                        "total " +\
                        "per_page " +\
                        "current_page " +\
                        "from " +\
                        "to " +\
                        "last_page " +\
                        "has_more_pages " +\
                        "data{" +\
                            "id " +\
                            "name }}}}"
    return client.post(query)


def query_game_specs(zone_id: int, client=CLIENT) -> dict:
    query = "query {" +\
                "gameData{" +\
                    "classes(zone_id: " + str(zone_id) + "){" +\
                        "id " +\
                        "name " +\
                        "specs{" +\
                            "id " +\
                            "name }}}}"
    return client.post(query)


def query_reports_on_page(guild_id: int, page: int, client=CLIENT) -> dict:
    query = "query " +\
                "{reportData " +\
                    "{reports(guildID: " + str(guild_id) + ", page: " + str(page) + "){" +\
                        "total " +\
                        "per_page " +\
                        "current_page " +\
                        "from " +\
                        "to " +\
                        "last_page " +\
                        "has_more_pages " +\
                        "data{" +\
                            "code " +\
                            "title " +\
                            "startTime " +\
                            "endTime " +\
                            "segments}}}}"
    return client.post(query)


def query_report(code: str, actor_type="Player", client=CLIENT) -> dict:
    query = "query " +\
                "{reportData " +\
                    "{report(code: " + "\"" + code + "\"" + "){" +\
                        "code " +\
                        "title " +\
                        "startTime " +\
                        "endTime " +\
                        "masterData {actors(type:" + "\"" + actor_type + "\"" + "){" +\
                            "id " +\
                            "name " +\
                            "type " +\
                            "subType}}" +\
                        "fights {" +\
                            "id " +\
                            "name " +\
                            "difficulty " +\
                            "encounterID " +\
                            "size " +\
                            "hardModeLevel " +\
                            "startTime " +\
                            "endTime " +\
                            "kill " +\
                            "bossPercentage " +\
                            "lastPhase " +\
                            "averageItemLevel}}}}"
    return client.post(query)
