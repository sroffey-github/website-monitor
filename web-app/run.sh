clear
echo "[+] Building Docker Image..."
docker build -t website-monitor .

echo ""
echo "[+] Running Docker Container..."
docker run -dp 5000:5000 -v /home/pi/web-apps/website-monitor/db:/app/db website-monitor

echo ""
echo "*/5 * * * * /home/pi/web-apps/website-monitor/sh/run.sh" | tee -a /var/spool/cron/root