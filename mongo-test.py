import datetime, os
from mongoengine import DateTimeField, Document, IntField, StringField, connect
from dotenv import load_dotenv

load_dotenv(override=True)

mongo_host = os.getenv("DB_HOST")
mongo_db = os.getenv("DB")
mongo_user = os.getenv("DB_USER")
mongo_password = os.getenv("DB_PASSWORD")
sleep_time = os.getenv("SLEEP_TIME", default=0)

print(f"Connecting to {mongo_host} as {mongo_user}")
connect(
    db=mongo_db,
    host=mongo_host,
    username=mongo_user,
    password=mongo_password,
    retryWrites=False,
)


class CatBreed(Document):
    breed = StringField(required=True, max_length=64)
    style = StringField(max_length=255)
    sub_species_count = IntField()
    last_updated = DateTimeField()


cat = CatBreed(
    breed="Siamese",
    style="Sassy",
    last_updated=datetime.datetime.now(datetime.timezone.utc),
    sub_species_count=5,
)

cat.save()

print(cat.to_json())

d = cat.to_mongo().to_dict()

print(f"As a dictionary: {d}")
d["id"] = str(d["_id"])
d.pop("_id")
print(f"As a dictionary: {d}")
