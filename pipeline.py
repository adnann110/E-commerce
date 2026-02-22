import logging
import json

# Configure logging
def configure_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

# Validate data
def validate_data(data):
    if not isinstance(data, dict):
        logging.error("Data must be a dictionary.")
        return False
    # Add more validation logic as needed
    return True

# Process order

def process_order(data):
    logging.info("Processing order...")
    try:
        if not validate_data(data):
            raise ValueError("Invalid data provided.")
        order_id = data.get('order_id')
        items = data.get('items')
        if not items:
            raise ValueError("No items to process.")

        # Processing logic here
        logging.info(f"Order ID: {order_id} processed successfully with items: {items}")
        return True
    except Exception as e:
        logging.error(f"Error processing order: {e}")
        return False

# Main function
def main():
    configure_logging()
    sample_order = {
        'order_id': 12345,
        'items': [{'item_id': 1, 'quantity': 2}, {'item_id': 2, 'quantity': 1}]
    }
    success = process_order(sample_order)
    if success:
        logging.info("Order processed successfully.")
    else:
        logging.info("Order processing failed.")

if __name__ == '__main__':
    main()