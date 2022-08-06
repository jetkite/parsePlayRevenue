import pandas as pd
import xlsxwriter
df = pd.read_csv('play.csv')
c = df.groupby('Buyer Country')['Amount (Merchant Currency)'].sum().reset_index()
country_revenue = [72]
for x in range(72):
    country_revenue.append(0)

countries = c['Buyer Country'].tolist()
revenues = c['Amount (Merchant Currency)'].tolist()

country_revenue[0] = revenues[countries.index('US')] if 'US' in countries else 0
country_revenue[1] = revenues[countries.index('DE')] if 'DE' in countries else 0
country_revenue[2] = revenues[countries.index('AT')] if 'AT' in countries else 0
country_revenue[3] = revenues[countries.index('JP')] if 'JP' in countries else 0
country_revenue[4] = revenues[countries.index('CA')] if 'CA' in countries else 0
country_revenue[5] = revenues[countries.index('FR')] if 'FR' in countries else 0
country_revenue[6] = revenues[countries.index('CH')] if 'CH' in countries else 0
country_revenue[7] = revenues[countries.index('KR')] if 'KR' in countries else 0
country_revenue[8] = revenues[countries.index('NL')] if 'NL' in countries else 0
country_revenue[9] = revenues[countries.index('GB')] if 'GB' in countries else 0
country_revenue[10] = revenues[countries.index('BE')] if 'BE' in countries else 0
country_revenue[11] = revenues[countries.index('IT')] if 'IT' in countries else 0
country_revenue[12] = revenues[countries.index('BR')] if 'BR' in countries else 0
country_revenue[13] = revenues[countries.index('TW')] if 'TW' in countries else 0
country_revenue[14] = revenues[countries.index('HK')] if 'HK' in countries else 0
country_revenue[15] = revenues[countries.index('DK')] if 'DK' in countries else 0
country_revenue[16] = revenues[countries.index('SE')] if 'SE' in countries else 0
country_revenue[17] = revenues[countries.index('FI')] if 'FI' in countries else 0
country_revenue[18] = revenues[countries.index('AU')] if 'AU' in countries else 0
country_revenue[19] = revenues[countries.index('ES')] if 'ES' in countries else 0
country_revenue[20] = revenues[countries.index('PL')] if 'PL' in countries else 0
country_revenue[21] = revenues[countries.index('MX')] if 'MX' in countries else 0
country_revenue[22] = revenues[countries.index('CZ')] if 'CZ' in countries else 0
country_revenue[23] = revenues[countries.index('SK')] if 'SK' in countries else 0
country_revenue[24] = revenues[countries.index('TH')] if 'TH' in countries else 0
country_revenue[25] = revenues[countries.index('HU')] if 'HU' in countries else 0
country_revenue[26] = revenues[countries.index('IE')] if 'IE' in countries else 0
country_revenue[27] = revenues[countries.index('NZ')] if 'NZ' in countries else 0
country_revenue[28] = revenues[countries.index('ID')] if 'ID' in countries else 0
country_revenue[29] = revenues[countries.index('VN')] if 'VN' in countries else 0
country_revenue[30] = revenues[countries.index('NO')] if 'NO' in countries else 0
country_revenue[31] = revenues[countries.index('HR')] if 'HR' in countries else 0
country_revenue[32] = revenues[countries.index('LU')] if 'LU' in countries else 0
country_revenue[33] = revenues[countries.index('IL')] if 'IL' in countries else 0
country_revenue[34] = revenues[countries.index('GR')] if 'GR' in countries else 0
country_revenue[35] = revenues[countries.index('ZA')] if 'ZA' in countries else 0
country_revenue[36] = revenues[countries.index('RU')] if 'RU' in countries else 0
country_revenue[37] = revenues[countries.index('PT')] if 'PT' in countries else 0
country_revenue[38] = revenues[countries.index('RO')] if 'RO' in countries else 0
country_revenue[39] = revenues[countries.index('IN')] if 'IN' in countries else 0
country_revenue[40] = revenues[countries.index('LV')] if 'LV' in countries else 0
country_revenue[41] = revenues[countries.index('EE')] if 'EE' in countries else 0
country_revenue[42] = revenues[countries.index('LT')] if 'LT' in countries else 0
country_revenue[43] = revenues[countries.index('SG')] if 'SG' in countries else 0
country_revenue[44] = revenues[countries.index('MY')] if 'MY' in countries else 0
country_revenue[45] = revenues[countries.index('BN')] if 'BN' in countries else 0
country_revenue[46] = revenues[countries.index('CO')] if 'CO' in countries else 0
country_revenue[47] = revenues[countries.index('PE')] if 'PE' in countries else 0
country_revenue[48] = revenues[countries.index('AR')] if 'AR' in countries else 0
country_revenue[49] = revenues[countries.index('PH')] if 'PH' in countries else 0
country_revenue[50] = revenues[countries.index('PY')] if 'PY' in countries else 0
country_revenue[51] = revenues[countries.index('JM')] if 'JM' in countries else 0
country_revenue[52] = revenues[countries.index('HT')] if 'HT' in countries else 0
country_revenue[53] = revenues[countries.index('GT')] if 'GT' in countries else 0
country_revenue[54] = revenues[countries.index('BO')] if 'BO' in countries else 0
country_revenue[55] = revenues[countries.index('EC')] if 'EC' in countries else 0
country_revenue[56] = revenues[countries.index('CL')] if 'CL' in countries else 0
country_revenue[57] = revenues[countries.index('PA')] if 'PA' in countries else 0
country_revenue[58] = revenues[countries.index('NI')] if 'NI' in countries else 0
country_revenue[59] = revenues[countries.index('PR')] if 'PR' in countries else 0
country_revenue[60] = revenues[countries.index('CR')] if 'CR' in countries else 0
country_revenue[61] = revenues[countries.index('BB')] if 'BB' in countries else 0
country_revenue[62] = revenues[countries.index('UY')] if 'UY' in countries else 0
country_revenue[63] = revenues[countries.index('DO')] if 'DO' in countries else 0
country_revenue[64] = revenues[countries.index('SV')] if 'SV' in countries else 0
country_revenue[65] = revenues[countries.index('EG')] if 'EG' in countries else 0
country_revenue[66] = revenues[countries.index('MA')] if 'MA' in countries else 0
country_revenue[67] = revenues[countries.index('TN')] if 'TN' in countries else 0
country_revenue[68] = revenues[countries.index('JO')] if 'JO' in countries else 0
country_revenue[69] = revenues[countries.index('SA')] if 'SA' in countries else 0
country_revenue[70] = revenues[countries.index('AE')] if 'AE' in countries else 0
country_revenue[71] = revenues[countries.index('QA')] if 'QA' in countries else 0
country_revenue[72] = revenues[countries.index('KW')] if 'KW' in countries else 0

