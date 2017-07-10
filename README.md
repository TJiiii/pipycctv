# 기초환경 설정

### 파이 업데이트

```
$ sudo apt-get upgrade
$ sudo apt-get update
$ sudo apt-get install rpi-update && sudo rpi-update
$ sudo reboot
```


### 카메라모듈 연결
```
$ sudo raspi-config 
```
에서 카메라 항목 enable

```
$ sudo modprobe bcm2835-v4l2
```

이 명령어로 /dev/video0 로 파이카메라를 인식


### opencv 3.2.0 의존성 패키지설치

OpenCV를 컴파일하는데 사용하는 것들이 포함된 패키지들을 설치합니다. 

build-essential 패키지에는 C/C++ 컴파일러와 관련 라이브러리, make 같은 도구들이 포함되어 있습니다.

cmake는 컴파일 옵션이나 빌드된 라이브러리에 포함시킬 OpenCV 모듈 설정등을 위해 필요합니다. 

``` 
$ sudo apt-get install build-essential cmake
```

pkg-config는 프로그램 컴파일 및 링크시 필요한 라이브러리에 대한 정보를 메타파일(확장자가 .pc 인 파일)로부터 가져오는데 사용됩니다. 

터미널에서 특정 라이브러리를 사용한 소스코드를 컴파일시 필요한 컴파일러 및 링커 플래그를 추가하는데 도움이 됩니다.
 
```
$ sudo apt-get install pkg-config
```

특정 포맷의 이미지 파일을 불러오거나 기록하기 위해 필요한 패키지들입니다.

 
```
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
```

특정 코덱의 비디오 파일을 읽어오거나 기록하기 위해 필요한 패키지들입니다. 
```
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev 
$ sudo apt-get install libxvidcore-dev libx264-dev libxine2-dev
```

Video4Linux 패키지는 리눅스에서 실시간 비디오 캡처를 지원하기 위한 디바이스 드라이버와 API를 포함하고 있습니다. 

``` 
$ sudo apt-get install libv4l-dev v4l-utils
```

GStreamer는 비디오 스트리밍을 위한 라이브러리입니다. 

```
$ sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 
```
 

OpenCV에서는 highgui 모듈을 사용하여 자체적으로 윈도우 생성하여 이미지나 비디오들을 보여줄 수 있습니다. 

윈도우 생성 등의 GUI를 위해 gtk 또는 qt를 선택해서 사용가능합니다.

여기서는 qt4를 지정해주었습니다. QImage와 Mat 간의 변환에는 영향을 주지 않습니다.

 
```
$ sudo apt-get install libqt4-dev 
```

그외 선택 가능한 패키지는 다음과 같습니다.

libgtk2.0-dev
libgtk-3-dev

libqt5-dev


OpenGL 지원하기 위해 필요한 라이브러리입니다.

```
$ sudo apt-get install mesa-utils libgl1-mesa-dri libqt4-opengl-dev 
```
 
OpenCV 최적화를 위해 사용되는 라이브러리들입니다.

 
```
$ sudo apt-get install libatlas-base-dev gfortran libeigen3-dev
```

python2.7-dev와 python3-dev 패키지는 OpenCV-Python 바인딩을 위해 필요한 패키지들입니다. 

Numpy는 매트릭스 연산등을 빠르게 처리할 수 있어서 OpenCV에서 사용됩니다. 

```
$ sudo apt-get install python2.7-dev python3-dev
$ sudo apt-get install python-numpy python3-numpy
```

대충 합쳐서
```
$ sudo apt-get install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev libv4l-dev v4l-utils libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libqt4-dev libgtk2.0-dev libgtk-3-dev mesa-utils libgl1-mesa-dri libqt4-opengl-dev libatlas-base-dev gfortran libeigen3-dev python2.7-dev python3-dev python-numpy python3-numpy
```

### opencv 설치

작업 디렉토리 생성 
```
$ mkdir opencv
$ cd opencv
```
opencv 3.2.0 버젼 소스파일
```
$ wget https://github.com/opencv/opencv/archive/3.2.0.zip
$ wget https://github.com/opencv/opencv_contrib/archive/3.2.0.tar.gz
```
압축해제
```
$ unzip 3.2.0.zip 
$ tar zxf 3.2.0.tar.gz 
```
빌드 디렉토리 생성

```
$ cd opencv-3.2.0/
$ mkdir build_with_contrib
$ cd build_with_contrib/
```
cmake
```
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D PLANTUML_JAR=/usr/share/java/plantuml.jar \
-D ENABLE_NEON=ON \
-D WITH_TBB=OFF \
-D BUILD_TBB=OFF \
-D WITH_QT=ON \
-D WITH_OPENGL=OFF \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules \
-D BUILD_opencv_freetype=OFF \
-D BUILD_EXAMPLES=OFF ..
```

빌드
```
$ make -j4
```

인스톨
```
$ sudo make install
```

### 서보모터 설정

카메라를 이리저리 돌아가게 만들 생각이기 때문에...

라즈베리파이 3 model b 기준으로

참고 : https://pinout.xyz/#

서보모터의 
주황색라인을 12번핀
빨간색라인을 2번핀
갈색라인을 6번핀 에 연결

gpio.rpi 라이브러리 설치

```
$ sudo apt-get install python-rpi.gpio
```

설치 후

import RPi.GPIO 
만 가능하다면 제대로 작동하는것.
 
ServoMotor 디렉토리의 테스트로 확인가능


## UV4L

```
$ wget http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc && sudo apt-key add ./lrkey.asc
```

/etc/apt/source.list 에 
```
deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ jessie main
```
라인을 추가

소스를 추가했기 때문에 업데이트를 시켜준다

```
$ sudo apt-get update
```

uv4l 과 uv4l-raspicam 패키지를 설치

```
$ sudo apt-get install -y uv4l-raspicam
```

uv4l 에 대한 상세한 메뉴얼

```
$ man uv4l
$ man uv4l-raspicam
```

시스템 시작마다 자동으로 관련모듈 적재를 위한 패키지 설치

```
$ sudo apt-get install uv4l-raspicam-extras
```

서비스 실행

```
$ sudo service uv4l_raspicam restart
```

uv4l 옵션

```
$ uv4l --help --driver raspicam --driver-help
```

http 스트리밍을 위한 패키지 설치

```
$ sudo apt-get install uv4l-server
$ sudo apt-get install uv4l-uvc
$ sudo apt-get install uv4l-xscreen
$ sudo apt-get install uv4l-mjpegstream
```

다시 서비스를 재실행한후 
로컬호스트의 8080 포트로 접속하면 스트림 영상 등 uv4l 의 다양한 기능을 확인할 수 있다

### opencv 참고사이트

http://a244.hateblo.jp/entry/2016/12/30/235927

http://webnautes.tistory.com/916

