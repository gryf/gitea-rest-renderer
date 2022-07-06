FROM gitea/gitea:latest
COPY ./rst2htmlbody.py /bin/rst2htmlbody
RUN apk --no-cache add py3-docutils py3-pygments && \
    chmod 755 /bin/rst2htmlbody
