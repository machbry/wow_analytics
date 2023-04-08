from .api import graphQL_client_from_json


CLIENT = graphQL_client_from_json()


def query_reports_on_page(guild_id, page, client=CLIENT) -> str:
    query = "query {reportData {reports(guildID: "+str(guild_id)+", page: "+str(page)+")\
     {total per_page current_page from to last_page has_more_pages data{code title startTime endTime segments}}}}"
    return client.post(query)


def query_report(code, actor_type="Player", client=CLIENT):
    query = "query {reportData {report(code: "+"\""+code+"\""+") {code title startTime endTime masterData \
    {actors(type:"+"\""+actor_type+"\""+") {id name type subType}} \
    fights {id name difficulty encounterID size hardModeLevel startTime endTime kill bossPercentage lastPhase \
    averageItemLevel}}}}"
    return client.post(query)
