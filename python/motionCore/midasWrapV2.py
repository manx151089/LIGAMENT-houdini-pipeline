import glob
import os
import subprocess
import MiDaS as midas
import mimetypes
import logging
from motionCore import videoToImg
def checkVideo(filepath):
    fileInfo = mimetypes.guess_type(filepath)#parse doesnt seem to exist in MediaInfo
    if fileInfo[0] is None:
        return False
    if fileInfo[0].startswith("video") is True:
        return True
    else:
        return False
def removeBackSlash(filepath):
    mystr = '/'.join(filepath.split('\\'))
    return mystr
def run(input="",output="",verbose=0,modelType='dpt_beit_base_384'):
    """
    run(input=string,output=string,verbose=int)
    
    input: A path for a folder which has the images needed to be rendered a z-depth estimation. If it finds video in this folder it will convert that to images first.
    
    output: A path for a folder which will have the rendered z-depth

    verbose: An integer which is either 0 or 1 for logging incase you are running into issues
    """
    mBase = midas.__path__._path[0]
    mBase = '/'.join(mBase.split('\\'))
    
   # run = 'python {0}/run.py --model_weights {0}/weights/{1}.pt --model_type {1}'.format(mBase,modelType)
    command = [
        'python',
        os.path.join(mBase,'run.py'),
        '--model_weights',os.path.join(mBase,'weights',f'{modelType}.pt'),
        '--model_type',modelType
    ]
    if input != "":
        command.extend(['--input_path', input])
    if output != "":
        command.extend(['--output_path', output])

    # Execute the command using subprocess.check_output
    try:
        log = subprocess.check_output(command, stderr=subprocess.STDOUT)
        if verbose == 1:
            print(log.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        # Handle errors in the called executable
        if verbose == 1:
            print("Error during subprocess call:", e.output.decode('utf-8'))
    except Exception as e:
        # Handle other exceptions such as file not found error
        if verbose == 1:
            print("Execution failed:", str(e))
"""
    if input!="":
        if(os.path.exists(input)):
            files=glob.glob(os.path.join(input,"*"))
            files = [removeBackSlash(x) for x in files]
            videos = [x for x in files if checkVideo(x)]
            if verbose==1:
                print("videos:",videos,"\n files:",files)
            ext = os.path.splitext(input)[-1]
            if(len(videos)>0):
                images = os.path.join(input,'images')
                if verbose==1:
                    print("video found converting to jpgs")
                for each in videos:
                    print(dir(videoToImg),videoToImg)
                    videoToImg.convertMp4ToJpg(each,images,mkdir=True)
                input = images
            if verbose==1:
                print("input:",input)
            run += ' --input_path '+input
    if output!="":
        if(os.path.exists(output)):
            pass
        else:
            os.makedirs(output)
        run += ' --output_path '+output
        if verbose==1:
            print("output:",output)
    log = subprocess.check_output(run)#try subprocess here instead
    if verbose==1:
        print(log)
"""

if __name__=="__main__":
    #testing
    run(input='D:/testInput/',output='D:/testOutput2/')
