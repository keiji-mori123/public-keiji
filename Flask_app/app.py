from flask import Flask,url_for
from flask import render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from datetime import datetime
import pytz
from flask import current_app
from sqlalchemy.orm import DeclarativeBase
from flask_login import UserMixin,LoginManager,login_user,logout_user,login_required, current_user
import os
from werkzeug.security import generate_password_hash,check_password_hash
from flask_bootstrap import Bootstrap
from flask import flash

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app インスタンス作成
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
#appにSQLightを認識させるコード。そしてdb名は「blog.db」
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
#ここにシークレットキーを入れて、ログイン情報などを秘匿する。
app.config["SECRET_KEY"] = os.urandom(24)
#ここでdbを初期化する。
db = SQLAlchemy(app)
#bootstrap(装飾)とappを紐づける。
bootstrap = Bootstrap(app)

#ログインのためのインスタンス作成、そしてappのインスタンスと連接する。
login_manager = LoginManager()
login_manager.init_app(app)

#ここでテーブル、カラムとか作る。
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,
                           default=datetime.now(pytz.timezone("Asia/Tokyo")))
    
#ログインの情報を入れたテーブル作成
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(12))  

#flaskでは必須のコード。ログイン状況を把握するもの。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# アプリケーションコンテキストを手動で作成
with app.app_context():
    # データベースを作成
    db.create_all()

#最初に表示するのはログイン画面
@app.before_request
def before_request():
    if not request.path.startswith('/login') and not request.path.startswith('/signup') and not current_user.is_authenticated:
        # 未ログイン状態で、かつログインまたはサインアップ以外のリクエスト時に/loginにリダイレクトする
        return redirect(url_for("login"))

#ホーム画面
@app.route("/",methods =["GET","POST"])
@login_required
def index():
    if request.method =="GET":
        posts = Post.query.all()
        return render_template("index.html",posts=posts)

#サインアップ  
@app.route("/signup", methods=["GET","POST"])
def signup():
    #この文でhtmlのメソッド別に条件分岐する。
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User(username=username,password=generate_password_hash(password,method="pbkdf2:sha256"))
        #これでdbにデータをインサートする。
        db.session.add(user)
        db.session.commit()
        #サインインできたら、ログイン画面に遷移させる。
        return redirect("/login")
    else:
        return render_template("signup.html")
        
#ログイン
@app.route("/login", methods=["GET","POST"])
def login():
    #この文でhtmlのメソッド別に条件分岐する。ログインする時に入力された値を取ってくる。
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")

         # 入力が空欄の場合にエラーメッセージを表示（例外処理）
        if not username or not password:
            flash("ログイン情報を入力してください。", "error")
            return redirect("/login")
        
        user = User.query.filter_by(username=username).first()
        # ユーザーが存在しない場合やパスワードが一致しない場合にエラーメッセージを表示（例外処理）
        if user is None or not check_password_hash(user.password, password):
            flash("有効なユーザー名、パスワードを入力してください。", "error")
            return redirect("/login")
        # ログインが成功した場合
        login_user(user)
        return redirect("/")
    else:
        return render_template("login.html")
        #elseは、get（サイトを閲覧するだけ。）の場合は、ログイン画面見ることができる。

#ログアウト       
@app.route("/logout")
#ログインしているからこそログアウトできる。というコード（アクセス制限）
@login_required
def logout():
    logout_user()
    return redirect("/login")
    
#新規登録
@app.route("/create", methods=["GET","POST"])
@login_required
def create():
    #この文でhtmlのメソッド別に条件分岐する。フォーム（create.html）に入力された値を使うコード。
    if request.method =="POST":
        title = request.form.get("title")
        body = request.form.get("body")
        #上で作成したPostカラムごとに入力された値を放り込む。
        post = Post(title=title,body=body)
        #これでdbにデータをインサートする。
        db.session.add(post)
        db.session.commit()
        #登録完了したらindex.htmlの画面に戻る。
        return redirect("/")
    else:
        return render_template("create.html")
        
#update      
@app.route("/<int:id>/update", methods=["GET","POST"])
@login_required
def update(id):
    post = Post.query.get(id)    
    #この文でhtmlのメソッド別に条件分岐する。フォーム（create.html）に入力された値を使うコード。
    if request.method =="GET":
        return render_template("update.html",post=post)
    else:
        #新規登録とは違い、該当するpostデータについて上書きする動きになる。
        post.title = request.form.get("title")
        post.body = request.form.get("body")
        db.session.commit()
        #登録完了したらindex.htmlの画面に戻る。
        return redirect("/")   

#delete
@app.route("/<int:id>/delete", methods=["GET"])
@login_required
def delete(id):
    post = Post.query.get(id) 
    db.session.delete(post)
    db.session.commit()
    return redirect("/")    

#以下は、デバックモードをオンに強制的に行うもの。
if __name__ == "__main__":
    app.run(debug=True)