# 실습
## API와 웹 데이터 활용하기

### API란 무엇인가?
- API(Application Programming Interface)는 서로 다른 프로그램이 데이터를 주고받을 수 있게 해주는 방법
- 웹 API를 통해 실시간 날씨, 뉴스, 주식 정보 등을 가져올 수 있음
- 우리가 사용할 `requests` 라이브러리로 쉽게 API 호출 가능

### requests 라이브러리 설치 및 기본 사용법
#### 라이브러리 설치
```python
# 구글 코랩에서는 이미 설치되어 있음
import requests
import json
```

#### 기본 GET 요청
```python
# 간단한 API 호출 예시
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200이면 성공
print(response.json())       # JSON 데이터를 딕셔너리로 변환
```

### try-except로 안전한 API 호출
#### 기본 예외 처리
```python
import requests

def safe_api_call(url):
    """안전한 API 호출 함수"""
    try:
        response = requests.get(url, timeout=5)  # 5초 타임아웃
        response.raise_for_status()  # HTTP 에러 시 예외 발생
        return response.json()
    except requests.exceptions.Timeout:
        print("요청 시간이 초과되었습니다.")
        return None
    except requests.exceptions.ConnectionError:
        print("인터넷 연결을 확인해주세요.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 에러 발생: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
        return None
    except json.JSONDecodeError:
        print("응답을 JSON으로 변환할 수 없습니다.")
        return None

# 사용 예시
data = safe_api_call("https://jsonplaceholder.typicode.com/posts/1")
if data:
    print(f"제목: {data['title']}")
else:
    print("데이터를 가져올 수 없습니다.")
```

### 실습 1: 가짜 데이터로 연습하기 (JSONPlaceholder)
- https://jsonplaceholder.typicode.com/ 사이트에서는 JSON API call을 테스트하기 위한 더미 데이터를 제공

#### 게시글 목록 가져오기
```python
def get_posts():
    """게시글 목록을 가져오는 함수"""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()

        print("=== 게시글 목록 ===")
        for post in posts[:5]:  # 처음 5개만 출력
            print(f"ID: {post['id']}")
            print(f"제목: {post['title']}")
            print(f"내용: {post['body'][:50]}...")
            print("-" * 30)

    except Exception as e:
        print(f"게시글을 가져오는 중 오류 발생: {e}")

get_posts()
```

#### 사용자 정보 가져오기
```python
def get_user_info(user_id):
    """특정 사용자 정보를 가져오는 함수"""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            print("사용자를 찾을 수 없습니다.")
            return

        response.raise_for_status()
        user = response.json()

        print("=== 사용자 정보 ===")
        print(f"이름: {user['name']}")
        print(f"이메일: {user['email']}")
        print(f"웹사이트: {user['website']}")
        print(f"회사: {user['company']['name']}")

    except Exception as e:
        print(f"사용자 정보를 가져오는 중 오류 발생: {e}")

# 사용 예시
get_user_info(1)
```

