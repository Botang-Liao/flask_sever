# Flask sever

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
## how to maintain this repo
每次增修內容前請依循下列流程進行：
1. Pull origin/ 最新版本
    ```shell
    $ git pull
    ```
2. 在 local 新增 branch 並切換
    ```shell
    $ git checkout -b <NEW_BRANCH_NAME>
    ```
3. 編輯完成後請以 `prettier` 進行 syntax check 及 auto format，倘若沒有錯誤再進行 commit
    ```shell
    $ npx prettier --write .
    $ git add .
    $ git commit -m "COMMIT_MSG"
    ```
4. 回到 master 再次獲取 origin/master 的最新版本、與自己的修正合併並修正出現的 conflict
    ```shell
    $ git checkout master
    $ git pull
    $ git checkout <NEW_BRANCH_NAME>
    $ git rebase master
    ```
5. 將新 branch 的修正與 master 合併並 push 到 GitLab
    ```shell
    $ git checkout master
    $ git merge <NEW_BRANCH_NAME>
    $ git push
    ```
