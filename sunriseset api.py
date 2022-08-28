from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
url = 'http://apis.data.go.kr/1360000/BeachInfoservice/getSunInfoBeach'
service_key ='K5fygs3Ao38zhEsyxA2qi4TnFk1O6Q4Rpwok1XdloMNXSfLFOf1VNbuUV7zKFSIZZvgnFw8Iz2cCqzO0Eyvoyw=='
date = '20220828'
#날짜 '2022' : 연도, '0828' : 날짜
beach = '188'
#해수욕장 번호는 엑셀 데이터 참고
queryParams = '?' + urlencode({quote_plus('ServiceKey') : service_key, quote_plus('numOfRows') : '1', quote_plus('pageNo') : '10', quote_plus('dataType') : 'JSON', quote_plus('Base_date') : date,  quote_plus('beach_num') : beach})
response = urlopen(url + queryParams)
json_api = response.read().decode("utf-8")
print (json_api)

#< respond >
#sunrise : 일출, sunset : 일몰