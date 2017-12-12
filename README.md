# emojis

downloads apple, twitter, google and one emojis from unicode.org

```
curl http://www.unicode.org/emoji/charts/full-emoji-list.html -o full-emoji-list.html

pip install beautifulsoup4

python3 ./parse.py

zip -r emojis.zip ./images emojis.csv

```

### `parse.py` creates `emojis.csv`:

|no|codepoints|filename|emoji|
| --- | ---  | ---  | --- |
|1|\u{1f600}|1f600.png|😀|
|2|\u{1f601}|1f601.png|😁|
|3|\u{1f602}|1f602.png|😂|
|4|\u{1f923}|1f923.png|🤣|
|5|\u{1f603}|1f603.png|😃|
|6|\u{1f604}|1f604.png|😄|
|7|\u{1f605}|1f605.png|😅|
|8|\u{1f606}|1f606.png|😆|
|9|\u{1f609}|1f609.png|😉|
|75|\u{1f92e}|1f92e.png|🤮|

### ... and images:

```
./images
├── apple
│   ├── 0023_fe0f_20e3.png
│   ├── 002a_fe0f_20e3.png
│   ├── 0030_fe0f_20e3.png
│   └── ...
├── google
│   ├── 0023_fe0f_20e3.png
│   ├── 002a_fe0f_20e3.png
│   ├── 0030_fe0f_20e3.png
│   └── ...
├── one
│   ├── 0023_fe0f_20e3.png
│   ├── 002a_fe0f_20e3.png
│   ├── 0030_fe0f_20e3.png
│   └── ...
└── twitter
    ├── 0023_fe0f_20e3.png
    ├── 002a_fe0f_20e3.png
    ├── 0030_fe0f_20e3.png
    └── ...png
 ```
