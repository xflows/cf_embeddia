import requests


def cf_embeddia_article_analyzer(input_dict):
    text = input_dict['text']
    analyzer = input_dict['algorithm']
    url = input_dict['url']

    jsondata = {'text': text, 'analyzers': [analyzer]}
    response = requests.post(url, json=jsondata)
    if response.status_code // 100 != 2:
        raise Exception('Web service error, code {}'.format(response.status_code))
    result = response.json()

    tags = [x['tag'] for x in result.get('tags', [])]
    entities = [(x['entity'], x['type']) for x in result.get('entities', [])]

    return {'keywords': tags, 'entities': entities}


def cf_embeddia_article_analyzer_keywords(input_dict):
    text = input_dict['text']
    analyzer = input_dict['algorithm']
    url = input_dict['url']

    jsondata = {'text': text, 'analyzers': [analyzer]}
    response = requests.post(url, json=jsondata)
    if response.status_code // 100 != 2:
        raise Exception('Web service error, code {}'.format(response.status_code))
    result = response.json()

    tags = [x['tag'] for x in result.get('tags', [])]
    return {'keywords': tags}


def cf_embeddia_article_analyzer_NER(input_dict):
    text = input_dict['text']
    analyzer = input_dict['algorithm']
    url = input_dict['url']

    jsondata = {'text': text, 'analyzers': [analyzer]}
    response = requests.post(url, json=jsondata)
    if response.status_code // 100 != 2:
        raise Exception('Web service error, code {}'.format(response.status_code))
    result = response.json()

    entities = [(x['entity'], x['type']) for x in result.get('entities', [])]
    return {'entities': entities}


def cf_embeddia_comment_analyzer(input_dict):
    corpus = input_dict['corpus']
    url = input_dict['url']

    jsondata = {'texts': corpus}
    response = requests.post(url, json=jsondata)
    if response.status_code // 100 != 2:
        raise Exception('Web service error, code {}'.format(response.status_code))
    result = response.json()
    labels = result.get('labels')
    print(labels)
    labels = ['offensive' if x == 'Blocked' else x for x in labels]
    labels = ['ok' if x == 'Non-Blocked' else x for x in labels]
    return {'labels': labels, 'confidences': result.get('confidences')}


def cf_embeddia_author_profiling(input_dict):
    corpus = input_dict['corpus']
    url = input_dict['url']

    jsondata = {'texts': corpus}
    response = requests.post(url, json=jsondata)
    if response.status_code // 100 != 2:
        raise Exception('Web service error, code {}'.format(response.status_code))
    result = response.json()
    return {'profiles': result.get('decisions')}
