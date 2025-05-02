import logging
import os

def get_log_filename(base_name="output", extension=".log"):
    """
    Generate a unique log filename. If the base file exists, increment the filename.
    """
    counter = 0
    while True:
        filename = f"{base_name}{'' if counter == 0 else f'_{counter}'}{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1

def setup_logger():
    """
    Set up the logger to write to a unique log file.
    """
    log_filename = get_log_filename()
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return log_filename

def log_messages():
    """
    Logs several messages using the logging library.
    """
    logging.info("Log Entry 1: Script started.")
    logging.info("Log Entry 2: Performing some operations.")
    logging.info("Log Entry 3: Operations completed successfully.")
    logging.info("Log Entry 4: Script ended.")

if __name__ == "__main__":
    log_file = setup_logger()
    log_messages()
    print(f"Logs have been written to {log_file}")