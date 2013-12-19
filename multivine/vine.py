import multiprocessing
import re
import requests


RE_DICT = {'user': '\<p\sclass=\"username\"\>(.+)\<\/p\>',
          'user_avatar': '\<img\ssrc="(.+)"\sclass=\"avatar\"\>',
          'video_image': '\<meta\sproperty=\"og\:image\"\scontent=\"(.+)">',
          'video_description': '\<p\sclass\=\"description\"\>\s+(.+)\s+<\/p\>',
          'video_stream': '\<meta\sproperty=\"twitter\:player\:stream\"\s+content=\"(.+)"\>'}
VINE_C_DICT = []
VINE_R_DICT = {}

def check(url):
    check_vine_id = re.search('http(?:s)\:\/\/vine\.co\/v\/([a-zA-Z0-9]{1,})', url)
    if check_vine_id is not None:
        VINE_C_DICT.append(check_vine_id)
        return VINE_C_DICT


def fetch(url):
        request = requests.get(url)
        if not ( request.status_code == 200):
            raise BaseException('Page Not Found: {0}'.format(q))
        else:
            request = request.text
            VINE_R_DICT[url] = {
                        'author': {
                                'user': re.search(RE_DICT['user'], request).group(1),
                                'user_avatar': re.search(RE_DICT['user_avatar'], request).group(1),
                        },
                        'video_image': re.search(RE_DICT['video_image'], request).group(1),
                        'video_description': re.search(RE_DICT['video_description'], request).group(1),
                        'video_stream': re.search(RE_DICT['video_stream'], request).group(1),
                        }
        return VINE_R_DICT

def parse (vine_url):
    filter_DICT = filter(check, vine_url)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() * 2)
    result_list = [pool.apply(fetch, [vine]) for vine in filter_DICT]
    return result_list