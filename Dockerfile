FROM thubo/latexmk

FROM python:3
ADD proto.py /
RUN pip install gnureadline
RUN pip install pylatex

CMD [ "python", "./proto.py"]