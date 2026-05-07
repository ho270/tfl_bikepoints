# pylint: skip-file

#imports
import os
import datetime
import logging

#Function
def setup_logging(log_dir):
    """
    This function sets up the logging for all modules. Means we repeat ourselves less. 

    Args:
        log_dir (string): the file path that you want the log files to be saved to.
    """

    os.makedirs(log_dir,exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_filename = os.path.join(f'{log_dir},{timestamp}.log')

    logging.basicConfig(
        filename=log_filename,
        format='%(asctime)s - %(names)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    return logging.getLogger('Main')