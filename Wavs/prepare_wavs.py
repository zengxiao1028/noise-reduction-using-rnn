import soundfile as sf
import os



def run():
    train_dir = '/data/xiao/Hearing_Challenge/openSLR/LibriSpeech/train-clean-100'
    paths = os.walk(train_dir)
    for top, dirs, nondirs in paths:
        for file in nondirs:
            if file.find('.flac')>0:
                data, samplerate = sf.read(os.path.join(top,file))
                sf.write(file[:-4]+'wav', data, samplerate)

if __name__ == '__main__':
    run()

