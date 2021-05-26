def getFrames(signal, size, overlap):
    step = int(size * overlap)
    i = 0
    while i < len(signal):
        yield signal[i:i+size]
        i += step
signal = [i for i in range(15)]
print("Сигнал: {}".format(signal))
for frame in getFrames(signal, 3, 0.5):
    print(frame)