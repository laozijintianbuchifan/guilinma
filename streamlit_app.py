import requests
import json
import streamlit as st
import time

st.write(time.time())
url = "https://m.ctrip.com/restapi/soa2/19728/fuzzySearch?_fxpcqlniredt=09031163218327913389&x-traceID=09031163218327913389-1719051584090-2667907"

payload = json.dumps({
  "tt": 1,
  "source": "online_map",
  "st": 18,
  "segments": [
    {
      "dcs": [
        {
          "ct": 1,
          "code": "BJS",
          "name": "北京"
        }
      ],
      "acs": [
        {
          "ct": 3,
          "code": "DOMESTIC_ALL",
          "name": "全中国"
        }
      ],
      "dow": [],
      "sr": None,
      "drl": [
        {
          "begin": "2024-6-22",
          "end": "2024-7-22"
        }
      ],
      "ddate": None
    }
  ],
  "filters": None,
  "head": {
    "cid": "09031163218327913389",
    "ctok": "",
    "cver": "1.0",
    "lang": "01",
    "sid": "8888",
    "syscode": "999",
    "auth": "",
    "xsid": "",
    "extension": []
  }
})
headers = {
  'accept': '*/*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'content-type': 'application/json',
  'cookie': 'UBT_VID=1718941212311.ffa662NVl7RG; GUID=09031163218327913389; _RSG=mXqkK4s_Mk4DOwlbpapCHA; _RDG=2824d64ab4e07e225534302efbfc58682a; _RGUID=4b96ff61-14bb-4870-a44c-ce4ce5bfa60d; _RF1=2409%3A8a5e%3Aa122%3A2440%3A8cb2%3Adefc%3Afa4a%3A943f; _abtest_userid=2bb8f078-868b-4719-b1b3-a3fc736ee6f8; _ubtstatus=%7B%22vid%22%3A%221718941212311.ffa662NVl7RG%22%2C%22sid%22%3A2%2C%22pvid%22%3A2%2C%22pid%22%3A600001375%7D; _bfaStatusPVSend=1; _bfaStatus=send; FlightIntl=Search=[%22HAK|%E6%B5%B7%E5%8F%A3(HAK)|42|HAK|480%22%2C%22HET|%E5%91%BC%E5%92%8C%E6%B5%A9%E7%89%B9(HET)|103|HET|480%22%2C%222024-06-25%22]; Union=OUID=&AllianceID=4897&SID=1520901&SourceID=&createtime=1719032845&Expires=1719637645264; MKT_OrderClick=ASID=48971520901&AID=4897&CSID=1520901&OUID=&CT=1719032845264&CURL=https%3A%2F%2Fflights.ctrip.com%2Fonline%2Fchannel%2Fdomestic%3Fallianceid%3D4897%26sid%3D1520901%26utm_medium%3Dbaidu%26utm_campaign%3Dty%26utm_source%3Dbaiduppc%26bd_creative%3D8005267900%26bd_vid%3D13451096799875603608%26keywordid%3D1186563087&VAL={}; nfes_isSupportWebP=1; MKT_CKID=1719032869056.0kizf.9fgl; _jzqco=%7C%7C%7C%7C1719032870447%7C1.861025259.1719032869059.1719032869059.1719032869059.1719032869059.1719032869059.0.0.0.1.1; _bfa=1.1718941212311.ffa662NVl7RG.1.1719032868779.1719051583983.3.1.10650052821',
  'cookieorigin': 'https://flights.ctrip.com',
  'origin': 'https://flights.ctrip.com',
  'priority': 'u=1, i',
  'referer': 'https://flights.ctrip.com/',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()

for i in range(0,30): 
    flights_data = data['routes'][i]
    flightNoname = (flights_data['flights'][0])['flightNo']
    aportname = flights_data['flights'][0]['aport']['name']
    dportname = flights_data['flights'][0]['dport']['name']
    dtime_date = (flights_data['flights'][0])['dtime']
    atime_date = (flights_data['flights'][0])['atime']
    st.write(flightNoname)
    st.write(aportname)
    st.write(dportname)
    st.write(dtime_date)
    st.write(atime_date)


