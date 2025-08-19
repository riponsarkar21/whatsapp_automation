# whatsapp_automation
# 📦 WhatsApp Production Report Sender

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Twilio](https://img.shields.io/badge/Twilio-WhatsApp-green.svg)](https://www.twilio.com/whatsapp)

This Python script reads a production value from an Excel file and sends it via WhatsApp using the Twilio API. Ideal for automated production reporting or daily notifications.

---

## 🔹 Features

- Reads a specific cell from an Excel sheet (`.xlsx`) using `openpyxl`.
- Sends WhatsApp messages via **Twilio API**.
- Supports **sandbox testing** with Twilio WhatsApp.
- Optional 10-second delay before sending messages.
- Can be extended to multiple recipients or automated schedules.

---

## 🛠 Prerequisites

- Python 3.8+
- Twilio account with WhatsApp sandbox setup
- Python libraries:
  ```bash
  pip install twilio openpyxl
⚙️ Setup
Clone the repository

bash
Copy
Edit
git clone <your-repo-url>
cd <repo-folder>
Twilio Sandbox

Open WhatsApp and send the join keyword to the sandbox number:

bash
Copy
Edit
join them-rice
Example: +14155238886

You should receive a confirmation message from Twilio.

Update Twilio credentials in the script:

python
Copy
Edit
account_sid = '<YOUR_ACCOUNT_SID>'
auth_token = '<YOUR_AUTH_TOKEN>'
Set recipient number (must have joined sandbox):

python
Copy
Edit
recipient_number = '+8801766695428'
Configure Excel file path and cell:

python
Copy
Edit
file_path = r"F:\Packing\Packing All Backup\Ripon\Production Report\Yearly Summary & Run Time 2021.xlsx"
sheet_name = "Production"
cell_address = "K154"
▶️ Usage
Run the script:

bash
Copy
Edit
python main.py
Reads the value from the Excel cell.

Waits 10 seconds.

Sends a WhatsApp message with the production value.

Example message:

csharp
Copy
Edit
The monthly production is 77327.7 MT
⚠️ Notes
Sandbox only allows messages to numbers that joined using the keyword.

Free-form messages (body=) require a 24-hour window after the recipient last messaged the sandbox.
→ For fully automated messages outside this window, use WhatsApp templates (content_sid).

Multiple recipients must each join the sandbox separately.

🖼 Screenshot
You can add a screenshot of the script output in VSCode or WhatsApp message here for better clarity.

📄 License
MIT License

🔗 References
Twilio WhatsApp Sandbox

openpyxl Documentation

Twilio Python SDK
