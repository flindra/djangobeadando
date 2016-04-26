from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60, default='', blank=True)
	birth_year = models.IntegerField(null=True, blank=True)
	birth_place = models.CharField(max_length=60, default='', blank=True)
	death_year = models.IntegerField(null=True, blank=True)
	death_place = models.CharField(max_length=60, default='', blank=True)

	def __str__(self):
		name = self.first_name
		if self.last_name:
			name += ' {0}'.format(self.last_name)
		return name


class Book(models.Model):
	author = models.ManyToManyField(Author)
	title = models.CharField(max_length=60)
	publisher = models.CharField(max_length=60, default='', blank=True)
	year = models.IntegerField()
	btype = models.CharField('type of lending', max_length=2, choices=(
		('1m', '1 hónapos kölcsönzés'),
		('1w', '1 hetes kölcsönzés'),
		('0w', 'nem kölcsönözhető')
		), default='1m')

	def __str__(self):
		return self.title


class User(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	birth_year = models.IntegerField()
	birth_place = models.CharField(max_length=60)
	work_place = models.CharField(max_length=60)
	email = models.EmailField(max_length=60)
	phone = models.CharField(max_length=60)

	def __str__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)


class Lending(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	lending_date = models.DateTimeField()

	def __str__(self):
		return '{0} | {1} | {2}'.format(self.user, self.book, self.lending_date)