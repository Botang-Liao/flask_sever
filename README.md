# Flask server

This project is for the backend server of the Hobhub application, and you can develop or test in this [docker container](https://github.com/Botang-Liao/pythonFlask-workspace).

The docker development environment for the flask projects based on Ubuntu 20.04 with SSH server and Ngrok installed.

Ｔhe frontend webpage code is [here](https://github.com/Botang-Liao/App)
## Development 
- Clone this repo
    ```shell
    $ https://github.com/Botang-l/flask_sever.git
    $ cd flask_sever
    ```
- Install the Python dependencies
    ```shell
    $ pip install -r deployment/requirements.txt
    ```
- Run the server on port 5000
    ```shell
    $ python local_server.py
    ```

## Project structure
```
├── deployment                  # configuration for deployment
│   └── requirements.txt        # Python package list
├── model                       # the class for specific utilities 
│   └── user.py                 # class user 
├── flaskr                      # backend server
│   ├── __init__.py             # the basic configuration of the web backend
│   ├── api_user.py             # APIs related to basic app usage by users
│   ├── api_auth.py             # APIs related to user login and logout.
│   └── utils.py                # General-purpose functions.
├── README.md
├── scripts                     # quickly deployment
│   ├── build.sh                
│   ├── kill.sh
│   └── run.sh
└── server.py                   # the backend server
```

