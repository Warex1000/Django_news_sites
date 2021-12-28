"""

python3 manage.py runserver - runserver
python3 manage.py runserver - runserver 4000 (port address: 4000)
python3 manage.py runserver - runserver 1.2.3.4:4000 (ip adress 1.2.3.4, port address: 4000)


pip install pillow - install for photo models python3 manage.py makemigrations - do migrations from models python3
manage.py sqlmigrate news 0001 - see the migration request to data base python3 manage.py migrate - after this to do
migration python3 manage.py shell - open console Django Work in Django: from news.models import News - We must import
models News in console Django News(title='Новость 1', content='Конент новости 1') - fill constructor data v.1 news1 =
_ - To do new variable news1.title - read result 'Новость 1' news1.save() - save information in Django - Refresh
Database in right side in IDE ds.sqlite from django.db import connection - see execute request in django
connection.queries - see the properties of connections result: ''' [{'sql': 'INSERT INTO "news_news" ("title",
"content", "create_at", "updated_at", "photo", "is_published") VALUES (\'Новость 1\', \'Конент новости 1\',
\'2021-08-14 06:30:20.078095\', \'2021-08-14 06:30:20.078192\', \'\', 1)', 'time': '0.241'}] ''' news1.pk - like id
news2 = News(title='Новость 2', content='Контент новости 2') - new News number2

news3 = News() - fill constructor data v.2
news3.title = 'Новость 3'
news3.content = 'Контент новости 3'
news1.save() - save information in Django

news4 = News.objects.create(title ='Новость 4', content='Контент новости 4') - fill constructor data v.3
News.objects.create(title ='News 5', content='Content of news 5') - v.4 Coming soon new information about it

News.objects.all() - show all objects if in russian language go th models.py line 13

for item in news: - show only title of news and status published
print(item.title, item.is_published)

News.objects.create(title='News 5', content='News 5 Content') - create the same news 5
News.objects.filter(title = 'News 5')

News.objects.get(pk=5) - pk like id, number in bd, this command take this object in bd v.1
News.objects.get(title='Новость 4') - title like id, title in bd, this command take this object in bd v.2
news5 = _ - insert information to values
news5.content (or news5.title) = 'News 5 content' - do changes
news5.save() - save changes

news7.delete() - delete in bd
News.objects.order_by('-title') - metod sortirovki
News.objects.exclude(title='Новость 2') - Filter News 2

cd mysite - go to folder mysite
python manage.py createsuperuser - create super user

cd /home/warex/PycharmProjects/django-sites/testssite/mysite/ - way to folder

"""
'''-> 
!!! Docker compose !!!
!!! React – JavaScript-библиотека !!!

Создать одностраничный сайт на джанго, 
'''





