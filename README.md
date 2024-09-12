# User Authentication System

## Video Demo:  
[![Watch the video](https://img.youtube.com/vi/ViZ9dB15JVs/hqdefault.jpg)](https://youtu.be/ViZ9dB15JVs)


## Description

This project was created as part of the selection round for the Newton School of Coding Club at SRM University. I have created a GUI-based application built using Python, Tkinter, and ttkbootstrap. The system supports user registration, login, and logout functionalities, with password management using SHA-256 hashing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Author](#author)
- [Contact](#contact)

## Features

- **User Registration**: Allows users to register with a username and password. Passwords are hashed using SHA-256.
- **User Login**: Users can log in using their registered credentials. Login success and error messages are displayed via pop-up alerts.
- **User Logout**: Users can log out, and their session will be terminated.
- **Data Storage**: User credentials are stored in a CSV file (`usrs.csv`).


## Installation

1. Clone the repository:
    ```
    git clone https://github.com/kevgon8/user-authentication-system.git
    ```

2. Navigate into the project directory:
    ```
    cd user-authentication-system
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

To run the User Authentication System:
```
python auth_system.py
```

## Screenshots
![Screenshot 2024-09-12 021555](https://github.com/user-attachments/assets/7826e91b-8791-4960-9ba3-655a3caa221d)


![Screenshot 2024-09-12 021632](https://github.com/user-attachments/assets/38b3c2b0-9df2-4e28-bae0-9ba5eb9aac71)


![Screenshot 2024-09-12 021649](https://github.com/user-attachments/assets/05e7b2a3-b2d7-41c2-b592-7753e4c25d75)


![Screenshot 2024-09-12 021809](https://github.com/user-attachments/assets/dbb547be-a148-46e3-b820-4dadeafe7cfc)


![Screenshot 2024-09-12 021834](https://github.com/user-attachments/assets/066cba3c-4378-42cc-89d4-2e06f0a4532e)


![Screenshot 2024-09-12 021955](https://github.com/user-attachments/assets/3487ccb8-2d0f-475b-be57-5e451ea15b4e)


![Screenshot 2024-09-12 022024](https://github.com/user-attachments/assets/7ac39dde-0b1e-4737-ab22-74b22513dae5)


![Screenshot 2024-09-12 022103](https://github.com/user-attachments/assets/32ed2ea8-1d2f-47d6-9c6b-89a038c31296)


![Screenshot 2024-09-12 022125](https://github.com/user-attachments/assets/d5c197a9-824f-475e-8f24-1949754ba623)




## Features in the GUI
1. **Login**: Enter your username and password, then click "LOGIN" to authenticate.
2. **Register**: Enter a new username and password, then click "REGISTER" to create a new account.
3. **Logout**: Click "LOGOUT" to end your session if you are logged in.


## File Structure
```
user-authentication-system/
├── auth_system.py
├── usrs.csv
├── README.md
└── requirements.txt
```


## Technologies Used
- **Tkinter**: Used for creating the GUI.
- **ttkbootstrap**: Adds modern themes and styles to the Tkinter GUI.
- **hashlib**: Used for hashing passwords.
- **CSV**: Used for storing and managing user data.

## Contributing
If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a feature branch:
    ```
    git checkout -b feature/NewFeature
    ```
3. Commit your changes:
    ```
    git commit -m 'Add some NewFeature'
    ```
4. Push to the branch:
    ```
    git push origin feature/NewFeature
    ```
5. Open a pull request.

## Author
Kevin Gonsalves

***Please be sure to check out my other repositories too!***

## Contact
Email: kevgon146@gmail.com
