#!/bin/bash
cd "$(dirname "$0")"

#check if the virtual environment exists and, if not, creates one
if [ ! -d "/venv" ]; then    
    python3 -m venv venv    
fi

#Activate virtual environment
source venv/bin/activate

#Install dependencies from requirements.txt
pip install -r requirements.txt

#Run Scraper
python3 ex1.py generated 40 > generated/report_$(date +%Y-%m-%d).txt

deactivate
