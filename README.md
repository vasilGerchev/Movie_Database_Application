                                Project Title: "Movie Database Application"




Functionality ( CLI ):

Movie Listing Page: movlst
When executed this command should return a structured representation of all the movies in the database
(Трябва да върне структурирана репрезнтация на всички филми от базата данни те може да са json или csv - трябва да се обосновем защо сме избрали този формат )

Movie Details Page: movdt <movie_id>
Users should be able to get the details of a movie if it exists in the database. Details
may include the movie's title, description, release date, director, genre, and user
ratings.
(С командата movdt приема аргумент ID на даден филм. Ако той съществува потребителите трябва да вземат детаили за тотизи филм(title, description, release date, director, genre, and user
ratings) ако филмът не съществува трябва да по пимислим дали ще отпечатаме нещо. Когато съсдаваме базата данни за филмите ако взимаме информацията от IMDB или Google трябва да добавим API интеграция)


Относно командният интерфеис (movlst, movvdt, movsrch......) единият вариянт е да имаме отделни питонски скриптове за всяка команда а другият вариянт е да направим един питонски скрипт които да се казва например (moviedb) и на него да се добавят различните команди (movlst, movvdt, movsrch......).


Search Functionality: movsrch <query>
Users should be able to search for movies based on their titles.
Search results should be a structured representation of all the movies that match the
search query.
(Филмите трябва да могат да се търсят само да база заглавията им добре е да направим по проста заявка да се търси по точно съвпадение. Резултатите трябва да са структурирана репрезентация на всички филми които съвпадат със заявката за търсене. Хубаво е да използваме един и същи формат фаил json или csv).

Adding New Movies: movadd <title> <desc> <date> <director> <genre>
Users can add new movies to the database.
They should provide details such as the movie's title, description, release date,
director, and genre
(Потребителите могат да добавят филми и трябва да дават детаили за всеки един филм. Трябва да помислим какво става ако има дубликат(едно и също заглавие). Тук трябва да помислим и за реитингът на филма. Хубаво е да направим някакво ограничение за жанровете, например да има само 3 или 4 жанра)

Favorites: movfv <movie_id>
Users should be able to mark movies as their favorites.
(Командата маркира даден филм като любим)


Трябва да помислим как да създадем някаква логин команда за да може дадена команда да се изпълни от името на даден потребител.


Movie Categories: movcat <category: [liked, newest, genre]>
Movies will be categorized by genres.
Sections like "Most Liked," "Newest," and "Genres" will feature the top 5 movies in
each category.
(Трябва да може да показваме 5 най харесвани от жанр филма, 5 най нови от жанр  филма)
