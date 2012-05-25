from mongoengine import *
from models import User, IA

DATABASE_NAME = "ia"

def get_code_by_id_ia(id_ia):
    """Get the python code of a specific ia"""
    connect(DATABASE_NAME)
    try:
        ia = IA.objects.get(id=id_ia)
        ia_code = ia.code
        ia.save()
        return { 'success':True, 'result': ia_code }
    except Exception:
        ia_dict = { 'success':False, 'error': Exception.message }

    return ia_dict

def update_ia_points(id_ia, points_to_add):
    """Update points of a specific ia"""
    connect(DATABASE_NAME)
    try:
        ia = IA.objects.get(id=id_ia)
        updated_ia_points = int(ia.points) + int(points_to_add)
        ia.points = str(updated_ia_points)
        ia.save()
        return { 'success':True, 'result': updated_ia_points }
    except :
        return { 'success':False, 'error': Exception.message }

#Example
#if __name__ == '__main__':
    #user = User.objects.create(name="test1", email="sandro")
    #IA.objects.create(code="import json ...", points="3", user=user)

    #print get_code_by_id_ia("4fa2f20666969c1dea000001")
    #print update_ia_points("4fa2eee266969c1b2f000001", '3')