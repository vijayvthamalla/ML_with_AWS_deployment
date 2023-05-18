import logging
import os
from datetime import datetime

File_name = f"{datetime.now().strftime('%m_%d_%Y_%H')}.log"

logs_path = os.path.join(os.getcwd(),"logs",f"{datetime.now().strftime('%m_%d_%Y')}")
os.makedirs(logs_path, exist_ok=True)

Log_File_path = os.path.join(logs_path,File_name)

logging.basicConfig(
    filename=Log_File_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("Logging is started")