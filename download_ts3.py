# -*- coding: utf-8 -*-
import os, shutil
import urllib.request, urllib.error, requests
import glob
# 打开并读取网页内容
def getUrlData(url):
    try:
        urlData = urllib.request.urlopen(url, timeout=20)  # .read().decode('utf-8', 'ignore')
        return urlData
    except Exception as err:
        print(f'err getUrlData({url})\n', err)
        return -1

# 下载文件-urllib.request
def getDown_urllib(url, file_path):
    try:
        urllib.request.urlretrieve(url, filename=file_path)
        return True
    except urllib.error.URLError as e:
        # hasttr(e, 'code')，判断e 是否有.code属性，因为不确定是不是HTTPError错误，URLError包含HTTPError，但是HTTPError以外的错误是不返回错误码(状态码)的
        if hasattr(e, 'code'):
            print(e.code)  # 打印服务器返回的错误码（状态码），如403，404,501之类的
        elif hasattr(e, 'reason'):
            print(e.reason)  # 打印错误原因


def getVideo_urllib(url_m3u8, path, videoName):

    print('begin run ~~\n')

    urlData = getUrlData(url_m3u8)
    num = 0
    #open a file store m3u8 list
    with open(os.path.join(path,'m3u8_list.txt'),'w') as m3u8file:
        for line in urlData:
            # 解码，由于是直接使用了所抓取的链接内容，所以需要按行解码，如果提前解码则不能使用直接进行for循环，会报错
            # 改用上面的readlines()或readline()也可以，但更繁琐些，同样需要按行解码，效率更低
            url_ts = line.decode('utf-8')
            tempName_ts = os.path.join(path, f'{num}.ts')  # f'{}' 相当于'{}'.format()
            if not '.ts' in url_ts:
                continue
            else:
                if not url_ts.startswith('http'):  # 判断字符串是否以'http'开头，如果不是则说明url链接不完整，需要拼接
                    m3u8file.write(url_ts)
                    # 拼接ts流视频的url
                    url_ts = url_m3u8.replace(url_m3u8.split('/')[-1], url_ts)
                else:
                    m3u8file.write(url_ts.split('/')[-1].strip('\n'))
            print(url_ts)
            getDown_urllib(url_ts, tempName_ts)  # 下载视频流

            num += 1

    m3u8file.close()
    print(f'finish down!')


def merge_video(file_path,videoName):
    file_list=open(os.path.join(path,'m3u8_list.txt')).readlines()

    output_video = os.path.join(path, f'{videoName}')
  #  shutil.move(tempName_ts, output_video)

    with open(output_video, 'wb+') as f:
        for idx in range(len(file_list)):
            with open('./video/'+str(idx)+'.ts', 'rb') as mergefile:
                shutil.copyfileobj(mergefile, f)
                print('merge'+os.path.join(file_path,f'{str(idx)}'))

        print(videoName + ' merged.')
    f.close()

if __name__ == '__main__':
    url_m3u8 = 'https://1252524126.vod2.myqcloud.com/522ff1e0vodcq1252524126/602b75385285890787265952362/playlist.f3.m3u8?time=1557823906960'
    path = r'./video'
    # if os.path.exists(path):
    #     print("File Exist!,delete it")
    #     os.rmdir(path)
    #     os.mkdir(path)
    # else:
    #     os.mkdir(path)
    #'台北'
    videoName = '1111.mp4'

    getVideo_urllib(url_m3u8, path, videoName)
    merge_video(path, videoName)