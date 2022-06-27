import csv
import os
from collections import defaultdict, namedtuple

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIE_DATA = 'movies.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 22
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_DATA):
    directors=defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                title=line['movie_title'].replace('\xa0', '')
                year=int(line['title_year'])
                director=line['director_name']
                score=float(line['imdb_score'])
            except ValueError:
                continue
            m=Movie(title=title,year=year,score=score)
            if m.year and int(m.year) >= MIN_YEAR:
                directors[director].append(m)
    
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    result = defaultdict(float)
    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        else:
            result[(director, _calc_mean(movies))] = sorted(movies, key=lambda m: m.score, reverse=True)
    return result


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum(float(movie.score) for movie in movies) / len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter:>02}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    reports = sorted(directors.items(), key=lambda d: d[0][1], reverse=True)[:NUM_TOP_DIRECTORS]
    print(reports)
    for counter, (k, v) in enumerate(reports, 1):
        print(counter)
        print(k,v)
        print(fmt_director_entry.format(counter=counter, director=k[0], avg=str(k[1])))
        print(sep_line)
        print(fmt_movie_entry)
        for movie in v:
            print(fmt_movie_entry.format(year=movie.year,
                                         title=movie.title,
                                         score=movie.score))
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    print_results(directors)


if __name__ == '__main__':
    main()