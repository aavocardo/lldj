import requests
from re import search

host = "https://www.indexoflebanon.com/lottery/loto/draw/"


def extract_source(url):
    req = requests.get(url, "html.parser")
    return req.text


def extract(source, scope=42):
    source, bonus, results = source, '<div class="loto_no_w loto_no_hot">', []
    results.clear()

    def ball(parameter):
        return f'<div class="loto_no_r bbb{str(parameter)}">'

    def clear_value(value):
        if value < 10:
            return f'0{str(value)}'
        else:
            return str(value)

    def get_element(segment):
        for i in range(scope+1):
            script = f'{segment}{str(clear_value(i))}</div>'
            if search(script, source):
                results.append(i)

    def get_draw_number(trials=3000):
        for i in range(2000, trials):
            script = f'<div class="numbers_title">Loto Winning Numbers <span class="draw_no">Loto Draw {str(i)}</span' \
                     f'></div>'
            if search(script, source):
                results.append(i)

    get_element(ball(1))
    get_element(ball(2))
    get_element(ball(3))
    get_element(ball(4))
    get_element(ball(5))
    get_element(ball(6))
    results.sort()
    get_element(bonus)
    get_draw_number()
    return results
