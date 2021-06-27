# 『PENTO-ARTS』とは？
Webアプリ開発初心者が作成した投稿型SNSとなります。

# ◆本サービスの作成目的

* 自己学習（楽しく開発できました！）
* ポートフォリオ

# ◆実装内容一覧

# 1.ログイン・新規登録

☆django-allauthで実装

## 〈遷移図〉
![ユーザー認証遷移図](/img/スライド1.PNG) 

## (1)ログイン

ログイン前のトップ画面です。  
登録したメールアドレス・パスワードを入力することで、タイムライン画面へと遷移します。  
まだユーザー登録をしていない場合は、『_新規登録はこちら_』で新規登録を行って頂きます。  
![ログイン](/img/スライド2.PNG) 

## (2)新規登録

ユーザー登録画面です。
メールアドレス・ユーザー名・パスワード・パスワード（確認用）を入力後、『_登録する_』をクリックします。  
クリック後、自動的に作成したユーザー名でタイムライン画面へと遷移します。
![新規登録](/img/スライド3.PNG) 

# 2.タイムライン・プロフィール

## 〈遷移図〉
![タイムライン遷移図](/img/スライド5.PNG)

## (1)タイムライン  

ログイン後のタイムライン画面です。  
ツイートを投稿する、他ユーザー投稿の閲覧、いいね、プロフィール閲覧等、様々な機能が集約されています。  
![タイムライン遷移図](/img/スライド4.PNG)





# 3.フォロー機能
* フォロー後、プロフィールにフォロー数、フォロワー数が反映される。
　※まだまだ機能追加の余地が沢山ありますが、そこは順々に追加していきます。。。

# 3.今後実装予定の機能

* 通知
* 投稿コメント
* 検索機能
* タグ機能  

※他にも思いつき次第、順次追加していく予定です。

# 製作者

* 作成者：吉田　剛史（タケシ）
* E-mail：rainhistory0901@gmail.com


