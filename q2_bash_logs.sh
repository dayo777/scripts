#!/usr/bin/env bash


LOG_URL="https://coderbyte.com/api/challenges/logs/web-logs-raw"
log_data=$(curl -s "$LOG_URL")

while IFS= read -r line; do
    # check if the line contains 'coderbyte heroku/router'
    if [[ "$line" == *"coderbyte heroku/router"* ]]; then
        # extract the request_id
        request_id=$(echo "$line" | grep -oP '(?<=request_id=)[^ ]+')
        # extract the fwd value
        fwd=$(echo "$line" | grep -oP '(?<=fwd=")[^"]+')
        echo "$request_id"
        # check if fwd is MASKED
        if [[ "$fwd" == "MASKED" ]]; then
            echo -n " [M]"
        else
            echo -n " [$fwd]"
        fi
        echo ""  # new line
    fi
done <<< "$log_data"