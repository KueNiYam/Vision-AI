Vision-AI  
=======================

# 1. 설명  
캡스톤 프로젝트의 본격적인 개발에 앞서, **Google Vision API**의 인식이 저희가 실제로 이용할 수 있는 기술인지를 테스트하는 소스 코드입니다.  

-----------------------  
# 2. 구성
2.1과 2.2는 **서버/클라이언트 관계**의 상호작용적인 소스 코드 패키지이며, 2.3은 별개의 테스트 코드입니다.  

## 2.1. server_test
서버 측 소스 코드 패키지입니다.  

### 2.1.1. server.py  
- 서버 측 실행 파일입니다.  
- http 요청을 받으면 표정 인식에 대한 데이터를 반환해줍니다.

### 2.1.2. vision_AI.py  
- 표정 인식 처리 관련 모듈입니다.

## 2.2. request_test
클라이언트 측 소스 코드 패키지입니다.

### 2.2.1. request_try.py  
- 클라이언트 측 실행 파일입니다.
- 테스트를 위하여 시간이 많이 소요되는 http 요청을 **thread**를 이용하여 여러 번 반복합니다.  

## 2.3. simple_test
단순히 사진 촬영부터 표정 인식까지 수행하는 소스 코드의 패키지입니다.  
실행 순서는 main1.py -> main2.py 입니다.

### 2.3.1. main1.py  
- 웹캠을 이용하여 사진을 촬영하는 소스 코드입니다.  
- 조작 방법은 다음과 같습니다.  

      Spacebar - 촬영
      key 'q'  - 종료

### 2.3.2. main2.py  
- Google Vision API의 로컬 이미지 표정 인식을 사용하는 코드입니다.  
- 반환 받은 감정을 데이터로 그대로 출력합니다.

-----------------------  
# 3. 결론  
테스트 결과 모두 사용 가능하다고 결론 지었습니다.  
개별 수행 시간은 1\~2초 정도로 길지만, 100회를 동시에 요청했을 시 처리되는 시간은 7\~8초 정도 걸립니다.

-----------------------
