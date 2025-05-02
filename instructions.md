# Discord Bot

This project is a Discord bot written in Python that connects to a MySQL database. It is designed to be hosted on Railway.com.

## Features

- Connects to a MySQL database for data storage and retrieval.
- Implements various commands that can be executed within Discord.
- Utilizes environment variables for sensitive information.

## Project Structure

```
discord-bot
├── bot
│   ├── __init__.py
│   ├── main.py
│   ├── commands
│   │   └── __init__.py
│   └── utils
│       └── database.py
├── requirements.txt
├── config.py
├── README.md
└── .env
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd discord-bot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your Discord bot token and MySQL database credentials:
   ```
   DISCORD_TOKEN=your_discord_token
   DB_HOST=your_database_host
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_NAME=your_database_name
   ```

5. **Run the bot:**
   ```
   python bot/main.py
   ```

## Usage

Once the bot is running, you can interact with it in your Discord server. Use the commands defined in the `bot/commands` directory.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.