# 데이터 전처리
# - NaN 값 포함된 데이터 전체 삭제
# - "구" 필드 생성하기
# - 데이터 출력 필드: 상호, 상표, 구, 세프여부, 휘발유, 경우 만 출력
# - "휘발유", "경유": float64로 변경
# - "휘발유", "경유" 데이터의 "-"를 평균값으로 수정

import os
import pandas as pd


oildf = pd.DataFrame()
fname = os.listdir('./data')
for i in fname:
  try:
    df = pd.read_csv("/content/data/"+i, header=2)
    oildf = pd.concat([oildf,df])
  except:
    df = pd.read_csv("/content/data/"+i, header=2, encoding="cp949")
    oildf = pd.concat([oildf,df])
del df
# oildf.info()
oildf.reset_index(drop=True, inplace=True)


# NaN 값 포함된 데이터 전체 삭제
oildf2 = oildf.dropna(subset=["휘발유","경유"]).copy()
oildf2 = oildf2.fillna("-")

# "휘발유", "경유" 데이터의 "-"를 평균값으로 수정
sum = 0
cnt = 0
for i in oildf2.index:
    if oildf2.loc[i, "휘발유"] != '-':
        sum += float(oildf2.loc[i, "휘발유"])
        cnt += 1

    else:
        continue

mean = sum / cnt
# oildf2[(oildf2["휘발유"]=="-")] = mean
oildf2["휘발유"].replace("-", mean, inplace=True)

# "휘발유", "경유": float64로 변경
oildf2 = oildf2.astype({"휘발유": float})
print(oildf2.info())