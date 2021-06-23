import json

from bson.objectid import ObjectId

from mongo.mongoService import MongoClientService

mongo = MongoClientService("db", "comments", "localhost", 27017, "mongodbuser", "mongoPassword")
comments = []


def configure_record(request):
    tags = request.POST.get('tags').split()

    setting = {
        'author_name': request.POST.get('author_name'),
        'description': request.POST.get('description'),
        'commentsSet': [{
            'mandatory_words': tags,
            'comments': comments
        }]
    }
    setting_dict = toJsonFormatedDict
    mongo.db.insert_one(setting)
    comments.clear()
    comments_list = read_all()
    return comments_list


def toJsonFormatedDict(value):
    setting_json = json.dumps(value)  # json format
    setting_dict = json.loads(setting_json)
    return setting_dict


def add(request):
    single_comment = request.POST.get('comment')
    print(single_comment)
    comments.append(single_comment)
    return comments


def clear():
    comments.clear()


def read_all():
    comments_list = []
    all = mongo.readAll()  # read all comments form db
    for comment in all:
        comments_list.append(comment)
    return comments_list


def read_one(_id):
    return mongo.db.find_one({'_id': ObjectId(_id)})


def read_tmp_comment_list():
    return comments


def delete(_id):
    mongo.db.delete_one({'_id': ObjectId(_id)})
