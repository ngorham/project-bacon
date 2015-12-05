# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################


def index():
    """
    Splash page
    """
    return dict()


def instructions():

    return dict()


def wordlist():
    """
    List of all words used in the game
    """
    d = db().select(db.wordList.ALL).as_list()
    return dict(wordList=d)


def board():
    """
    List of playable games
    """
    return dict()


def game():
    """
    Individual game
    """
    game = db(db.games.id == request.args(0)).select().first()
    rows = db().select(db.wordList.ALL)
    d = [r.word for r in rows]
    return dict(targetWord=game.targetWord)


def load_wordlist():
    """
    Loads the list of words
    """
    rows = db().select(db.wordList.ALL)
    d = [r.word for r in rows]
    return response.json(dict(wordList=d))


def add_game():
    """
    Adds a game to the database
    Removes a game name from the database
    """
    db.games.update_or_insert(targetWord = request.vars.targetWord)
    db(db.game_names.word == request.vars.targetWord).delete()
    return 'ok'


def load_games():
    """
    Loads the list of created games
    """
    rows = db().select(db.games.ALL)
    d = {r.id: {'word': r.targetWord} for r in rows}
    return response.json(dict(games=d))


def load_game_names():
    """
    Loads the list of available game names
    """
    rows = db().select(db.game_names.ALL)
    d2 = [r.word for r in rows]
    return response.json(dict(game_names=d2))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


