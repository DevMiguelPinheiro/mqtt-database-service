# MQTT to MySQL Service

## Overview
This project is a Python-based service that connects to an MQTT broker, listens for temperature readings on a specific topic, and stores these readings in a MySQL database. The implementation follows best practices using dependency injection for modularity and scalability.

---

## Features
- Connects to an MQTT broker to subscribe to a specific topic.
- Listens for incoming messages and parses temperature data.
- Inserts the temperature data into a MySQL database with a timestamp.
- Implements dependency injection using the `dependency-injector` library for better modularity and testability.

---

## Project Structure

```
mqtt_mysql_service/
├── __init__.py
├── config.py          # Configuration for MQTT and MySQL
├── containers.py      # Dependency injection container
├── database.py        # MySQL database service
├── mqtt_client.py     # MQTT client service
└── main.py            # Entry point for the application
```

---

## Requirements

- Python 3.8+
- MySQL database

### Python Libraries
Install the required libraries using pip:

```bash
pip install paho-mqtt mysql-connector-python dependency-injector
```

---

## Setup

### MySQL Configuration
Create a database and table to store the temperature readings:

```sql
CREATE DATABASE temperature_db;

USE temperature_db;

CREATE TABLE temperature_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Configuration
Update the `config.py` file with your MQTT broker and MySQL database details:

```python
class Config:
    # MQTT Configuration
    BROKER_URL = "your_broker_url"
    BROKER_PORT = 1883
    MQTT_TOPIC = "sensor/temperature"

    # MySQL Configuration
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "your_password"
    DB_NAME = "temperature_db"
```

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/mqtt-mysql-service.git
   cd mqtt-mysql-service
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the service:

   ```bash
   python main.py
   ```

---

## Testing

### MQTT Messages
You can use a tool like `mosquitto_pub` to publish messages to the MQTT topic:

```bash
mosquitto_pub -h your_broker_url -t sensor/temperature -m "25.5"
```

### Verifying Data in MySQL
Check the data in the MySQL table:

```sql
SELECT * FROM temperature_readings;
```

---

## Technologies Used
- **Python**: Core programming language
- **Paho-MQTT**: MQTT client library
- **MySQL**: Database for storing temperature readings
- **Dependency Injector**: Library for managing dependency injection

---

## Future Improvements
- Add error handling for unstable network or broker issues.
- Implement retries for database connection failures.
- Extend support for multiple topics and sensors.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributions
Feel free to fork the repository and submit pull requests for new features or improvements. For major changes, please open an issue first to discuss what you would like to change.

