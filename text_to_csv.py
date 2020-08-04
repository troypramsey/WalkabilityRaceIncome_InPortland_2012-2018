import csv

f = open('OR_Features_20200701.txt', 'r')
content = ''
for i in f:
    content += i

# content_comma = content.replace('|', ',')

# # print(content_comma)

# header_raw = 'FEATURE_ID|FEATURE_NAME|FEATURE_CLASS|STATE_ALPHA|STATE_NUMERIC|COUNTY_NAME|COUNTY_NUMERIC|PRIMARY_LAT_DMS|PRIM_LONG_DMS|PRIM_LAT_DEC|PRIM_LONG_DEC|SOURCE_LAT_DMS|SOURCE_LONG_DMS|SOURCE_LAT_DEC|SOURCE_LONG_DEC|ELEV_IN_M|ELEV_IN_FT|MAP_NAME|DATE_CREATED|DATE_EDITED'
# header = header_raw.replace('|', ',').lower()

print(content)