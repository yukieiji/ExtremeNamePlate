# ExtremeNamePlate
Extreme RolesのアドオンであるExtreme Skinsのネームプレートデータ管理用リポジトリ<br>
Extreme Skins以外のMOD(Extreme Skinsのフォーク等も含めて)でこのリポジトリのデータを使用する場合、このリポジトリ自体のライセンス(使用規約)を読み把握した上で各ネームプレートのグループにのライセンス(使用規約、LICENSE.md)に従って下さい<br>
このリポジトリのライセンスは[こちら](https://github.com/yukieiji/ExtremeNamePlate/blob/main/LICENSE.md)

## 新しいネームプレートの追加方法
- ネームプレートは[template.png](https://github.com/yukieiji/ExtremeNamePlate/blob/main/template.png)を元に作成すると楽です

### ExtremeSkins.Generatorを使用する場合
1. [ここ](https://github.com/yukieiji/ExtremeSkins.Generator/releases/latest)からExtremeSkins.Generatorの最新版をダウンロードする
  - エディションの違い、よくわからないって方はAllinOneをダウンロードして下さい(LightとAllinOneで機能の違いはありません)
    - AllinOne : 容量は大きいが何もしなくてもそのまま利用可能
    - Light : 容量は小さいが別途.NET 6.0 Runtimeのインストールが必要になります
2. ダウンロードしたZipファイルを適当な場所に展開する
3. 展開したフォルダの中にある「ExtremeSkins.Generator.exe」をダブルクリックして起動する
   - 起動しない場合はセキュリティソフトの設定を見直して下さい
4. 画面の「ExtremeNamePlate」を選択する
5. 必要なファイル等を画面に従って用意、選択する
6. エクスポートボタンを押す

### 手動でやる場合

0. 必要であれば、ExtremeNamePlateの下に新しいフォルダを作る(フォルダがグループ分けの目安になりますローマ字推奨、日本語等は使用しない)
1. 追加したいネームプレートの画像データ(名前はローマ字推奨、日本語等は使用しない、透過pngファイル)を追加したいグループのフォルダ入れる
2. ゲームを再起動する

- エラーが出た場合
  - AmongUs.exeのあるフォルダのBepInExの下にLogOutput.txtがあります。正しくロードできているとそのログの途中に以下の様な出力が出ているはずです
    - ```[Info   :Extreme Skins] NamePlate Loaded:（ネームプレートの画像名）, from:（ロードしているファイル名）```

## 他のMODのネームプレートをExtremeNamePlate用に変換したい
- [ExtremeSkins.Converter](https://github.com/yukieiji/ExtremeSkins.Converter/releases/latest)を使用することで変換できます

#### 身内内専用のネームプレートを追加して遊ぶ場合は[Impostor](https://github.com/Impostor/Impostor)等のカスタムサーバーの使用をおすすめします

## ネームプレートを提供していただいた方々
- [YJ\*白桜](https://twitter.com/_Sakura_White_)様(ExtremeNamePlateで使えるようにデータ構造を変更しています(ネームプレートデータがGNU General Public License v3.0ライセンスのため詳細を記載))
- アンハッピーセット様
- おやきもん様
- ラプ様
- クロドル様
- Nyayuta様
