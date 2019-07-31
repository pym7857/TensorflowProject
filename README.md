# TensorflowProject
다변인 선형회귀를 이용한 가격예측 프로그램 

## Web Site
![1](./image/1.png)

## 서버 실행
```
# 깃 허브에서 소스코드를 다운로드 받습니다.
git clone https://github.com/pym7857/TensorflowProject.git

# 받은 프로젝트 폴더로 이동합니다.
cd TensorflowProject

# 플라스크 웹 서버 폴더로 이동합니다.
cd "Web"

# 웹 서버를 실행합니다.
python server.py
```

## 파이썬 데이터 학습 모델 생성
```
# 프로젝트 폴더에서 파이썬 폴더로 이동합니다.
cd "Python Code"

# 엑셀(Excel) 파일로 학습을 수행합니다.
python offline_save.py

# (옵션) 학습된 데이터를 확인합니다.
python "user_input.py"
>> 평균 온도: -2.7
>> 최저 온도: -6.6
>> 최고 온도: 2.0
>> 강수량:  0.1
[2000.2086]

# 이후에 생성된 모델 파일을 웹 서버의 model 폴더에 붙여넣기 하면 적용됩니다.
```
