#!/bin/sh
if [ -z $arg ] ; then
echo "Please use '-h' to see avialable commands."
fi
while getopts "fbhsrdu" arg; do
    case $arg in
        f) # Build and run detached docker-compose
            docker-compose up --build 
        ;;
        b) # Build docker-compose.
            docker-compose build
        ;;
        u) # Start docker-compose.
            docker-compose up
        ;;
        s) # Stop docker-compose if running
            docker-compose down
        ;;
        r) # Restart docker-compose
            docker-compose down && docker-compose up
        ;;
        d) # Run docker-compose without terminal output
            docker-compose up --detach
        ;;  
        h) # Help.
            echo "$0 usage:" && grep " .)\ #" $0; exit 0;
        ;;
    esac
done    
