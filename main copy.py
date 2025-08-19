from twilio.rest import Client
import time

# Twilio credentials
account_sid = 'AC46c8025107d3bd22a8edd8a6ab317029'
auth_token = 'eae6ffcef985f7089fa0b25d9b0b4104'

# Initialize Twilio client
client = Client(account_sid, auth_token)

from openpyxl import load_workbook

# File path and sheet details
file_path = r"F:\Packing\Packing All Backup\Ripon\Production Report\Yearly Summary & Run Time 2021.xlsx"
sheet_name = "Production"
cell_address = "K154"

def get_cell_value(file_path, sheet_name, cell_address):
    try:
        # Load the workbook
        workbook = load_workbook(file_path, data_only=True)
        # Get the specified sheet
        sheet = workbook[sheet_name]
        # Get the value of the specified cell
        cell_value = sheet[cell_address].value
        return cell_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Fetch the value
value = get_cell_value(file_path, sheet_name, cell_address)

# Print the result
if value is not None:
    print(f"The value in cell {cell_address} is: {value}")
else:
    print("Could not retrieve the cell value.")



def send_whatsapp_message(recipient_number, message_body):
    try:
        # Send the WhatsApp message
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Replace with your Twilio sandbox or approved WhatsApp number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Parameters
recipient_number = '+8801928078420'
# recipient_number = '+8801766695428'
message_body = f'The monthly production is {value} MT'

# Delay for 10 seconds
print("Waiting for 10 seconds before sending the message...")
time.sleep(10)

# Send the message
send_whatsapp_message(recipient_number, message_body)