### 실습 2: 날씨 정보 가져오기 (OpenWeatherMap)
- [OpenWeatherMap](https://openweathermap.org/api)
    - Current Weather Data, Daily Forecast 8 days 등 다양한 정보를 제공
    - Price 정보: https://openweathermap.org/full-price#current
    - (API 서비스 주체가) API를 누가 사용하는지 추적하기 위하여 API 키가 필요
- API 키 관리 방법
    - OpenWeatherMap 에 가입한다.
    - 계정 정보의 My API Keys 에 들어가서 API 키를 얻는다.
    - 환경변수로 API 키를 저장한다.
        - Linux/Mac의 경우
            ```shell
                export WORLD_WEATHER_API_KEY="actual api key"
            ```
            ```python
                import os
                api_key = os.environ.get('WORLD_WEATHER_API_KEY')
            ```
        - Colab의 경우
            - 왼쪽의 열쇠 모양 (보안 비밀) 버튼을 눌러 적당한 이름으로 API 키를 등록한다. (ex., WORLD_WEATHER_API_KEY)
            - 노트북 액세스를 열어준다.
            ```python
                from google.colab import userdata
                userdata.get('WORLD_WEATHER_API_KEY')
            ```

#### API 키 설정 및 기본 호출
```python
import os
from google.colab import userdata

def get_weather(city_name, api_key):
    """도시별 날씨 정보를 가져오는 함수"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # 요청 매개변수
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # 섭씨 온도
        'lang': 'kr'        # 한국어
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)

        if response.status_code == 401:
            print("API 키가 올바르지 않습니다.")
            return
        elif response.status_code == 404:
            print("도시를 찾을 수 없습니다.")
            return

        response.raise_for_status()
        weather_data = response.json()

        # 날씨 정보 출력
        print(f"=== {weather_data['name']} 날씨 ===")
        print(f"날씨: {weather_data['weather'][0]['description']}")
        print(f"온도: {weather_data['main']['temp']}°C")
        print(f"체감온도: {weather_data['main']['feels_like']}°C")
        print(f"습도: {weather_data['main']['humidity']}%")
        print(f"풍속: {weather_data['wind']['speed']} m/s")

        return weather_data

    except requests.exceptions.Timeout:
        print("요청 시간이 초과되었습니다. 나중에 다시 시도해주세요.")
    except requests.exceptions.ConnectionError:
        print("인터넷 연결을 확인해주세요.")
    except Exception as e:
        print(f"날씨 정보를 가져오는 중 오류 발생: {e}")

# 사용 예시 (실제 API 키 필요)
api_key = userdata.get('WORLD_WEATHER_API_KEY')
get_weather("Seoul", api_key)
```

### 실습 3: 여러 도시 날씨 비교하기
```python
def compare_cities_weather(cities, api_key):
    """여러 도시의 날씨를 비교하는 함수"""
    weather_data = []

    for city in cities:
        print(f"{city} 날씨 정보를 가져오는 중...")

        try:
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric',
                'lang': 'kr'
            }

            response = requests.get(base_url, params=params, timeout=5)
            response.raise_for_status()

            data = response.json()
            weather_info = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }
            weather_data.append(weather_info)

        except Exception as e:
            print(f"{city} 날씨 정보 가져오기 실패: {e}")
            continue

    # 결과 출력
    if weather_data:
        print("\n=== 도시별 날씨 비교 ===")
        for weather in weather_data:
            print(f"{weather['city']}: {weather['temp']}°C, {weather['description']}")

        # 가장 더운 도시 찾기
        hottest = max(weather_data, key=lambda x: x['temp'])
        print(f"\n가장 더운 도시: {hottest['city']} ({hottest['temp']}°C)")

# 사용 예시
cities = ["Seoul", "Tokyo", "New York", "London", "Paris"]
compare_cities_weather(cities, api_key)
```

### 실습 4: 한국 공공데이터 활용하기
- 여러 사이트가 있지만, 여기에서 https://www.data.go.kr/ 를 사용한다.
- 사이트에 접속하여 원하는 API를 검색하면 어떤 API가 제공되는지 확인할 수 있다.
    - 예: 기상청 -> 오픈 API를 클릭하면 "기상청_단기예보 ((구)_동네예보) 조회서비스" 등이 나온다.
        - 사용하고 싶은 API를 선택하여 활용신청을 해야 API를 쓸 수 있다.
        - 마이페이지 -> 활용신청 현황에서 해당 API 상세 페이지로 들어가면 일반 인증키를 얻을 수 있다.
        - ...근데 지금은 API가 작동하지 않는다! 다른 예시!

#### 네이버 지도 / 지역 검색 API
- A와 B가 약속 장소를 정하려고 한다. 약속 장소는 두 사람의 출발지에서 동일한 거리에 있는 곳으로 정하고 싶다.
- 프로그램 순서
    1. A/B 지오코딩: NAVER Cloud Maps의 Geocoding API로 주소->위경도 변환.
    2. 중간지점 계산: 하버사인/구면중점으로 위경도 산출(앱 내부 계산).
    3. 중간지점 역지오코딩: 중간지점 위경도를 행정구역(시/구/동)으로 변환.
    4. 장소 후보 가져오기: 네이버 검색>지역(Local) 오픈API는 키워드 검색(API 파라미터는 query, display, start, sort만). 좌표/반경 파라미터는 없지만, 행정구역명을 포함한 키워드(예: 역삼동 카페, 강남구 식당)로 후보를 받아옵니다. 응답에는 좌표(mapx/mapy, WGS84)가 포함됩니다.
    5. 반경·거리 정렬은 앱에서: Local API 응답 좌표를 중간지점과의 거리로 필터링/정렬하면 “주변 카페/식당 리스트업”이 됩니다.
- 필요한 API 키
    - 네이버 클라우드 콘솔: https://console.ncloud.com/maps/application
        - Geocoding / Reverse Geocoding 신청
        - NCP_CLIENT_ID: 네이버 클라우드 지도 클라이언트 ID
        - NCP_CLIENT_SECRET: 네이버 클라우드 지도 시크릿 키
    - 네이버 지역 검색: https://developers.naver.com/apps/#/list
        - 검색 API 신청
        - NAVER_OPENAPI_ID: 네이버 오픈 API 클라이언트 ID
        - NAVER_OPENAPI_SECRET: 네이버 오픈 API 시크릿 키


```python
import math, requests
from math import radians, degrees, sin, cos, atan2, sqrt
from google.colab import userdata

# --- 설정 ---
NCP_CLIENT_ID = userdata.get('NCP_CLIENT_ID')
NCP_CLIENT_SECRET = userdata.get('NCP_CLIENT_SECRET')
NAVER_OPENAPI_ID = userdata.get('NAVER_OPENAPI_ID')
NAVER_OPENAPI_SECRET = userdata.get('NAVER_OPENAPI_SECRET')

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    a = sin(radians(lat2-lat1)/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(radians(lon2-lon1)/2)**2
    return 2*R*atan2(sqrt(a), sqrt(1-a))

def midpoint(lat1, lon1, lat2, lon2):
    pi1, lambda1, pi2, lambda2 = map(radians,[lat1,lon1,lat2,lon2])
    Bx = cos(pi2) * cos(lambda2-lambda1)
    By = cos(pi2) * sin(lambda2-lambda1)
    x = cos(pi1) + Bx
    y = By
    z = sin(pi1) + sin(pi2)
    return degrees(atan2(z, sqrt(x*x+y*y))), degrees(lambda1 + atan2(y, x))

def geocode(addr):
    url = "https://maps.apigw.ntruss.com/map-geocode/v2/geocode"
    try:
        r = requests.get(
            url,
            params={"query": addr},
            headers={
                "X-NCP-APIGW-API-KEY-ID": NCP_CLIENT_ID,
                "X-NCP-APIGW-API-KEY": NCP_CLIENT_SECRET
            },
            timeout=15
        )
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        print(f"[geocode] 요청 실패: {e}")
        return None
    except ValueError:
        print("[geocode] JSON 파싱 실패")
        return None

    items = data.get("addresses", [])
    if not items:
        print(f"[geocode] 결과 없음: {addr}")
        return None

    it = items[0]
    try:
        return float(it["y"]), float(it["x"])  # lat, lon
    except (KeyError, ValueError) as e:
        print(f"[geocode] 좌표 변환 실패: {e}")
        return None

def reverse_geocode(lat, lon):
    url = "https://maps.apigw.ntruss.com/map-reversegeocode/v2/gc"
    params = {"coords": f"{lon},{lat}", "orders": "legalcode,admcode", "output": "json"}
    try:
        r = requests.get(
            url,
            params=params,
            headers={
                "X-NCP-APIGW-API-KEY-ID": NCP_CLIENT_ID,
                "X-NCP-APIGW-API-KEY": NCP_CLIENT_SECRET
            },
            timeout=15
        )
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        print(f"[reverse_geocode] 요청 실패: {e}")
        return ""
    except ValueError:
        print("[reverse_geocode] JSON 파싱 실패")
        return ""

    res = data.get("results", [])
    if not res:
        return ""
    try:
        # 예: "서울특별시 강남구 역삼동"
        return " ".join([a["name"] for a in res[0]["region"].values() if isinstance(a, dict) and "name" in a])
    except Exception:
        return ""

def local_search(query, display=30, start=1, sort="random"):
    url = "https://openapi.naver.com/v1/search/local.json"
    try:
        r = requests.get(
            url,
            params={"query": query, "display": display, "start": start, "sort": sort},
            headers={
                "X-Naver-Client-Id": NAVER_OPENAPI_ID,
                "X-Naver-Client-Secret": NAVER_OPENAPI_SECRET
            },
            timeout=15
        )
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        print(f"[local_search] 요청 실패({query}): {e}")
        return []
    except ValueError:
        print(f"[local_search] JSON 파싱 실패({query})")
        return []

    return data.get("items", [])
```

```python
for k, v in {
    "NCP_CLIENT_ID": NCP_CLIENT_ID,
    "NCP_CLIENT_SECRET": NCP_CLIENT_SECRET,
    "NAVER_OPENAPI_ID": NAVER_OPENAPI_ID,
    "NAVER_OPENAPI_SECRET": NAVER_OPENAPI_SECRET
}.items():
    if not v:
        print(f"[경고] {k}가 설정되지 않았습니다. userdata에 저장했는지 확인하세요.")
```

```python
A = geocode("중구 한강대로 405")
B = geocode("서초구 서초대로73길 7")

if not A or not B:
    raise RuntimeError("A/B 지오코딩 실패 – 주소를 확인하거나 키 설정을 점검하세요.")

mid_lat, mid_lon = midpoint(*A, *B)
region = reverse_geocode(mid_lat, mid_lon) or ""   # 예: "서울특별시 강남구 역삼동"

print(f'중간 지역: {region} (lat={mid_lat}, lon={mid_lon})')

items = local_search(region.split()[-1] + " 카페", display=30) + local_search(region.split()[-1] + " 식당", display=30)

# Local API 좌표(mapx, mapy) 변환 + 개별 아이템 예외 방어
cands = []
for it in items:
    try:
        lat = float(it.get("mapy")) / 10000000
        lon = float(it.get("mapx")) / 10000000

        if math.isnan(lat) or math.isnan(lon):
            continue

        dist = haversine(mid_lat, mid_lon, lat, lon)
        addr = it.get("addresses", {}).get("roadAddress") or it.get("address") or ""
        name = it.get("title", "").replace("<b>", "").replace("</b>", "")
        cands.append({
            "name": name,
            "addr": addr,
            "lat": lat,
            "lon": lon,
            "dist_m": dist
        })
    except Exception as e:
        # 개별 아이템 문제는 전체 흐름 막지 않고 스킵
        print(f"[items] 스킵: {e}")
        continue

# 반경 1500m 이내 + 거리 오름차순
nearby = sorted([c for c in cands if c["dist_m"] <= 1500], key=lambda x: x["dist_m"])[:20]
nearby[:5]

```

### API 사용 시 주의사항
#### 1. API 키 보안
```python
# 나쁜 예시 - 코드에 직접 하드코딩
api_key = "12345abcdef"

# 좋은 예시 - 환경 변수 사용
import os
api_key = os.getenv('WEATHER_API_KEY')

if not api_key:
    print("API 키가 설정되지 않았습니다.")
    exit()
```

#### 2. 요청 제한 준수
- 너무 잦은 API call은 정책에 따라서 제한될 수 있다.
- time.sleep() 함수를 사용하면 초 단위로 프로그램을 멈추게 만들 수 있다.
```python
import time

def rate_limited_requests(urls, delay=1):
    """요청 제한을 지키면서 여러 API 호출"""
    results = []

    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            results.append(response.json())

            # 마지막 요청이 아닌 경우 대기
            if i < len(urls) - 1:
                time.sleep(delay)

        except Exception as e:
            print(f"요청 실패: {e}")
            results.append(None)

    return results
```

#### 3. 응답 데이터 검증
```python
def validate_weather_data(data):
    """날씨 데이터 유효성 검사"""
    required_fields = ['main', 'weather', 'name']

    for field in required_fields:
        if field not in data:
            raise ValueError(f"필수 필드 '{field}'가 없습니다.")

    if 'temp' not in data['main']:
        raise ValueError("온도 정보가 없습니다.")

    return True

# 사용 예시
try:
    weather_data = get_weather("Seoul", api_key)
    if weather_data and validate_weather_data(weather_data):
        print("유효한 날씨 데이터입니다.")
except ValueError as e:
    print(f"데이터 검증 실패: {e}")
```

## 과제
### API 활용 프로젝트
data.go.kr 같은 API 제공 서비스를 찾아서 그것을 이용하는 코드 작성해보기

#### 기본 요구사항
- try-except 문을 사용한 예외 처리
- 최소 2개 이상의 API 엔드포인트 사용

#### 추가 도전 과제
- 데이터 시각화 (matplotlib 활용)
- 클래스를 활용한 구조화된 코드
