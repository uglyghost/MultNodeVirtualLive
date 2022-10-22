from argparse import ArgumentParser

parser = ArgumentParser(description='')

'''
basic information
'''
# network
parser.add_argument('--host', default='127.0.0.1',
                    type=str, help='Server Host IP')
parser.add_argument('--port', default=10100,
                    type=int, help='Server IP port')

# other
parser.add_argument('--Max_Text_Length', default=100,
                    type=int, help='Max length of single text for one general video')
parser.add_argument('--window_size', default=2,
                    type=int, help='')
parser.add_argument('--start_up_delay', default=3,
                    type=int, help='')

'''
model parameters
'''
# Wav2LipPredictor model
parser.add_argument('--face_det_batch_size', default=2,
                    type=int, help='')
parser.add_argument('--wav2lip_batch_size', default=16,
                    type=int, help='')
parser.add_argument('--face_enhancement', default=True,
                    type=bool, help='')

# TTS model
parser.add_argument('--TTS_Config', default='./Config/default.yaml',
                    type=str, help='path to Config file of TTS (text to speech)')

'''
path settings
'''
# model training
parser.add_argument('--input_video_path', default='./Input/zimeng.mp4',
                    type=str, metavar='PATH',
                    help='path to input video')
parser.add_argument('--temp_path', default='./Stream/',
                    type=str, metavar='PATH',
                    help='path to temp files')

# live streaming
parser.add_argument('--path_to_push', default='D:/Multimedia/MultNodeVirtualLive/Stream/',
                    type=str, metavar='PATH',
                    help='path to script of push streaming')
parser.add_argument('--stream1_path', default='./Stream/stream1.mp4',
                    type=str, metavar='PATH',
                    help='path of video stream 1')
parser.add_argument('--stream2_path', default='./Stream/stream2.mp4',
                    type=str, metavar='PATH',
                    help='path of video stream 2')
parser.add_argument('--recovery_list_path', default='./Stream/listR',
                    type=str, metavar='PATH',
                    help='path to file of recovery video list')
parser.add_argument('--tmp_video_path', default='./Stream/listC',
                    type=str, metavar='PATH',
                    help='path to list of general videos')


args = parser.parse_args()


def get_args():
    arguments = parser.parse_args()
    return arguments
