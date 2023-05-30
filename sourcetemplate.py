def sourcetemplate(url):
    def inner(**x):
        return url + '?' + '&'.join(sorted([f'{k}={v}' for k, v in x.items()])) if x != {} else url
    return inner

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(name='Daniil', thread='solutions', unit=648165))