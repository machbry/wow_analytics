def query_reports_on_page(guild_id, page) -> str:
    query = "query {reportData {reports(guildID: "+str(guild_id)+", page: "+str(page)+")\
     {total per_page current_page from to last_page has_more_pages data{code title startTime endTime segments}}}}"
    return query


def query_report(code, actor_type="Player"):
    query = "query {reportData {report(code: "+"\""+code+"\""+") {code title startTime endTime masterData \
    {actors(type:"+"\""+actor_type+"\""+") {id name type subType}} \
    fights {id name difficulty encounterID size startTime endTime kill bossPercentage lastPhase averageItemLevel}}}}"
    return query
