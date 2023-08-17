#! /bin/bash

env_file=".env"
root_dir=$(pwd)
guild_id=$1
default_zone_id=$2

if [ -f $env_file ];
then
  rm $env_file
fi

{
  echo "WA_ROOT_DIR=$root_dir"
  echo "GUILD_ID=$guild_id"
  echo "DEFAULT_ZONE_ID=$default_zone_id"
} >> $env_file
