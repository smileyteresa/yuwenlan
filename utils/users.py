from flask import session, redirect

def require_login(func):
    def _deco(*args, **kwargs):
        try:
            session['id']
        except Exception:
            pass
        else:
            if session['id']:
                return func(*args, **kwargs)
        finally:
            return redirect('/whatsup/')

    return _deco