# Web Crawler

### Main Objective
Produces a web crawler to scrap several pages

Quick Start set up the project on your to local machine
-
1 - Get started:
```
$ git clone <repository.git>
$ cd dcp_webscrapper
```

2 - Create virtual environment
```
$ python -m venv env
$ env\Scripts\activate
```

3 - Install requirements
```
$ pip install -r requirements.txt
```

4 - Modifications

Each modification such as, addition of new features, changing the training data, experiment new alghoritms shall be firstly tested on notebooks folder, and only then changed in the packages sections.

5 - Testing
```
$ pytest packages\tests
```

6 - Running Project
```
$ python package\crawler\crawler\crawler.py
```

7 - Pushing to central repository
```
$ git checkout <branch_repository.git>
$ git add .
$ git commit -m "Addition of new feature [feature_name]"
$ git push
```