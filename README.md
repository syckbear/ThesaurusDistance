# ThesaurusDistance

List the synonyms to needed to transform one word to another.

## Installation

```
> virtualenv ThesaurusDistance.env
> source ThesaurusDistance.env
> pip install -r requirements.txt
# download nltk data if you haven't already; this could take a while
> python -m nltk.downloader all
# set location of NLTK_DATA; mine is in my home dir
> export NLTK_DATA=$HOME/nltk_data
```

### Run tests

```
> python thesaurus_distance_test.py
```

## Usage

### Command line

```
> python ThesaurusDistance dog cat
blackguard,guy
```

### Libaray

```python
from ThesaurusDistance import thesaurus_distance

path = thesaurus_distance('dog', 'cat')
# ['blackguard', 'guy']
```

### Trivia

War can never become peace but peace can become war.

```
> ThesaurusDistance.py war peace
no route found.
> python ThesaurusDistance.py peace war
repose,ease,facilitate,help,supporter,champion,fighter,belligerent,warring
```
