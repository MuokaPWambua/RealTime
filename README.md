# RealTime
This is a script that fetches market data in real time from yahoo finance, deserialize it and write it to excel file in real time

## How To Run
You will need a virtual environment to create one run

  `python -m venv virtual`
  
Activate the created virtual environment

  `source virtual/bin/activate` or `virtual/Scripts/activate`
  
Install requirements

  `pip install -r requirements.txt`
  
Run script

  `python app.py`

*Note  
You will have to be connected to the internet.
Once the script starts running a directory named NSE will be created in your home directory
containing example.xlsx file which you will open with microsoft excel to see live updates