countries_main = ["US",
"Germany",
"Austria",
"Japan",
"Canada",
"France",
"Switzerland",
"South Korea",
"Netherlands",
"UK",
"Belgium",
"Italy",
"Brazil",
"Taiwan",
"Hong Kong",
"Denmark",
"Sweden",
"Finland",
"Australia",
"Spain",
"Poland",
"Mexico",
"Czech Republic",
"Slovakia",
"Thailand",
"Hungary",
"Ireland",
"New Zealand",
"Indonesia",
"Viet nam",
"Norway",
"Croatia",
"Luxembourg",
"Israel",
"Greece",
"South Africa",
"Russia",
"Portugal",
"Romania",
"India",
"Latvia",
"Estonia",
"Lithuania",
"Singapore",
"Malaysia",
"Brunei",
"Colombia",
"Peru",
"Argentina",
"Philippinnes",
"Paraguay",
"Jamaica",
"Haiti",
"Guatemala",
"Bolivia",
"Ecuador",
"Chile",
"Panama",
"Nicaragua",
"Puerto Rico",
"Costa Rica",
"Barbados",
"Uruguay",
"Dominican R.",
"El Salvador",
"Egypt",
"Morocco",
"Tunisia",
"Jordan",
"Saudi Arabia",
"UAE",
"Qatar",
"Kuwait"]
df = pd.DataFrame({
    'Countries': countries_main,
    'Revenue': country_revenue
})

writer = pd.ExcelWriter('play.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='play', index=False)
writer.save()