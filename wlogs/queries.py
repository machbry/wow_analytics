from .api import graphQL_client_from_json


CLIENT = graphQL_client_from_json()


def post_query(query_func):
    def query_arguments_wrapper(*args, **kwargs):
        return CLIENT.post(query_func(*args, **kwargs))
    return query_arguments_wrapper


@post_query
def query_item(id: int) -> str:
    query = "query {" +\
                "gameData{" +\
                    "item(id: " + str(id) + "){" +\
                        "id " +\
                        "name}}}"
    return query


@post_query
def query_game_zones_on_page(page: int) -> str:
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
    return query


@post_query
def query_game_specs(zone_id: int) -> str:
    query = "query {" +\
                "gameData{" +\
                    "classes(zone_id: " + str(zone_id) + "){" +\
                        "id " +\
                        "name " +\
                        "specs{" +\
                            "id " +\
                            "name }}}}"
    return query


@post_query
def query_reports_on_page(guild_id: int, page: int) -> str:
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
                            "segments " +\
                            "guild{" +\
                                "id }}}}}"
    return query


@post_query
def query_report(code: str, actor_type="Player") -> str:
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
    return query
