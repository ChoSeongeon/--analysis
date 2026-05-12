# --analysis
프롬프트 링크: https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221cFJ_1IjeSHcNlT8AxphN4b257hwaLIaA%22%5D,%22action%22:%22open%22,%22userId%22:%22102732912304129699895%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing

<데이터>
1) 입장객.csv : 예술의전당에서 개최되는 다양한 공연 및 전시의 관람객 수를 시간/장소별로 수집한 데이터
   
   CREATE TABLE 입장객 (
    작품명             TEXT NOT NULL,
    공간명             TEXT,          
    구분              TEXT,          
    기획사             TEXT,          
    일자              TEXT,         
    시간              TEXT,
    무료              INTEGER DEFAULT 0, 
    유료              INTEGER DEFAULT 0, 
    합계              INTEGER DEFAULT 0 
    PRIMARY KEY (작품명, 일자, 시간) );

2) 회원.csv : 예술의전당의 나이, 성별에 따른 회원수(멤버십) 통계 데이터
   
   CREATE TABLE 회원 (
    아이디             INTEGER PRIMARY KEY,
    나이              INTEGER,             
    성별              TEXT,               
    전체              INTEGER DEFAULT 0,  
    골드              INTEGER DEFAULT 0,   
    블루              INTEGER DEFAULT 0,   
    그린              INTEGER DEFAULT 0,   
    무료              INTEGER DEFAULT 0,   
    기타              INTEGER DEFAULT 0 );

3) 안내.csv : 예술의전당에서 진행된 공연과 전시 관련 정보
   
   CREATE TABLE 안내 (
    ID         INTEGER PRIMARY KEY
    제목        TEXT,
    공연시작일   TEXT,
    공연종료일   TEXT,
    장르        TEXT,
    대관기업명   TEXT,
    구분        TEXT,
    공연장      TEXT,
    상세링크     TEXT );

<시각화 결과>
1) 예술의 전당 회원의 성별 비율 가로 막대 그래프
 - 회원 성별 비중을 통해 마케팅 타겟 설정 용이
 - 여성과 남성의 비율에 큰 차이 없음 -> 모든 성별이 즐길 수 있는 공연 기획

2) 예술의 전당 회원의 연령대 분포 세로 막대 그래프
 - 주연령대 확인하여 타겟 설정 후 공연 프로그램 기획 용이
 - 미취학아동 회원이 다른 연령대에 비해 비율이 낮은 편이므로 10대 미만 아이들을 위한 프로그램 기획하여
   해당 연령층 회원을 추가 확보할 수 있다.

3) 2025년 관객수 TOP10 작품
 - 2025년 예술의 전당에서 진행한 공연 중 가장 흥행한 작품과 장르를 표시한 가로 막대 그래프
 - 뮤지컬 '웃는 남자'가 압도적인 흥행을 하였고 연극 '셰익스피어 인 러브', 뮤지컬 '시라노'가 뒤를 따른다. 
   상위권 작품의 흥행 요인을 분석하여 2026년 공연 흥행 전략에 반영해 볼 수 있다.

4) 2025년 공연 입장객 TOP 100 작품의 장르 비중
 - 2025년에 진행한 입장객 TOP 100개 작품 중 특정 장르가 차지하는 비중
 - 3번 결과에서 TOP3 작품의 장르는 뮤지컬과 연극이었다. 해당 결과만으로는 인기있는 공연 장르가 뮤지컬과 연극이라고
   단정지을 수 없기에 장르를 따로 조사하였다.
 - 관객들이 선호하는 장르는 클래식, 오페라, 발레이다. 관객들의 선호 장르 공연 횟수를 공연 라인업에 반영한다.






