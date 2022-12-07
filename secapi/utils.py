#!/usr/bin/env python
# -*- coding: utf-8 -*-

cik_mapping = {'MMM': '0000066740',
 'AOS': '0000091142',
 'ABT': '0000001800',
 'ABBV': '0001551152',
 'ABMD': '0000815094',
 'ACN': '0001467373',
 'ATVI': '0000718877',
 'ADM': '0000007084',
 'ADBE': '0000796343',
 'ADP': '0000008670',
 'AAP': '0001158449',
 'AES': '0000874761',
 'AFL': '0000004977',
 'A': '0001090872',
 'APD': '0000002969',
 'AKAM': '0001086222',
 'ALK': '0000766421',
 'ALB': '0000915913',
 'ARE': '0001035443',
 'ALGN': '0001097149',
 'ALLE': '0001579241',
 'LNT': '0000352541',
 'ALL': '0000899051',
 'GOOGL': '0001652044',
 'GOOG': '0001652044',
 'MO': '0000764180',
 'AMZN': '0001018724',
 'AMCR': '0001748790',
 'AMD': '0000002488',
 'AEE': '0001002910',
 'AAL': '0000006201',
 'AEP': '0000004904',
 'AXP': '0000004962',
 'AIG': '0000005272',
 'AMT': '0001053507',
 'AWK': '0001410636',
 'AMP': '0000820027',
 'ABC': '0001140859',
 'AME': '0001037868',
 'AMGN': '0000318154',
 'APH': '0000820313',
 'ADI': '0000006281',
 'ANSS': '0001013462',
 'AON': '0000315293',
 'APA': '0001841666',
 'AAPL': '0000320193',
 'AMAT': '0000006951',
 'APTV': '0001521332',
 'ANET': '0001596532',
 'AJG': '0000354190',
 'AIZ': '0001267238',
 'T': '0000732717',
 'ATO': '0000731802',
 'ADSK': '0000769397',
 'AZO': '0000866787',
 'AVB': '0000915912',
 'AVY': '0000008818',
 'BKR': '0001701605',
 'BALL': '0000009389',
 'BAC': '0000070858',
 'BBWI': '0000701985',
 'BAX': '0000010456',
 'BDX': '0000010795',
 'WRB': '0000011544',
 'BRK.B': '0001067983',
 'BBY': '0000764478',
 'BIO': '0000012208',
 'TECH': '0000842023',
 'BIIB': '0000875045',
 'BLK': '0001364742',
 'BK': '0001390777',
 'BA': '0000012927',
 'BKNG': '0001075531',
 'BWA': '0000908255',
 'BXP': '0001037540',
 'BSX': '0000885725',
 'BMY': '0000014272',
 'AVGO': '0001730168',
 'BR': '0001383312',
 'BRO': '0000079282',
 'BF.B': '0000014693',
 'CHRW': '0001043277',
 'CDNS': '0000813672',
 'CZR': '0001590895',
 'CPT': '0000906345',
 'CPB': '0000016732',
 'COF': '0000927628',
 'CAH': '0000721371',
 'KMX': '0001170010',
 'CCL': '0000815097',
 'CARR': '0001783180',
 'CTLT': '0001596783',
 'CAT': '0000018230',
 'CBOE': '0001374310',
 'CBRE': '0001138118',
 'CDW': '0001402057',
 'CE': '0001306830',
 'CNC': '0001071739',
 'CNP': '0001130310',
 'CDAY': '0001725057',
 'CF': '0001324404',
 'CRL': '0001100682',
 'SCHW': '0000316709',
 'CHTR': '0001091667',
 'CVX': '0000093410',
 'CMG': '0001058090',
 'CB': '0000896159',
 'CHD': '0000313927',
 'CI': '0001739940',
 'CINF': '0000020286',
 'CTAS': '0000723254',
 'CSCO': '0000858877',
 'C': '0000831001',
 'CFG': '0000759944',
 'CLX': '0000021076',
 'CME': '0001156375',
 'CMS': '0000811156',
 'KO': '0000021344',
 'CTSH': '0001058290',
 'CL': '0000021665',
 'CMCSA': '0001166691',
 'CMA': '0000028412',
 'CAG': '0000023217',
 'COP': '0001163165',
 'ED': '0001047862',
 'STZ': '0000016918',
 'CEG': '0001868275',
 'COO': '0000711404',
 'CPRT': '0000900075',
 'GLW': '0000024741',
 'CTVA': '0001755672',
 'CSGP': '0001057352',
 'COST': '0000909832',
 'CTRA': '0000858470',
 'CCI': '0001051470',
 'CSX': '0000277948',
 'CMI': '0000026172',
 'CVS': '0000064803',
 'DHI': '0000882184',
 'DHR': '0000313616',
 'DRI': '0000940944',
 'DVA': '0000927066',
 'DE': '0000315189',
 'DAL': '0000027904',
 'XRAY': '0000818479',
 'DVN': '0001090012',
 'DXCM': '0001093557',
 'FANG': '0001539838',
 'DLR': '0001297996',
 'DFS': '0001393612',
 'DISH': '0001001082',
 'DIS': '0001744489',
 'DG': '0000029534',
 'DLTR': '0000935703',
 'D': '0000715957',
 'DPZ': '0001286681',
 'DOV': '0000029905',
 'DOW': '0001751788',
 'DTE': '0000936340',
 'DUK': '0001326160',
 'DD': '0001666700',
 'DXC': '0001688568',
 'EMN': '0000915389',
 'ETN': '0001551182',
 'EBAY': '0001065088',
 'ECL': '0000031462',
 'EIX': '0000827052',
 'EW': '0001099800',
 'EA': '0000712515',
 'ELV': '0001156039',
 'LLY': '0000059478',
 'EMR': '0000032604',
 'ENPH': '0001463101',
 'ETR': '0000065984',
 'EOG': '0000821189',
 'EPAM': '0001352010',
 'EQT': '0000033213',
 'EFX': '0000033185',
 'EQIX': '0001101239',
 'EQR': '0000906107',
 'ESS': '0000920522',
 'EL': '0001001250',
 'ETSY': '0001370637',
 'RE': '0001095073',
 'EVRG': '0001711269',
 'ES': '0000072741',
 'EXC': '0001109357',
 'EXPE': '0001324424',
 'EXPD': '0000746515',
 'EXR': '0001289490',
 'XOM': '0000034088',
 'FFIV': '0001048695',
 'FDS': '0001013237',
 'FAST': '0000815556',
 'FRT': '0000034903',
 'FDX': '0001048911',
 'FITB': '0000035527',
 'FRC': '0001132979',
 'FE': '0001031296',
 'FIS': '0001136893',
 'FISV': '0000798354',
 'FLT': '0001175454',
 'FMC': '0000037785',
 'F': '0000037996',
 'FTNT': '0001262039',
 'FTV': '0001659166',
 'FBHS': '0001519751',
 'FOXA': '0001754301',
 'FOX': '0001754301',
 'BEN': '0000038777',
 'FCX': '0000831259',
 'GRMN': '0001121788',
 'IT': '0000749251',
 'GNRC': '0001474735',
 'GD': '0000040533',
 'GE': '0000040545',
 'GIS': '0000040704',
 'GM': '0001467858',
 'GPC': '0000040987',
 'GILD': '0000882095',
 'GL': '0000320335',
 'GPN': '0001123360',
 'GS': '0000886982',
 'HAL': '0000045012',
 'HIG': '0000874766',
 'HAS': '0000046080',
 'HCA': '0000860730',
 'PEAK': '0000765880',
 'HSIC': '0001000228',
 'HSY': '0000047111',
 'HES': '0000004447',
 'HPE': '0001645590',
 'HLT': '0001585689',
 'HOLX': '0000859737',
 'HD': '0000354950',
 'HON': '0000773840',
 'HRL': '0000048465',
 'HST': '0001070750',
 'HWM': '0000004281',
 'HPQ': '0000047217',
 'HUM': '0000049071',
 'HBAN': '0000049196',
 'HII': '0001501585',
 'IBM': '0000051143',
 'IEX': '0000832101',
 'IDXX': '0000874716',
 'ITW': '0000049826',
 'ILMN': '0001110803',
 'INCY': '0000879169',
 'IR': '0001699150',
 'INTC': '0000050863',
 'ICE': '0001571949',
 'IP': '0000051434',
 'IPG': '0000051644',
 'IFF': '0000051253',
 'INTU': '0000896878',
 'ISRG': '0001035267',
 'IVZ': '0000914208',
 'INVH': '0001687229',
 'IQV': '0001478242',
 'IRM': '0001020569',
 'JBHT': '0000728535',
 'JKHY': '0000779152',
 'J': '0000052988',
 'JNJ': '0000200406',
 'JCI': '0000833444',
 'JPM': '0000019617',
 'JNPR': '0001043604',
 'K': '0000055067',
 'KDP': '0001418135',
 'KEY': '0000091576',
 'KEYS': '0001601046',
 'KMB': '0000055785',
 'KIM': '0000879101',
 'KMI': '0001506307',
 'KLAC': '0000319201',
 'KHC': '0001637459',
 'KR': '0000056873',
 'LHX': '0000202058',
 'LH': '0000920148',
 'LRCX': '0000707549',
 'LW': '0001679273',
 'LVS': '0001300514',
 'LDOS': '0001336920',
 'LEN': '0000920760',
 'LNC': '0000059558',
 'LIN': '0001707925',
 'LYV': '0001335258',
 'LKQ': '0001065696',
 'LMT': '0000936468',
 'L': '0000060086',
 'LOW': '0000060667',
 'LUMN': '0000018926',
 'LYB': '0001489393',
 'MTB': '0000036270',
 'MRO': '0000101778',
 'MPC': '0001510295',
 'MKTX': '0001278021',
 'MAR': '0001048286',
 'MMC': '0000062709',
 'MLM': '0000916076',
 'MAS': '0000062996',
 'MA': '0001141391',
 'MTCH': '0000891103',
 'MKC': '0000063754',
 'MCD': '0000063908',
 'MCK': '0000927653',
 'MDT': '0001613103',
 'MRK': '0000310158',
 'META': '0001326801',
 'MET': '0001099219',
 'MTD': '0001037646',
 'MGM': '0000789570',
 'MCHP': '0000827054',
 'MU': '0000723125',
 'MSFT': '0000789019',
 'MAA': '0000912595',
 'MRNA': '0001682852',
 'MHK': '0000851968',
 'MOH': '0001179929',
 'TAP': '0000024545',
 'MDLZ': '0001103982',
 'MPWR': '0001280452',
 'MNST': '0000865752',
 'MCO': '0001059556',
 'MS': '0000895421',
 'MOS': '0001285785',
 'MSI': '0000068505',
 'MSCI': '0001408198',
 'NDAQ': '0001120193',
 'NTAP': '0001002047',
 'NFLX': '0001065280',
 'NWL': '0000814453',
 'NEM': '0001164727',
 'NWSA': '0001564708',
 'NWS': '0001564708',
 'NEE': '0000753308',
 'NKE': '0000320187',
 'NI': '0001111711',
 'NDSN': '0000072331',
 'NSC': '0000702165',
 'NTRS': '0000073124',
 'NOC': '0001133421',
 'NLOK': '0000849399',
 'NCLH': '0001513761',
 'NRG': '0001013871',
 'NUE': '0000073309',
 'NVDA': '0001045810',
 'NVR': '0000906163',
 'NXPI': '0001413447',
 'ORLY': '0000898173',
 'OXY': '0000797468',
 'ODFL': '0000878927',
 'OMC': '0000029989',
 'ON': '0001097864',
 'OKE': '0001039684',
 'ORCL': '0001341439',
 'OGN': '0001821825',
 'OTIS': '0001781335',
 'PCAR': '0000075362',
 'PKG': '0000075677',
 'PARA': '0000813828',
 'PH': '0000076334',
 'PAYX': '0000723531',
 'PAYC': '0001590955',
 'PYPL': '0001633917',
 'PNR': '0000077360',
 'PEP': '0000077476',
 'PKI': '0000031791',
 'PFE': '0000078003',
 'PCG': '0001004980',
 'PM': '0001413329',
 'PSX': '0001534701',
 'PNW': '0000764622',
 'PXD': '0001038357',
 'PNC': '0000713676',
 'POOL': '0000945841',
 'PPG': '0000079879',
 'PPL': '0000922224',
 'PFG': '0001126328',
 'PG': '0000080424',
 'PGR': '0000080661',
 'PLD': '0001045609',
 'PRU': '0001137774',
 'PEG': '0000788784',
 'PTC': '0000857005',
 'PSA': '0001393311',
 'PHM': '0000822416',
 'QRVO': '0001604778',
 'PWR': '0001050915',
 'QCOM': '0000804328',
 'DGX': '0001022079',
 'RL': '0001037038',
 'RJF': '0000720005',
 'RTX': '0000101829',
 'O': '0000726728',
 'REG': '0000910606',
 'REGN': '0000872589',
 'RF': '0001281761',
 'RSG': '0001060391',
 'RMD': '0000943819',
 'RHI': '0000315213',
 'ROK': '0001024478',
 'ROL': '0000084839',
 'ROP': '0000882835',
 'ROST': '0000745732',
 'RCL': '0000884887',
 'SPGI': '0000064040',
 'CRM': '0001108524',
 'SBAC': '0001034054',
 'SLB': '0000087347',
 'STX': '0001137789',
 'SEE': '0001012100',
 'SRE': '0001032208',
 'NOW': '0001373715',
 'SHW': '0000089800',
 'SBNY': '0001288784',
 'SPG': '0001063761',
 'SWKS': '0000004127',
 'SJM': '0000091419',
 'SNA': '0000091440',
 'SEDG': '0001419612',
 'SO': '0000092122',
 'LUV': '0000092380',
 'SWK': '0000093556',
 'SBUX': '0000829224',
 'STT': '0000093751',
 'STE': '0001757898',
 'SYK': '0000310764',
 'SIVB': '0000719739',
 'SYF': '0001601712',
 'SNPS': '0000883241',
 'SYY': '0000096021',
 'TMUS': '0001283699',
 'TROW': '0001113169',
 'TTWO': '0000946581',
 'TPR': '0001116132',
 'TRGP': '0001389170',
 'TGT': '0000027419',
 'TEL': '0001385157',
 'TDY': '0001094285',
 'TFX': '0000096943',
 'TER': '0000097210',
 'TSLA': '0001318605',
 'TXN': '0000097476',
 'TXT': '0000217346',
 'TMO': '0000097745',
 'TJX': '0000109198',
 'TSCO': '0000916365',
 'TT': '0001466258',
 'TDG': '0001260221',
 'TRV': '0000086312',
 'TRMB': '0000864749',
 'TFC': '0000092230',
 'TWTR': '0001418091',
 'TYL': '0000860731',
 'TSN': '0000100493',
 'USB': '0000036104',
 'UDR': '0000074208',
 'ULTA': '0001403568',
 'UNP': '0000100885',
 'UAL': '0000100517',
 'UPS': '0001090727',
 'URI': '0001067701',
 'UNH': '0000731766',
 'UHS': '0000352915',
 'VLO': '0001035002',
 'VTR': '0000740260',
 'VRSN': '0001014473',
 'VRSK': '0001442145',
 'VZ': '0000732712',
 'VRTX': '0000875320',
 'VFC': '0000103379',
 'VTRS': '0001792044',
 'VICI': '0001705696',
 'V': '0001403161',
 'VNO': '0000899689',
 'VMC': '0001396009',
 'WAB': '0000943452',
 'WBA': '0001618921',
 'WMT': '0000104169',
 'WBD': '0001437107',
 'WM': '0000823768',
 'WAT': '0001000697',
 'WEC': '0000783325',
 'WFC': '0000072971',
 'WELL': '0000766704',
 'WST': '0000105770',
 'WDC': '0000106040',
 'WRK': '0001732845',
 'WY': '0000106535',
 'WHR': '0000106640',
 'WMB': '0000107263',
 'WTW': '0001140536',
 'GWW': '0000277135',
 'WYNN': '0001174922',
 'XEL': '0000072903',
 'XYL': '0001524472',
 'YUM': '0001041061',
 'ZBRA': '0000877212',
 'ZBH': '0001136869',
 'ZION': '0000109380',
 'ZTS': '0001555280'}