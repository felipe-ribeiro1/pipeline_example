import logging
import sys

# Configure the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Remove all existing handlers
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

# Create a StreamHandler to output logs to the console
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)

# Define a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
stream_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(stream_handler)

# Example functions
def extract_data():
    logger.info("Extracting data...")
    return [1, 2, 3]

def transform_data(data):
    logger.info("Transforming data...")
    return [x ** 2 for x in data]

def load_data(data):
    logger.info(f"Loading data: {data}")

def main():
    logger.info("Pipeline started")
    data = extract_data()
    transformed = transform_data(data)
    load_data(transformed)
    logger.info("Pipeline completed")

if __name__ == "__main__":
    main()
