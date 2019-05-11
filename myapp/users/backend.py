from datetime import datetime
def getUserdata(user):
    fname, lname, name  = '', '', user.name
    if name: 
        if ' ' in name:
            index = name.index(' ')
            fname = name[:index+1]
            lname = name[index+1:]
        else:
            fname = name
    
    data = {
        'username': user.username,
        'email'   : user.email if user.email else '',
        'dob'     : str(user.dob),
        'country' : user.country if user.country else '',
        'image'   : user.image.url if user.image else '/media/profile_image/default.jpg',
        'fname'   : fname,
        'lname'   : lname,
    }
    return data