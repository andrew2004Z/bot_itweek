def sort_rating(sp):
    sp.sort(key=lambda x: x[2])
    sp = sp[::-1]
    return sp