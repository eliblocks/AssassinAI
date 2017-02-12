$(function() {
  var camera = document.getElementById('camera');
  var frame = document.getElementById('frame');

  camera.addEventListener('change', function(e) {
    var file = e.target.files[0]; 
     //Do something with the image file.
    frame.src = URL.createObjectURL(file);
  });

  $( "#camera" ).click(function() {
    $("#result").html("<h3>No Match</h3>");
  });

});
