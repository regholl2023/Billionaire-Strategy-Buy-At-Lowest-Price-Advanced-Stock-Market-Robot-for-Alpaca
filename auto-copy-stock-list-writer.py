import shutil
import time
import os
from datetime import datetime, timedelta
import pytz

def get_current_time():
    # Get the current time in Eastern Time (ET)
    et_timezone = pytz.timezone('US/Eastern')
    current_time = datetime.now(et_timezone)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z")

def copy_stock_symbols(source_file, destination_file):
    try:
        # Delete the destination file before copying
        if os.path.exists(destination_file):
            os.remove(destination_file)
        
        shutil.copyfile(source_file, destination_file)
        print("Stock symbols copied successfully.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    source_file = "list-of-stock-symbols-to-scan.txt"
    destination_file = "electricity-or-utility-stocks-to-buy-list.txt"
    
    while True:
        current_time = get_current_time()
        print("Current Eastern Time:", current_time)
        
        copy_stock_symbols(source_file, destination_file)
        
        next_runtime = datetime.now() + timedelta(seconds=30)
        print("Next runtime in 30 seconds.")
        
        time.sleep(30)
