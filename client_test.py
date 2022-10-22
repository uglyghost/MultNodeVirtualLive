# -*- coding: utf-8

import json
import requests

from arguments import get_args

args = get_args()


data = {}
url = 'http://' + args.host + ':' + str(args.port) + '/post_video_status'

short_text = '今天天气真好啊！'
length_text = '图片胜于文字，而视频更胜于图片，相比文字和图片，视频这种多媒体形式在有效吸引用户视线、增强用户理解等方面的能力是毋庸置疑的。'
data["text"] = short_text

r = requests.post(url, data=json.dumps(data))