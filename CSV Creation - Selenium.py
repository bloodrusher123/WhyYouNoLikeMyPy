import csv


Sites = ['Go Compare', 'Compare the Market', 'Money Supermarket', 'Insurers']
dictExtract = {
    'Site': 'Compare the Market',
    'AggQuote': '1,234',
    'BrandQuote': '5,678',
    'Top': '28',
    'Clicks': '12'
}

AggQuote = '2,345'
header = ['Site', 'AggQuote', 'BrandQuote', 'Top', 'Clicks']
rows = [
    [Sites[0], dictExtract['AggQuote'], dictExtract['BrandQuote'], dictExtract['Top'], dictExtract['Clicks']],
    [Sites[1], dictExtract['AggQuote'], dictExtract['BrandQuote'], dictExtract['Top'], dictExtract['Clicks']]
]

listOfExtractedData = ['Go Compare','4321', '3421', '23', '11']

def AssignDictionaryValues():
    dictExtract['Site'] = listOfExtractedData[0]
    dictExtract['AggQuote'] = listOfExtractedData[1]
    dictExtract['BrandQuote'] = listOfExtractedData[2]
    dictExtract['Top'] = listOfExtractedData[3]
    dictExtract['Clicks'] = listOfExtractedData[4]
    return dictExtract


def CSVwrite():
    with open('results.csv', 'a') as b:
        csv_append = csv.writer(b)
        csv_append.writerow()



with open("results.csv", 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    for row in rows:
        csv_writer.writerow(row)