import sys
import logging
from src import logger

def error_message_detail(error:str, error_detail:sys)->str:
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in {file_name}, line number {exec_tb.tb_lineno} and Error Message is {error}"
    return error_message

class CustomException(Exception):

    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self) -> str:
        return self.error_message
    
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Zero Division Error")
        raise CustomException(e,sys)
