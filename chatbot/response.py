from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from chatbot.data_processing import sent_tokens, LemNormalize


def response(user_response):
    c3po_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        c3po_response=c3po_response+"I am sorry! I don't understand you"
        return c3po_response
    else:
        c3po_response = c3po_response+sent_tokens[idx]
        return c3po_response