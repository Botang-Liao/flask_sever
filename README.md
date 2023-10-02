# Flask sever

This project is for the backend server of the Hobhub application, and you can develop or test in this [docker container](https://github.com/Botang-Liao/pythonFlask-workspace).

The docker development environment for the flask projects based on Ubuntu 20.04 with SSH server and Ngrok installed.

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
ITH Website/
├── app/                        # frontend webpage
│   ├── images/                 # common images
│   └── index.html
├── database/
│   └── data.sqlite
├── deployment/                 # configuration for deployment
│   └── requirements.txt        # Python package list
├── flaskr/                     # backend server
├── README.md
└── local_server.py
└── server.py
```

