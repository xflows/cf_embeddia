import requests


def cf_embeddia_article_analyzer(input_dict):
    text = input_dict['text']
    analyzer = input_dict['algorithm']
    url = input_dict['url']

    jsondata = {'text': text, 'analyzers': [analyzer]}
    response = requests.post(url, json=jsondata)
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
    result = response.json()

    tags = [x['tag'] for x in result.get('tags', [])]
    return {'keywords': tags}


def cf_embeddia_article_analyzer_NER(input_dict):
    text = input_dict['text']
    analyzer = input_dict['algorithm']
    url = input_dict['url']

    jsondata = {'text': text, 'analyzers': [analyzer]}
    response = requests.post(url, json=jsondata)
    result = response.json()

    entities = [(x['entity'], x['type']) for x in result.get('entities', [])]
    return {'entities': entities}


def cf_embeddia_comment_moderator(input_dict):
    corpus = input_dict['corpus']
    analyzer = input_dict['analyzer']
    threshold = float(input_dict['threshold'])
    url = input_dict['url']

    if len(corpus) > 100:
        raise ValueError('Too many input documents for this service.')

    filtered_corpus = []
    for doc in corpus:
        jsondata = {'text': doc, 'analyzers': [analyzer]}
        response = requests.post(url, json=jsondata)
        result = response.json()
        if result.get('tags'):
            first = result['tags'][0]
            if first['tag'] == 'OFFENSIVE' and first['probability'] > threshold:
                continue
            else:
                filtered_corpus.append(doc)
    return {'filtered_corpus': filtered_corpus}
