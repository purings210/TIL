# models.py



# models.py 작성 후 데이터를 넣는 3가지 방법

```django
article = Article()

article.title = 'aaa'

article.content = 'aaa'

article.save()



article = Article(title='bbb', content='bbb')

article.save()



Article.objects.create(title='ccc', content='ccc')
```



- Class 내부

```django
def _ _str_ _(self):

	return self.title
```

로 작성해서 출력을 조금 더 사람친화적으로 바꿀수있다.



## READ 부분

1. all()

   Article.objects.all()  -> 전체데이터가 QuerySet으로 전달됨으로 변수에 저장해서 사용하면 된다.

2. get()

   article = Article.objects.get(pk=1)  ->  pk에 해당하는 값을 가져오며, 변수에 담아서 확인 가능하다.

   없는 pk값을 인자로 넣으면 error발생(DoesNotExist), 또한 인자로 겹치는 데이터가 있다면 error(MultipleObjectsReturned, 그러므로 pk로 불러와야 겹침없이 불러올 수 있다 + NOT NULL일때!)

3. filter()









