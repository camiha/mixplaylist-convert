# mixplaylist-convert
Youtubeにおけるmixplaylist(複数の楽曲を一つの動画にまとめたプレイリスト)を  
spotifyのプレイリストに変換します.   

動画概要欄の楽曲情報を正規表現で抽出し,spotifyで検索・プレイリストを作成します.

## 使用方法
1. 必要apiキーの取得・登録
    * [spotify developers](https://developer.spotify.com/)にてアプリ作成  
    * cliant id/client secretを取得   
        参考:[Spotify Developer Platform: Spotify APIアクセスしてデータ取得してみてみた - Qiita](https://qiita.com/shirok/items/ba5c45511498b75aac27)   
   
    * [google cloud platform](https://console.cloud.google.com/)にてyoutube data apiの登録，apiキーの取得  
        参考:[Youtube Data APIを使ってPythonでYoutubeデータを取得する - Qiita](https://qiita.com/g-k/items/7c98efe21257afac70e9)   
   
    * 各apiキーをconvert.py内の該当場所にペースト

2. 必要ライブラリのインストール
```
% pip install google-api-python-client
% pip install spotipy
```

3. 実行
```
% python3 convert.py 

Please Input Your UserID
>> e0gqy0t4edd27782g8r930bto #自分のユーザIDを入力してください．（認証画面が別ウィンドウで表示されます）

Please Input Mixtape URL
>> https://www.youtube.com/watch?v=BKjX5UWsH_U 

❌ Not Found : Marietta – cinco de mayo shitshow
⭕ Add Success : graves. – Midwest Sports
⭕ Add Success : Olde Pine – For Twinny
⭕ Add Success : Mosey Jones – Linda Schuyler
⭕ Add Success : Marietta – god bless eric taylor
⭕ Add Success : Plainclothes – Burt Reynolds Burnt Candles
⭕ Add Success : You’ll Live – Maybe You Were Right
❌ Not Found : TWIABP – Walnut Street
⭕ Add Success : Gleemer – Workout
⭕ Add Success : Feed Me To The Forest – Survivor’s Guilt
❌ Not Found : Daephne – If This Is Living The Dream Then I Want Out
⭕ Add Success : Caving – Chore
⭕ Add Success : California Cousins – Soft Earth
⭕ Add Success : Bike Cruise – My Boyfriend is Pizza
⭕ Add Success : Bike Path – Saints 

📢 Playlist Convert Success 📢 
```

## ToDo 
* webアプリ化 
* 抽出機能の高精度化
   * 投稿者がスペルミスをしていても検索できるように 
   * 正規表現の見直し
