import pyupbit
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import ccxt #라이브러리 임포트 
import re
import time

#코인 이름 한글로 정리
krwcoin = ['비트코인(BTC-KRW)', '이더리움(ETH-KRW)', '네오(NEO-KRW)', '메탈(MTL-KRW)', '라이트코인(LTC-KRW)', '리플(XRP-KRW)', '이더리움 클래식(ETC-KRW)', '오미세고(OMG-KRW)', '스테이터스네트워크토큰(SNT-KRW)', '웨이브(WAVES-KRW)', '넴(XEM-KRW)', '퀸텀(QTUM-KRW)', '리스크(LSK-KRW)', '스팀(STEEM-KRW)', '스텔라루멘(XLM-KRW)', '아더(ARDR-KRW)', '아크(ARK-KRW)', '스토리지(STORJ-KRW)', '그로스톨코인(GRS-KRW)', '어거(REP-KRW)', '에이다(ADA-KRW)', '스팀달러(SBD-KRW)', '파워렛저(POWR-KRW)', '비트코인 골드(BTG-KRW)', '아이콘(ICX-KRW)', '이오스(EOS-KRW)', '트론(TRX-KRW)', '시아코인(SC-KRW)', '온톨로지(ONT-KRW)', '질리카(ZIL-KRW)', '폴리매쓰(POLY-KRW)', '제로엑스(ZRX-KRW)', '룸네트워크(LOOM-KRW)', '비트코인 캐시(BCH-KRW)', '베이직어텐션토큰(BAT-KRW)', '아이오에스티(IOST-KRW)', '리퍼리움(RFR-KRW)', '시빅(CVC-KRW)', '에브리피디아(IQ-KRW)', '아이오타(IOTA-KRW)', '메인프레임(MFT-KRW)', '온톨로지가스(ONG-KRW)', '가스(GAS-KRW)', '센티넬프로토콜(UPP-KRW)', '엘프(ELF-KRW)', '카이버네트워크(KNC-KRW)', '비트코인에스브이(BSV-KRW)', '쎄타토큰(THETA-KRW)', '쿼크체인(QKC-KRW)', '비트토렌트(BTT-KRW)', '모스(MOC-KRW)', '엔진(ENJ-KRW)', '쎄타퓨엘(TFUEL-KRW)', '디센트럴랜드(MANA-KRW)', '앵커(ANKR-KRW)', '아르고(AERGO-KRW)', '코스모스(ATOM-KRW)', '썬더토큰(TT-KRW)', '캐리프로토콜(CRE-KRW)', '무비블록(MBL-KRW)', '왁스(WAXP-KRW)', '헤데라(HBAR-KRW)', '메디블록(MED-KRW)', '밀크(MLK-KRW)', '에스티피(STPT-KRW)', '오브스(ORBS-KRW)', '비체인(VET-KRW)', '칠리즈(CHZ-KRW)', '스톰엑스(STMX-KRW)', '디카르고(DKA-KRW)', '하이브(HIVE-KRW)', '카바(KAVA-KRW)', '아하토큰(AHT-KRW)', '링크(LINK-KRW)', '테조스(XTZ-KRW)', '보라(BORA-KRW)', '저스트(JST-KRW)', '크로노스(CRO-KRW)', '톤(TON-KRW)', '스와이프(SXP-KRW)', '헌트(HUNT-KRW)', '플레이댑(PLA-KRW)', '폴카닷(DOT-KRW)', '세럼(SRM-KRW)', '엠블(MVL-KRW)', '스트라티스(STRAX-KRW)', '알파쿼크(AQT-KRW)', '골렘(GLM-KRW)', '썸씽(SSX-KRW)', '메타(META-KRW)', '피르마체인(FCT2-KRW)', '코박 토큰(CBK-KRW)', '샌드박스(SAND-KRW)', '휴먼스케이프(HUM-KRW)', '도지(DOGE-KRW)', '스트라이크(STRK-KRW)', '펀디엑스(PUNDIX-KRW)', '플로우(FLOW-KRW)', '던프로토콜(DAWN-KRW)', '엑시(AXS-KRW)', '스택스(STX-KRW)', '이캐시(XEC-KRW)', '솔라나(SOL-KRW)', '폴리곤(MATIC-KRW)', '누사이퍼(NU-KRW)', '에이브(AAVE-KRW)', '1인치(1INCH-KRW)', '알고랜드(ALGO-KRW)', '니어프로토콜(NEAR-KRW)', '위믹스(WEMIX-KRW)', '아발란체(AVAX-KRW)', '티(T-KRW)']
usdcoin = [  "비트코인(BTC-USDT)",
  "이더리움(ETH-USDT)",
  "비앤비(BNB-USDT)",
  "네오(NEO-USDT)",
  "라이트코인(LTC-USDT)",
  "퀀텀(QTUM-USDT)",
  "에이다(ADA-USDT)",
  "리플(XRP-USDT)",
  "이오스(EOS-USDT)",
  "트루usd(TUSD-USDT)",
  "아이오타(IOTA-USDT)",
  "스텔라루멘(XLM-USDT)",
  "온톨로지(ONT-USDT)",
  "트론(TRX-USDT)",
  "이더리움 클래식(ETC-USDT)",
  "아이콘(ICX-USDT)",
  "ven(VEN-USDT)",
  "널스(NULS-USDT)",
  "비체인(VET-USDT)",
  "팍소스스탠다드(PAX-USDT)",
  "비트코인 캐시(BCH-USDT)",
  "비트코인에스브이(BSV-USDT)",
  "스테이블(USDC-USDT)",
  "체인링크(LINK-USDT)",
  "웨이브(WAVES-USDT)",
  "비트토렌트(BTT-USDT)",
  "스테이블유에스디(USDS-USDT)",
  "온톨로지가스(ONG-USDT)",
  "홀로(HOT-USDT)",
  "질리카(ZIL-USDT)",
  "제로엑스(ZRX-USDT)",
  "페치(FET-USDT)",
  "베이직어텐션토큰(BAT-USDT)",
  "모네로(XMR-USDT)",
  "지캐시(ZEC-USDT)",
  "아이오에스티(IOST-USDT)",
  "셀러네트워크(CELR-USDT)",
  "대시(DASH-USDT)",
  "나노(NANO-USDT)",
  "오미세고(OMG-USDT)",
  "쎄타토큰(THETA-USDT)",
  "엔진(ENJ-USDT)",
  "미스릴(MITH-USDT)",
  "폴리곤(MATIC-USDT)",
  "코스모스(ATOM-USDT)",
  "쎄타퓨엘(TFUEL-USDT)",
  "하모니(ONE-USDT)",
  "팬텀(FTM-USDT)",
  "알고랜드(ALGO-USDT)",
  "USDSB(USDSB-USDT)",
  "기프토(GTO-USDT)",
  "엘론드(ERD-USDT)",
  "도지(DOGE-USDT)",
  "더스크네트워크(DUSK-USDT)",
  "앵커네트워크(ANKR-USDT)",
  "윙크(WIN-USDT)",
  "콘텐토스(COS-USDT)",
  "펀디엑스(NPXS-USDT)",
  "코코스(COCOS-USDT)",
  "메탈(MTL-USDT)",
  "토모체인(TOMO-USDT)",
  "PERL(PERL-USDT)",
  "덴트(DENT-USDT)",
  "메인프레임(MFT-USDT)",
  "KEY(KEY-USDT)",
  "스톰(STORM-USDT)",
  "도크(DOCK-USDT)",
  "완체인(WAN-USDT)",
  "펀페어(FUN-USDT)",
  "시빅(CVC-USDT)",
  "칠리즈(CHZ-USDT)",
  "밴드 프로토콜(BAND-USDT)",
  "BUSD(BUSD-USDT)",
  "빔(BEAM-USDT)",
  "테조스(XTZ-USDT)",
  "렌(REN-USDT)",
  "레이븐코인(RVN-USDT)",
  "에이치쉐어(HC-USDT)",
  "헤데라(HBAR-USDT)",
  "엔케이엔(NKN-USDT)",
  "스택스(STX-USDT)",
  "카바(KAVA-USDT)",
  "알파체인(ARPA-USDT)",
  "아이오텍스(IOTX-USDT)",
  "아이젝(RLC-USDT)",
  "MCO(MCO-USDT)",
  "코르텍스(CTXC-USDT)",
  "트로이(TROY-USDT)",
  "바이트토큰(VITE-USDT)",
  "에프티엑스토큰(FTT-USDT)",
  "EUR(EUR-USDT)",
  "오리진 프로토콜(OGN-USDT)",
  "드랩(DREP-USDT)",
  "BULL(BULL-USDT)",
  "BEAR(BEAR-USDT)",
  "ETHBULL(ETHBULL-USDT)",
  "ETHBEAR(ETHBEAR-USDT)",
  "토큰클럽(TCT-USDT)",
  "와지르엑스(WRX-USDT)",
  "비트셰어(BTS-USDT)",
  "리스크(LSK-USDT)",
  "뱅코르(BNT-USDT)",
  "엘티오 네트워크(LTO-USDT)",
  "EOSBULL(EOSBULL-USDT)",
  "EOSBEAR(EOSBEAR-USDT)",
  "XRPBULL(XRPBULL-USDT)",
  "XRPBEAR(XRPBEAR-USDT)",
  "스타트(STRAT-USDT)",
  "아이온(AION-USDT)",
  "무비블록(MBL-USDT)",
  "코티(COTI-USDT)",
  "BNBBULL(BNBBULL-USDT)",
  "BNBBEAR(BNBBEAR-USDT)",
  "에스티피(STPT-USDT)",
  "월튼체인(WTC-USDT)",
  "스트리머(DATA-USDT)",
  "지코인(XZC-USDT)",
  "솔라나(SOL-USDT)",
  "카르테시(CTSI-USDT)",
  "하이브(HIVE-USDT)",
  "크로미아(CHR-USDT)",
  "지엑스체인(GXS-USDT)",
  "아더(ARDR-USDT)",
  "에이브(LEND-USDT)",
  "미슈어러블데이타토큰(MDT-USDT)",
  "스톰엑스(STMX-USDT)",
  "카이버 네트워크(KNC-USDT)",
  "어거(REP-USDT)",
  "루프링(LRC-USDT)",
  "피네트워크(PNT-USDT)",
  "컴파운드(COMP-USDT)",
  "BKRW(BKRW-USDT)",
  "시아(SC-USDT)",
  "젠캐시(ZEN-USDT)",
  "신세틱스(SNX-USDT)",
  "비토르(VTHO-USDT)",
  "디지바이트(DGB-USDT)",
  "GBP(GBP-USDT)",
  "스와이프(SXP-USDT)",
  "메이커(MKR-USDT)",
  "다이(DAI-USDT)",
  "디크레드(DCR-USDT)",
  "스토리지(STORJ-USDT)",
  "디센트럴랜드(MANA-USDT)",
  "AUD(AUD-USDT)",
  "연파이낸스(YFI-USDT)",
  "발란서(BAL-USDT)",
  "블루젤(BLZ-USDT)",
  "아이리스넷(IRIS-USDT)",
  "코모도(KMD-USDT)",
  "저스트(JST-USDT)",
  "세럼(SRM-USDT)",
  "아라곤(ANT-USDT)",
  "커브(CRV-USDT)",
  "샌드박스(SAND-USDT)",
  "오션프로토콜(OCEAN-USDT)",
  "뉴메레르(NMR-USDT)",
  "폴카닷(DOT-USDT)",
  "루나(LUNA-USDT)",
  "리저브라이트(RSR-USDT)",
  "PAXG(PAXG-USDT)",
  "WNXM(WNXM-USDT)",
  "텔러(TRB-USDT)",
  "비지엑스(BZRX-USDT)",
  "스시스왑(SUSHI-USDT)",
  "디파이머니(YFII-USDT)",
  "쿠사마(KSM-USDT)",
  "엘론드(EGLD-USDT)",
  "디아(DIA-USDT)",
  "RUNE(RUNE-USDT)",
  "피오프로토콜(FIO-USDT)",
  "우마(UMA-USDT)",
  "벨라 프로토콜(BEL-USDT)",
  "윙(WING-USDT)",
  "유니스왑(UNI-USDT)",
  "뉴비트쉐어(NBS-USDT)",
  "오키드(OXT-USDT)",
  "썬(SUN-USDT)",
  "아발란체(AVAX-USDT)",
  "헬륨(HNT-USDT)",
  "플라밍고(FLM-USDT)",
  "오리온(ORN-USDT)",
  "유트러스트(UTK-USDT)",
  "비너스(XVS-USDT)",
  "알파(ALPHA-USDT)",
  "에이브(AAVE-USDT)",
  "니어프로토콜(NEAR-USDT)",
  "파일(FIL-USDT)",
  "인젝티브(INJ-USDT)",
  "오디우스(AUDIO-USDT)",
  "서틱(CTK-USDT)",
  "아크로폴리스(AKRO-USDT)",
  "엑시 인피니티(AXS-USDT)",
  "하드 프로토콜(HARD-USDT)",
  "디스트릭트0x(DNT-USDT)",
  "스트라티스(STRAX-USDT)",
  "유니파이(UNFI-USDT)",
  "오아시스 네트워크(ROSE-USDT)",
  "아바(AVA-USDT)",
  "넴(XEM-USDT)",
  "스케일네트워크(SKL-USDT)",
  "에스유에스디(SUSD-USDT)",
  "더그래프(GRT-USDT)",
  "유벤투스 팬 토큰(JUV-USDT)",
  "파리생제르맹(PSG-USDT)",
  "1인치(1INCH-USDT)",
  "리프(REEF-USDT)",
  "오쥐 팬 토큰(OG-USDT)",
  "아틀레티코 마드리드 팬 토큰(ATM-USDT)",
  "AS 로마 팬 토큰(ASR-USDT)",
  "셀로(CELO-USDT)",
  "리프(RIF-USDT)",
  "비트 코인 표준 해시 레이트 토큰(BTCST-USDT)",
  "트루파이(TRU-USDT)",
  "너보스(CKB-USDT)",
  "트러스트월렛(TWT-USDT)",
  "피로(FIRO-USDT)",
  "릿엔트리(LIT-USDT)",
  "세이프팔(SFP-USDT)",
  "도도(DODO-USDT)",
  "팬케이크 스왑(CAKE-USDT)",
  "AC밀란 팬 토큰(ACM-USDT)",
  "뱃저다오(BADGER-USDT)",
  "스타파이(FIS-USDT)",
  "만트라 다오(OM-USDT)",
  "말린(POND-USDT)",
  "디고(DEGO-USDT)",
  "마이네이버앨리스(ALICE-USDT)",
  "리니어(LINA-USDT)",
  "퍼페츄얼 프로토콜(PERP-USDT)",
  "램프(RAMP-USDT)",
  "콘플럭스(CFX-USDT)",
  "일립시스(EPS-USDT)",
  "큐브(AUTO-USDT)",
  "토코크립토(TKO-USDT)",
  "펀디엑스(PUNDIX-USDT)",
  "에일리언 월드(TLM-USDT)",
  "비트코인 골드(BTG-USDT)",
  "미러 프로토콜(MIR-USDT)",
  "FC 바르셀로나 팬 토큰(BAR-USDT)",
  "앰플포스 거버넌스 토큰(FORTH-USDT)",
  "베이커리스왑(BAKE-USDT)",
  "버거스왑(BURGER-USDT)",
  "스무스 러브 포션(SLP-USDT)",
  "시바이누(SHIB-USDT)",
  "인터넷 컴퓨터(ICP-USDT)",
  "알위브(AR-USDT)",
  "폴카스타터(POLS-USDT)",
  "엠덱스(MDX-USDT)",
  "마스크 네트워크(MASK-USDT)",
  "라이브피어(LPT-USDT)",
  "누사이퍼(NU-USDT)",
  "버지(XVG-USDT)",
  "오토마타(ATA-USDT)",
  "깃코인(GTC-USDT)",
  "토네이토 캐시(TORN-USDT)",
  "킵(KEEP-USDT)",
  "이더니티체인(ERN-USDT)",
  "클레이튼(KLAY-USDT)",
  "팔라 네트워크(PHA-USDT)",
  "본드(BOND-USDT)",
  "엔자임(MLN-USDT)",
  "딕시(DEXE-USDT)",
  "코인98(C98-USDT)",
  "클로버(CLV-USDT)",
  "퀀트 네트워크(QNT-USDT)",
  "플로우(FLOW-USDT)",
  "테라 버추어(TVK-USDT)",
  "미나 프로토콜(MINA-USDT)",
  "레이디움(RAY-USDT)",
  "하베스트(FARM-USDT)",
  "알파카(ALPACA-USDT)",
  "퀵스왑(QUICK-USDT)",
  "모박스(MBOX-USDT)",
  "포튜브(FOR-USDT)",
  "리퀘스트(REQ-USDT)",
  "아베고치(GHST-USDT)",
  "왁스(WAXP-USDT)",
  "트라이브(TRIBE-USDT)",
  "노시스(GNO-USDT)",
  "이캐시(XEC-USDT)",
  "엘프(ELF-USDT)",
  "디와이디엑스(DYDX-USDT)",
  "폴리매쓰(POLY-USDT)",
  "아이덱스(IDEX-USDT)",
  "VIDT 데이터링크(VIDT-USDT)",
  "USDP 스테이블코인(USDP-USDT)",
  "갈라(GALA-USDT)",
  "일루비움(ILV-USDT)",
  "일드 길드 게임즈(YGG-USDT)",
  "시스(SYS-USDT)",
  "디포스(DF-USDT)",
  "본피다(FIDA-USDT)",
  "프론티어(FRONT-USDT)",
  "파워풀(CVP-USDT)",
  "어드벤쳐골드(AGLD-USDT)",
  "레디클(RAD-USDT)",
  "베타(BETA-USDT)",
  "슈퍼레어(RARE-USDT)",
  "라치오(LAZIO-USDT)",
  "트랜체스(CHESS-USDT)",
  "애드엑스(ADX-USDT)",
  "바운스토큰(AUCTION-USDT)",
  "달라니아(DAR-USDT)",
  "바이너리X(BNX-USDT)",
  "라리 거버넌스 토큰(RGT-USDT)",
  "문리버(MOVR-USDT)",
  "시티(CITY-USDT)",
  "이더리움네임서비스(ENS-USDT)",
  "Keep3rV1(KP3R-USDT)",
  "QI스왑(QI-USDT)",
  "FC 포르투 팬 토큰(PORTO-USDT)",
  "파워렛저(POWR-USDT)",
  "보이저(VGX-USDT)",
  "자스미(JASMY-USDT)",
  "에이엠피(AMP-USDT)",
  "플레이댑(PLA-USDT)",
  "불칸 포지드(PYR-USDT)",
  "렌더(RNDR-USDT)",
  "알케믹스(ALCX-USDT)",
  "산토스 FC 팬 토큰(SANTOS-USDT)",
  "메리트 서클(MC-USDT)",
  "애니스왑(ANY-USDT)",
  "바이코노미(BICO-USDT)",
  "플럭스(FLUX-USDT)",
  "프락스 쉐어(FXS-USDT)",
  "복시(VOXEL-USDT)",
  "하이스트리트(HIGH-USDT)",
  "컨벡스(CVX-USDT)",
  "컨스티튜션 DAO(PEOPLE-USDT)",
  "OOKI 프로토콜(OOKI-USDT)",
  "스펠(SPELL-USDT)",
  "테라(UST-USDT)",
  "조(JOE-USDT)",
  "알케미 페이(ACH-USDT)",
  "이뮤터블X(IMX-USDT)",
  "문빔(GLMR-USDT)",
  "리그 오브 킹덤(LOKA-USDT)",
  "시크릿(SCRT-USDT)",
  "에이피아이3(API3-USDT)",
  "비트토렌트체인(BTTC-USDT)",
  "아칼라(ACA-USDT)",
  "앵커 프로토콜(ANC-USDT)",
  "제노(XNO-USDT)",
  "우네트워크(WOO-USDT)",
  "알파인(ALPINE-USDT)",
  "티(T-USDT)",
  "아스타(ASTR-USDT)",
  "누비츠(NBT-USDT)",
  "스태픈(GMT-USDT)",
  "카데나(KDA-USDT)",
  "에이프(APE-USDT)",
  "비스왑(BSW-USDT)"]

