#multivine
## usage
```python

from multivine import vine

vine_url = ['https://vine.co/v/h7O9FnKl5rI',
            'https://vine.co/v/h0alual61e9']
data = vine.parse(vine_url)
print(data)
```

```python
{
    'https://vine.co/v/h7O9FnKl5rI': {
        'video_image': 'https://v.cdn.vine.co/r/thumbs/B6F7F1BA-DD17-4F17-B96B-48D7EB8350D1-7204-00000729248B64FF_1b050e82df2.1.mp4.jpg?versionId=ME4ofp.K6TB_xO_0RYON_g14qCzH9YcU',
        'author':
            {'user_avatar': 'https://v.cdn.vine.co/r/avatars/5466C10154994631820706775040_128b143a36c.3.1_8TenK0ry0B7GwGJaiUM_O_F5dF9iVB4r3TPGc4a1PSLE9CYOgqcIAXjZJyKofGKi.jpg?versionId=45q4RtRoDt7U6OvPJlz4FkOfxtUQVHdx',
             'user': 'Memeli Mestan'
            },
        'video_description': 'Didem bebek henüz üç aylıktı..',
        'video_stream': 'https://mtc.cdn.vine.co/r/videos/B6F7F1BA-DD17-4F17-B96B-48D7EB8350D1-7204-00000729248B64FF_183389227f9.1.mp4?versionId=40WOhHJBQUado10JcAL4I2MpzLpH2xWv'
         }
},
{
    'https://vine.co/v/h0alual61e9': {
        'video_image': 'https://v.cdn.vine.co/r/thumbs/A3E683AD801024403492053442560_1ee43d76e1b.4.5.15177484147661946212.mp4_ooYUkwefy.0w.hEXL.MUJF6jFLqXk4JbU0FdG04Y6yBfTY0QNxKPD6OpP5Gk6Ekg.jpg?versionId=8esiyd7vjwLhNqZqJSX03u.fGOTHLZgS',
        'author':
            {'user_avatar': 'https://v.cdn.vine.co/r/avatars/92202FCFF01018933475312623616_1782759d2a8.4.4_TwUNgSYyvDZWfiV_JXKpx6z6A93UYnM5zT9yqLLi_M2hncSa280ztv73s35QUwhM.jpg?versionId=yxuGjKcL78L30jvUbBDydiVY6jMGNmzE',
             'user': 'djchrissayDiJAshotta'
            },
        'video_description': 'WHOS MORE FASTER Eminem OR Twista?(sorry for di faces dat how mi felt wen mi hear dem rap fast an yuh can&#39;t understand wah di hell dey say)',
        'video_stream': 'https://mtc.cdn.vine.co/r/videos/DE302B35211024403474235977728_169b60aeef1.4.5.15177484147661946212_8TSp_OB1tFqP4Org0bQ4r3W37rVfDpy1vXB7RVEvRVMeLLz8lrDSZd5Hy2HIZk2v.mp4?versionId=SK_d8nzVGDz_QSbN4MhheLk8elnJpspJ'
    }
}
```