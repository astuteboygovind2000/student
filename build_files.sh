echo " BUILD START "
mkdir -p dist
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo " BUILD END "