FROM matthewbentley/counter-base

ADD presence.py /

CMD python /presence.py
