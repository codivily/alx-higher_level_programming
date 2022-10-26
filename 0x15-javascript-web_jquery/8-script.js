$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const ul = $('ul#list_movies');
    for (let item of data) {
        ul.append('<li>' + item.name + '</li>');
    }
});
