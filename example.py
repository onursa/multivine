from multivine import vine

vine_url = ['https://vine.co/v/h7O9FnKl5rI',
            'https://vine.co/v/h0alual61e9']
data = vine.parse(vine_url)
print(data)