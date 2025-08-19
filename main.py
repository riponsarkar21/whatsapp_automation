from twilio.rest import Client
import time
from openpyxl import load_workbook
import config  # Import credentials and recipient numbers

# Initialize Twilio client
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

# Excel file details
file_path = r"F:\Packing\Packing All Backup\Ripon\Production Report\Yearly Summary & Run Time 2021.xlsx"
sheet_name = "Production"
cell_address = "K154"

def get_cell_value(file_path, sheet_name, cell_address):
    try:
        workbook = load_workbook(file_path, data_only=True)
        sheet = workbook[sheet_name]
        return sheet[cell_address].value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Fetch the value
value = get_cell_value(file_path, sheet_name, cell_address)

if value is not None:
    print(f"The value in cell {cell_address} is: {value}")
else:
    print("Could not retrieve the cell value.")

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_=config.TWILIO_WHATSAPP_NUMBER,
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Message details
message_body = f'The monthly production is {value} MT (Metric Ton)'

# Delay 10 seconds before sending
print("Waiting for 10 seconds before sending the message...")
time.sleep(10)

# Send the message to recipient from config
send_whatsapp_message(config.RECIPIENT_NUMBER, message_body)
