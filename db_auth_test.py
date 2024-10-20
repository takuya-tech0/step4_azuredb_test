import mysql.connector
from mysql.connector import errorcode

# データベース接続情報の設定
config = {
    'host': 'tech0-gen-7-step4-studentwebapp-test.mysql.database.azure.com',
    'user': 'tech0gen7student',
    'password': 'F4XyhpicGw6P',  # 実際のパスワードに置き換えてください
    'database': 'legotest',  # 実際のデータベース名に置き換えてください
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': '/Users/takuya/Downloads/AzureMySQL_Connection/DigiCertGlobalRootCA.crt.pem'  # 実際の証明書パスに置き換えてください
}

# データベース接続を取得
try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
    
    cursor = conn.cursor()
    
    # ここでデータベース内のユーザー情報を仮に取得します（必要に応じてSQLクエリを変更）
    query = "SELECT username, password FROM users;"  # 実際のテーブル名とカラム名に置き換えてください
    cursor.execute(query)
    
    # データを取得
    users = {username: password for username, password in cursor.fetchall()}
    
    # テスト用の入力データ
    input_username = "lego"
    input_password = "password456"
    
    # 認証チェック
    if input_username in users and users[input_username] == input_password:
        print(f"ようこそ！{input_username}さん")
    else:
        print("認証失敗")

    # 接続を閉じる
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("ユーザー名またはパスワードに誤りがあります")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("データベースが存在しません")
    else:
        print(err)
