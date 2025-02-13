from psycopg2 import sql
from dev.utils.DataframeToJson import dataFrameToJson
from dev.config.config import base_executor

class InternsInfoService():
    ## get 
    def getInternsDetails():
        query = sql.SQL("""
                        select * 
                        from interns_schema.interns_details
                        """)
        dataframe, message = base_executor.executeSelect(query=query,values=(),get_as_packet=True)
        if dataframe is None or dataframe.empty:
            return 500, {"error":"no record found"}
        response_data = dataFrameToJson(dataframe)
        return 200, response_data
        
        