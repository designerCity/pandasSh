# DataFrame Indexing
iphone_df = pd.read_csv('./Downloads/iphone.csv', index_col=0)
iphone_df
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
iphone_df.loc['iPhone 8', '메모리']
'2GB'
iphone_df.loc['iPhone X', :]
출시일        2017-11-03
디스플레이             5.8
메모리               3GB
출시 버전        iOS 11.1
Face ID           Yes
Name: iPhone X, dtype: object
iphone_df.loc['iPhone X']
출시일        2017-11-03
디스플레이             5.8
메모리               3GB
출시 버전        iOS 11.1
Face ID           Yes
Name: iPhone X, dtype: object
type(iphone_df.loc['iPhone X'])
pandas.core.series.Series
iphone_df.loc[:, '출시일']
iPhone 7         2016-09-16
iPhone 7 Plus    2016-09-16
iPhone 8         2017-09-22
iPhone 8 Plus    2017-09-22
iPhone X         2017-11-03
iPhone XS        2018-09-21
iPhone XS Max    2018-09-21
Name: 출시일, dtype: object
iphone_df['출시일']
iphone_df['출시일']
iPhone 7         2016-09-16
iPhone 7 Plus    2016-09-16
iPhone 8         2017-09-22
iPhone 8 Plus    2017-09-22
iPhone X         2017-11-03
iPhone XS        2018-09-21
iPhone XS Max    2018-09-21
Name: 출시일, dtype: object
여러 줄 indexing
iphone_df.loc[['iPhone 8', 'iPhone 7']]
iphone_df.loc[['iPhone 8', 'iPhone 7']]
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
메모리
iphone_df[['출시일','Face ID', '메모리']]
출시일	Face ID	메모리
iPhone 7	2016-09-16	No	2GB
iPhone 7 Plus	2016-09-16	No	3GB
iPhone 8	2017-09-22	No	2GB
iPhone 8 Plus	2017-09-22	No	3GB
iPhone X	2017-11-03	Yes	3GB
iPhone XS	2018-09-21	Yes	4GB
iPhone XS Max	2018-09-21	Yes	4GB
row slicing
XS
iphone_df.loc['iPhone 8':'iPhone XS']
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
columns slicing
iphone_df
iphone_df.loc[:, '메모리':'Face ID']
메모리	출시 버전	Face ID
iPhone 7	2GB	iOS 10.0	No
iPhone 7 Plus	3GB	iOS 10.0	No
iPhone 8	2GB	iOS 11.0	No
iPhone 8 Plus	3GB	iOS 11.0	No
iPhone X	3GB	iOS 11.1	Yes
iPhone XS	4GB	iOS 12.0	Yes
iPhone XS Max	4GB	iOS 12.0	Yes
DataFrame 조건으로 indexing
iphone_df.loc[[True,False,True,False,True,True,False]]
iphone_df.loc[[True,False,True,False,True,True,False]]
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iphone_df.loc[:, [True,False,True,False,True]]
출시일	메모리	Face ID
iPhone 7	2016-09-16	2GB	No
iPhone 7 Plus	2016-09-16	3GB	No
iPhone 8	2017-09-22	2GB	No
iPhone 8 Plus	2017-09-22	3GB	No
iPhone X	2017-11-03	3GB	Yes
iPhone XS	2018-09-21	4GB	Yes
iPhone XS Max	2018-09-21	4GB	Yes
​
iphone_df['디스플레이'] > 5
iphone_df['디스플레이'] > 5
iPhone 7         False
iPhone 7 Plus     True
iPhone 8         False
iPhone 8 Plus     True
iPhone X          True
iPhone XS         True
iPhone XS Max     True
Name: 디스플레이, dtype: bool
위의 데이터는 pandas Series 인 일차원 데이터이다.
Filtering
iphone_df.loc[iphone_df['디스플레이'] > 5]
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
iphone_df['Face ID'] == 'Yes'
iphone_df['Face ID'] == 'Yes'
iPhone 7         False
iPhone 7 Plus    False
iPhone 8         False
iPhone 8 Plus    False
iPhone X          True
iPhone XS         True
iPhone XS Max     True
Name: Face ID, dtype: bool
iphone_df.loc[iphone_df['Face ID'] == 'Yes']
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
두개 이상의 조건
and 연산 조건
condition_and
condition_and = (iphone_df['디스플레이'] > 5) & (iphone_df['Face ID'] == 'Yes')
iphone_df.loc[condition_and]
iphone_df.loc[condition_and]
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
iphone_df[condition]
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
or 연산 조건
condition_or
condition_or = (iphone_df['디스플레이'] > 5) | (iphone_df['Face ID'] == 'Yes')
iphone_df.loc[condition_or]
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
DataFrame 위치로 인덱싱
좌표 같이 적용된다. row, columns

iphone_df.iloc[1, 3]
'iOS 10.0'
리스트, 리스트
2,4
iphone_df.iloc[[1,3], [2,4]]
메모리	Face ID
iPhone 7 Plus	3GB	No
iPhone 8 Plus	3GB	No
슬라이싱을 할 때에는 [],[] 형태를 사용하지 않는다.
iphone_df.iloc[3:, 1:4]
디스플레이	메모리	출시 버전
iPhone 8 Plus	5.5	3GB	iOS 11.0
iPhone X	5.8	3GB	iOS 11.1
iPhone XS	5.8	4GB	iOS 12.0
iPhone XS Max	6.5	4GB	iOS 12.0
