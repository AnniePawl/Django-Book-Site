## Django Book Site Assignment

**Query Methods:** all(), get(), filter(), exclude() <br>

**How would we filter for all books with titles containing the word ‘Django’?**<br>
`django_books = Book.objects.filter(title__contains = 'Django')`
`django_books`<br>

**How would we filter for all books with tag ‘Fiction’?**<br>
`fiction_books = Book.objects.filter(tag='Fiction')` `fiction_books`<br>

**How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!**<br>