#현재 시간 불러오는 함수
def time_format():
    try:
        now = datetime.datetime.now()
        nowDATE=now.strftime('%Y-%m-%d')
        return nowDATE
    except:
        print("알림 : <현재 시간을 불러오는 중 오류가 발생했습니다.")

#timestamp로 변환
def to_mstimestamp(stamp):
    stamp = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
    stamp = datetime.datetime.timestamp(str)
    stamp = int(stamp) * 1000
    return stamp

#USDT 종목 생성
def usd_made():
    exchange = ccxt.binance() #바이낸스 객체 생성
    exchange.fetch_tickers() #티커의 각종 정보를 딕셔너리로 불러옴 
    ticker = list(exchange.fetch_tickers().keys()) #딕셔너리의 key값만 뽑아내서 리스트로 만들
    USDT_ticker = [] 
    p = re.compile(r'\w+[/]USDT')
    for i in ticker:
        if p.match(i) and 'UP' not in i and 'DOWN' not in i: #레버리지토큰 필터링을 위함
            USDT_ticker.append(i)
    path="/nomadcoders/boot/DB/usdcode.txt"
    file = open(path, 'w')
    for i in USDT_ticker:
        file.write(i)
        file.write("\n")
    file.close()

def usd_connect(coinname):
    path="/nomadcoders/boot/DB/usdcode.txt"
    file = open(path, 'r')
    USDT_ticker = file.read().splitlines()
    USDT = []
    rate=""
    for i in USDT_ticker:
        USDT.append(i)
    file.close()
    TICKER = ""
    for i in range (len(usdcoin)):
        if(coinname == usdcoin[i]):
            TICKER = USDT[i]
    return TICKER,rate


