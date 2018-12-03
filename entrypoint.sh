#!/usr/bin/env bash

echo "     . ^^ .     " && \
echo "    .. || ..    " && \
echo "   ... || ...   " && \
echo "  .... || ....  " && \
echo " ..... || ..... " && \
echo "...... || ......" && \
echo "...... || ......" && \
echo " ..... || ..... " && \
echo "  .... || ....  " && \
echo "   ... || ...   " && \
echo "    .. || ..    " && \
echo "     . vv .     " && \
python manage.py makemigrations && \
python manage.py migrate && \
python3 manage.py runserver 0.0.0.0:8000


