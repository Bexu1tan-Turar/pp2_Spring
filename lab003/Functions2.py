# Dictionary of movies
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1)
# def movie(s):
#   for i in movies:
#     if i['name'] == s:
#         if(i['imdb']> 5.5):
#             print('True')
#         else:
#             print('False')
# s = input()
# movie(s)

# 2)
# def result(movies):
#     list=[];
#     for i in range(0,len(movies)):
#         movie=movies[i];
#         if movie['imdb']>5.5:
#             list.append(movie)
#     return list
# print(result(movies))

# 3)
# def result(movies):
#     categ = input()
#     lst=[]
#     for i in movies:
#         categ1=i['category']
#         if categ.lower()==categ1.lower():
#             lst.append(i)
#     return lst
# print(result(movies))

# 4)
# def result(movies):
#     sum = 0
#     total=len(movies)
#     for i in movies:
#         sum = sum+i['imdb']
#     sum = sum/total
#     return sum
# print(result(movies))

# 5)
# def categ(movies,cat_name):
#     out_list=[]
#     for i in movies:
#         curr_cat=i['category']
#         if cat_name.lower()==curr_cat.lower():
#             out_list.append(i)
#     return out_list
# def imdb(movies):
#     avg_score=0
#     tot_movies=len(movies)
#     for i in movies:
#         avg_score=avg_score+i['imdb']
#     avg_score=avg_score/tot_movies
#     return avg_score
# def result(movies, cotegor):
#     movie = categ(movies,cotegor)
#     score = imdb(movie)
#     print(score)
# cotegor = input()
# result(movies,cotegor)