#df 생성
def get_df_binance(ticker,time_interval):
    exchange = ccxt.binance() #바이낸스 객체 생성
    exchange.fetch_tickers() #티커의 각종 정보를 딕셔너리로 불러옴 
    #start_date = start_date + " 00:00:00"
    #start_date = to_mstimestamp(start_date)
    data = exchange.fetch_ohlcv(ticker,time_interval) #값이 리스트로 반환된다
    df = pd.DataFrame(data) #데이터프레임으로 만든다
    df.columns = (['date','open','high','low','close','volume']) #컬럼 지정 
    #여기 수정해야함
    def parse_dates(ts):
        return datetime.datetime.fromtimestamp(ts/1000.0) #타임스탬프를 시간형식으로 전환 
    df['date'] = df['date'].apply(parse_dates) #Date컬럼에 적용 
    print(df)
    return df #데이터프레임 반환

#라이브러리 연결
def coin_connect(moneyvalue,coinname,date):
    #코인 리스트 가져오기(pyupbit)
    nowDATE = time_format()
    coinlist= pyupbit.get_tickers(fiat=moneyvalue)
    #한글로 입력 받은 코인 이름을 영어로 변경
    coinitem=""
    for i in range(len(krwcoin)):
        if(coinname ==krwcoin[i]):
            coinitem = coinlist[i]
        else:
            pass
    #df에 해당 코인의 데이터를 저장
    df = pyupbit.get_ohlcv(coinitem,interval="day",to = nowDATE,count = date)
    df = df[['open','close']]
    print(df)
    rate = pyupbit.get_current_price([coinitem])
    return df, rate

