from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
url = 'https://www.khoa.go.kr/api/oceangrid/beach/search.do'
ServiceKey ='J17oJtuWp5DrMImonXgIsw=='
beach = 'BCH001'
#beach 코드는 엑셀 참고
queryParams = '?' + urlencode({quote_plus('ServiceKey') : ServiceKey, quote_plus('BeachCode') : beach , quote_plus('ResultType') : 'json'})
response = urlopen(url + queryParams)
json_api = response.read().decode("utf-8")
print (json_api)

# water_temp : 수온
# wave_height : 파고
# wind_speed : 풍속
# wind_direct : 풍향
# obs_time : 측정 시간
# beach_name : 해수욕장 이름
