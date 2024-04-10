import MediaInfo
filepath = 'D:/testInput/spotJog.mp4'
info = MediaInfo.MediaInfo(filename=filepath)
infoData = info.getInfo()
print(infoData,info._ffmpegGetInfo.__class__)