#코인 가격 리스트에 저장
def coin_rate(moneyvalue,coinitem,df,rate):
    nowDATE = time_format()
    #오픈 가격만 뒤에서 2줄만 가져옴
    #df_open = df[['open']]
    #df_open = df_open[-2:]
    df_close = df[['close']]
    df_close = df_close[-2:]
    #해당 값을 두 개의 변수에 저장
    firstrate = df_close['close'].values[0]
    if(moneyvalue=="KRW"):
        lastrate = rate
    elif(moneyvalue=="USD"):
        lastrate = df_close['close'].values[1]
    coinrate =[]
    #날짜와 코인 이름, 현재 가격을 추가
    coinrate.append(nowDATE)
    coinrate.append(coinitem)
    if(int(firstrate) > 100):
        gap = "{0:,.0f}".format(lastrate-firstrate)
    elif(int(firstrate)<1):
        gap = "{0:,.3f}".format(lastrate-firstrate)
    else:
        gap = "{0:,.2f}".format(lastrate-firstrate)
    if(moneyvalue == "KRW"):
        #변동 계산 및 추가
        if(int(lastrate) > 100):
            coinrate.append("{0:,.0f}".format(lastrate)+"원")
        elif(int(lastrate)<1):
            coinrate.append("{0:,.3f}".format(lastrate)+"원")
        else:
            coinrate.append("{0:,.2f}".format(lastrate)+"원")
        coinrate.append(gap+"원")
    elif(moneyvalue == "USD"):
         #변동 계산 및 추가
        if(int(firstrate)> 100):
            coinrate.append("$"+"{0:,.0f}".format(lastrate))
        elif(int(firstrate<1)):
            coinrate.append("$"+"{0:,.3f}".format(lastrate))
        else:
            coinrate.append("$"+"{0:,.2f}".format(lastrate))
        coinrate.append("$"+gap)
    #수익률 계산 및 추가
    profit = "{:.2f}".format((lastrate-firstrate)/firstrate*100)
    coinrate.append("{0:,}".format(float(profit))+"%")
    return coinrate

#기본 차트 만들기
def basic_chart(df,Name,moneyvalue):
    #현재 인덱스인 값을 date라는 값으로 데이터프레임에 추가
    if(moneyvalue == "KRW"):
        df['date'] = df.index
    else:
        pass
    #차트크기
    plt.figure(figsize=(13,4))
    #차트 값 (x랑 y에 어떤 값 넣을지)
    plt.plot(df['date'],df['open'])
    #차트 행마다 이름
    plt.xlabel('date')
    plt.ylabel('close')
    src="./static/assets/img/"
    plt.savefig(src+Name +".png")
    
#내가 잘 모르는 내용
def real_chart(df,company):
    #고급 차트 생성
    fig = px.line(df, x='date', y='open', title='{}의 시가(Open) '.format(company))

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.write_html("./templates/chart.html")

    