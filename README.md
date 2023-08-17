# wow_analytics
Analytics based on warcraft logs data.

## Initial setup
1. Install wlogs package on your environment : pip install .
2. Run init_wlogs.sh <guild_id> <default_zone_id> (create an .env file)
   - ex : guild_id = 505778 (Rush N Wipe Again) & default_zone_id = 603 (WOTLK)
   - those IDs are taken from www.warcraftlogs.com
3. Create a V2 client at https://www.warcraftlogs.com/api/clients/ 
4. Save clients credentials into client_credentials.json in the root directory :
    >{ \
        "_client_id": "<client_id>", \
        "_client_secret": "<client_secret>", \
        "_authorize_url": "<redirect_url>" \
    }
5. Save PostgreSQL credentials into postgresql_credentials.json in the root directory :
    >{ \
        "username": "<db_username>", \
        "password": "<db_password>", \
        "host": "<db_host>", \
        "port": <db_port>, \
        "database": "<database_name>" \
    }
6. Have fun !
