website=$1

if curl -s --head  --request GET $website | grep "200 OK" > /dev/null; then 
   sqlite3 db/info.db "UPDATE Monitors SET Status='Up' WHERE Link='$1';"
else
    sqlite3 db/info.db "UPDATE Monitors SET Status='Down' WHERE Link='$1';"
fi