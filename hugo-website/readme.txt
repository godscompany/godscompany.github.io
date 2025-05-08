make a copy and modify the python script with more content
update makefile with new python script name
get domain name from ../CNAME
ex: tullamarineairporttransfers.com.au
update hugo.yaml:
baseURL: "https://tullamarineairporttransfers.com.au/hugo"
generate pages:
make build
will do:
initialise virtual environment
source ./venv-hugo/bin/activate
(create if not: python3 -m venv venv-hugo  )
install dependencies
pip install -r requirements.txt
run script:
python3 scripts/generate_pages_csv.py
:
mv public ../public/hugo
cp robot.txt sitemap-index.xml ../public
cd ..
update robot.txt sitemap-index.xml
git commit
