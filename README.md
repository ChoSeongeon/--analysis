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
    
