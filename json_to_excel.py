import openpyxl
import json

with open(r'C:\Users\Назар\Favorites\Desktop\PYTHON\EGOROV_CHANNEL_YOUTUBE\EXCEL\list_of_movies.json', 'r') as json_file:
    deserialization = json.load(json_file)

book = openpyxl.Workbook()
sheet = book.active

sheet['A1'] = 'Id'
sheet['B1'] = 'Title'
sheet['C1'] = 'Year'
sheet['D1'] = 'Genres'
sheet['E1'] = 'Actors'
sheet['F1'] = 'Director'

row = 2
for movie in deserialization['movies']:
    sheet[row][0].value = movie['id']
    sheet[row][1].value = movie['title']
    sheet[row][2].value = int(movie['year'])
    sheet[row][3].value = ' '.join(movie['genres'])
    sheet[row][4].value = movie['actors']
    sheet[row][5].value = movie['director']
    row += 1

book.save('json_to_excel.xlsx')
book.close()