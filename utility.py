import os
import time
import subprocess
import platform
import re

from threading import Thread

from arguments import get_args
args = get_args()


'''
推流视频
'''


def push_streaming(path):
    print(path)
    subprocess.Popen(path, shell=True, stdout=subprocess.PIPE)


'''
恢复被修改的视频
'''


def recovery_video():
    command = 'ffmpeg -y -f concat -i ' + args.recovery_list_path + ' -c copy ' + args.stream1_path
    subprocess.call(command, shell=platform.system() != 'Windows')


'''
生成视频基本单元
'''


def change_video(model, TTS, text, index):
    wavFile_path = args.temp_path + 'output' + str(index) + '.wav'
    TTS.run(text=text, output=wavFile_path)
    video_opening_path = args.temp_path + 'opening.mp4'
    video_ending_path = args.temp_path + 'ending.mp4'
    if index == -1:
        model.run(args.input_video_path, wavFile_path, args.stream1_path)
    elif index == 0:
        model.run(args.input_video_path, wavFile_path, video_opening_path)
    else:
        model.run(args.input_video_path, wavFile_path, video_ending_path)
        command = 'ffmpeg -y -i ./Stream/opening.mp4 -i ./Stream/ending.mp4 -filter_complex "[0:0] [0:1] [1:0] [1:1] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" ./Stream/stream1.mp4'
        subprocess.call(command, shell=platform.system() != 'Windows')
        command = 'ffmpeg -y -f concat -i ' + args.tmp_video_path + ' -c copy ' + video_opening_path
        subprocess.call(command, shell=platform.system() != 'Windows')
    os.remove(wavFile_path)


'''
按固定间隔分割句子
'''


def cut_text(obj, sec):
    return [obj[i:i+sec] for i in range(0, len(obj), sec)]


'''
根据标点符号分割句子
'''


def segmentation_text(text):
    pattern = r'\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|。|、|；|‘|’|【|】|·|！| |…|（|）'
    out_text = re.split(pattern, text)
    while '' in out_text:
        out_text.remove('')
    return out_text


'''
生成短视频（2秒左右）
'''


def general_video(model, TTS, text):
    change_video(model, TTS, text, -1)
    time.sleep(args.window_size + args.start_up_delay)
    recovery_video()


'''
多节点调度算法（未完善待优化）
'''


def scheduler(model, TTS, text):
    out_text = cut_text(text, args.Max_Text_Length)  # 中间存在卡顿问题！
    # out_text = segmentation_text(text)

    for index, value in enumerate(out_text):
        if index == 0:
            change_video(model, TTS, value, index)   # 需补充网络协同视频生成  参考模块socketserver！
            # Thread(target=change_video, args=(model, TTS, text, index)).start()
        else:
            change_video(model, TTS, value, index)   # 需补充网络协同视频生成
            # Thread(target=change_video, args=(model, TTS, text, index)).start()

    time.sleep(len(out_text) * args.window_size + args.start_up_delay)
    recovery_video()

