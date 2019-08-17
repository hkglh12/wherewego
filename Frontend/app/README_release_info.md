## First Relase

 **Ver1.apk변경점**

 ### Near Me section
  - Location Manager의 추가 
  - 위도, 경도 단위로 받아오는 메서드 추가

    -(2019.08.10)

 
 **Ver1.00A.apk 변경점**
  - Android 위험권한의 Runtime 요청 추가 : ACCESS_FINE_LOCATION


 **Ver1.00B.apk 변경점**
  - ToggleButton text set.
  - 문제점 : GPS Able이어도 GPS Provider가 False였던 부분
    - 해결책 : 배터리절전모드일경우 GPS Provider를 GPS로 사용하지 않음.
    - 해결책 : 배터리 절전모드를 푸는수밖에 없음. 구글 API 정책임

      - (2019.08.11)

  **Ver1.00C.apk 변경점**
   - Google map API import succcess
