# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
import logging
logger = logging.getLogger("web2py.app.myweb2pyapplication")
logger.setLevel(logging.DEBUG)


def index():
    """
    Splash page
    """
    if auth.user_id:
        redirect(URL('default','board'))

    return dict()


def instructions():

    return dict()


def wordlist():
    """
    List of all words used in the game
    """
    rows = db(db.wordList.id > 0).select(db.wordList.word)
    word_list = [r.word for r in rows]
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    y = []
    z = []
    for word in word_list:
        if word[0] == 'a':
            a.append(word)
        if word[0] == 'b':
            b.append(word)
        if word[0] == 'c':
            c.append(word)
        if word[0] == 'd':
            d.append(word)
        if word[0] == 'e':
            e.append(word)
        if word[0] == 'f':
            f.append(word)
        if word[0] == 'g':
            g.append(word)
        if word[0] == 'h':
            h.append(word)
        if word[0] == 'i':
            i.append(word)
        if word[0] == 'j':
            j.append(word)
        if word[0] == 'k':
            k.append(word)
        if word[0] == 'l':
            l.append(word)
        if word[0] == 'm':
            m.append(word)
        if word[0] == 'n':
            n.append(word)
        if word[0] == 'o':
            o.append(word)
        if word[0] == 'p':
            p.append(word)
        if word[0] == 'q':
            q.append(word)
        if word[0] == 'r':
            r.append(word)
        if word[0] == 's':
            s.append(word)
        if word[0] == 't':
            t.append(word)
        if word[0] == 'u':
            u.append(word)
        if word[0] == 'v':
            v.append(word)
        if word[0] == 'w':
            w.append(word)
        if word[0] == 'x':
            x.append(word)
        if word[0] == 'y':
            y.append(word)
        if word[0] == 'z':
            z.append(word)
    return dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m,
                n=n, o=o, p=p, q=q, r=r, s=s, t=t, u=u, v=v, w=w, x=x, y=y, z=z)


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

def send_score():
    highScore = db(db.games.word == request.vars.targetWord).select();
    logger.debug(highScore)
    if int(request.vars.score) > highScore:
        db.games.update(db.games.targetWord == request.vars.targetWord,winner=auth.user_id, highScore = int(request.vars.score))
    return True;

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


