# -*- coding: utf-8 -*-
import platform
import json
import utility

from threading import Thread

from flask import Flask, request, jsonify

from PaddleTools.TTS import TTSExecutor
from ppgan.apps.wav2lip_predictor import Wav2LipPredictor

from arguments import get_args

app = Flask(__name__)
app.debug = True


@app.route('/post_video_status', methods=['post'])
def post_http():
    if not request.data:  # 检测是否有数据
        return jsonify(code=300,
                       msg='ok',
                       data='fail')

    params = request.data.decode('utf-8')
    prams = json.loads(params)

    if len(prams['text']) <= args.Max_Text_Length:
        # utility.general_video(wav2lip_predictor, TTS, prams['text'])
        Thread(target=utility.general_video,
               args=(wav2lip_predictor, TTS, prams['text'])).start()
    else:
        # utility.scheduler(wav2lip_predictor, TTS, prams['text'])
        Thread(target=utility.scheduler,
               args=(wav2lip_predictor, TTS, prams['text'])).start()

    return jsonify(code=200,
                   msg='ok',
                   data='success')


if __name__ == '__main__':
    args = get_args()

    if platform.system() != 'Windows':
        path = args.path_to_push + 'push_streaming.sh'
        Thread(target=utility.push_streaming,
               args=[path]).start()
    else:
        path = args.path_to_push + 'push_streaming.bat'
        Thread(target=utility.push_streaming,
               args=[path]).start()

    # 热加载
    wav2lip_predictor = Wav2LipPredictor(face_det_batch_size=args.face_det_batch_size,
                                         wav2lip_batch_size=args.wav2lip_batch_size,
                                         face_enhancement=True)
    TTS = TTSExecutor(args.TTS_Config)

    app.run(host=args.host, port=args.port)
