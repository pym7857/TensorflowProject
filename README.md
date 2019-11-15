# Title
텐서플로우를 이용한 다변인 선형회귀를 이용한 가격예측 프로그램 
LSTM 딥러닝을 이용한 한달치 가격 예측

## 텐서플로우 소개 
```
설명
```

## LSTM 소개
```
설명
```

## Web Site
https://

## 서버 실행
```
# 깃 허브에서 소스코드를 다운로드 받습니다.
git clone https://github.com/pym7857/ ★ 이름 ★ .git

# 받은 프로젝트 폴더로 이동합니다.
cd ★프로젝트 이름★

# 플라스크 웹 서버 폴더로 이동합니다.
cd "Web"

# 웹 서버를 실행합니다.
python server.py
```

## 텐서플로우 데이터 학습 모델 생성
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

## 핵심사항
```
# offline_save.py: 다변인 선형회귀 모델 개발 & 데이터 저장 (model 폴더에 저장)
# user_input.py: 데이터 불러오기 & 사용자 입력

# Web 폴더는 model / static / templates로 나누어 구성 
# index.html에서 데이터 입력부분은 form 태그로 POST 방식으로 데이터 전송

# server.py: 플라스크(Flask)를 이용해 웹서버 연동 (port:5000)
```

<br>
<br>
