from flask import jsonify, request, Blueprint

from twits_service.models.twitmodel import TwitModel as twit_model
from twits_service.services.twits import TwitsService
from twits_service.twitter_apis.search import TwitterSearchApi

main = Blueprint('main', __name__)

api = TwitterSearchApi(url='https://api.twitter.com/1.1/search/tweets.json')
ts = TwitsService(api, twit_model)


@main.route('/hashtags/<hashtag>', methods=['GET'], provide_automatic_options=True)
def hashtags(hashtag):
    pages_limit = request.args.get('pages_limit', 10, int)
    twits = ts.get_twits_by_hashtag(hashtag, pages_limit=pages_limit)
    twit_dicts = [twit.as_dict() for twit in twits]
    return jsonify(twit_dicts)


@main.route('/users/<user>', methods=['GET'], provide_automatic_options=True)
def users(user):
    pages_limit = request.args.get('pages_limit', 10, int)
    twits = ts.get_twits_by_username(user, pages_limit=pages_limit)
    twit_dicts = [twit.as_dict() for twit in twits]
    return jsonify(twit_dicts)
