from datetime import date
from models import BookInfo

if __name__ == "__main__":
    book = BookInfo(
        btitle='西游记',
        bpub_date=date(1988, 1, 1),
        bread=10,
        bcomment=10,
    )
    book.save()
