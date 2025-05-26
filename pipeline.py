import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

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
