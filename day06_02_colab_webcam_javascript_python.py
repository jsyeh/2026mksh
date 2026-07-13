# day06_02_colab_webcam_javascript_python.py
# 將 day06_01 丟給 ChatGPT 得到3段程式, 如下, 能在 Colab 秀出視訊畫面

from IPython.display import display, Javascript
from google.colab.output import eval_js

import cv2
import numpy as np
import base64

def take_photo():

    js = Javascript('''
    async function takePhoto() {
      const div = document.createElement('div');
      const video = document.createElement('video');

      const stream = await navigator.mediaDevices.getUserMedia({
          video: true
      });

      document.body.appendChild(div);
      div.appendChild(video);

      video.srcObject = stream;
      await video.play();

      google.colab.output.setIframeHeight(document.body.scrollHeight, true);

      await new Promise(resolve => setTimeout(resolve, 1000));

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;

      canvas.getContext('2d').drawImage(video, 0, 0);

      stream.getTracks()[0].stop();

      div.remove();

      return canvas.toDataURL('image/jpeg');
    }
    ''')

    display(js)

    data = eval_js('takePhoto()')

    binary = base64.b64decode(data.split(',')[1])

    img = np.frombuffer(binary, dtype=np.uint8)

    return cv2.imdecode(img, cv2.IMREAD_COLOR)


img = take_photo()

cv2.imwrite("photo.jpg", img)

from google.colab.patches import cv2_imshow

cv2_imshow(img)
