
from utils import *

device = 'cpu'

def train():
    a_content, sr = wav2spectrum('./data/boy.wav')
    a_style, sr = wav2spectrum('./data/girl.wav')

if __name__ == "__main__":
    pass