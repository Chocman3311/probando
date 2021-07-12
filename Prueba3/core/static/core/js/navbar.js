function cargarNavbar2() {

  
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(ShowPosition);
    } else {
      console.log("geolocalizacion is not supported by this browser");
    }


  function ShowPosition(position) {
    //console.log("Latitude: " + position.coords.latitude + " Longitude: " + position.coords.longitude);
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var urlBase = "https://api.openweathermap.org/data/2.5/weather";
    var urlFormateada = `${urlBase}?lat=${lat}&lon=${lon}&appid=16f268e6a97bbba3396b473e2d3f5e0e&units=metric`;
    console.log(urlFormateada);


    $.get(urlFormateada, function (data) {
      // $.each(data.data,function(i, sitio){
      console.log(data);
      //})

      $(
        "#msg"
      ).html(`<img src="http://openweathermap.org/img/wn/${data.weather[0].icon}.png" height="50px"/>${data.main.temp}°C 
      ${data.weather[0].main}`);

    });
  }
}
