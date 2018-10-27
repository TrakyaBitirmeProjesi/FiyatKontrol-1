function deneme() {
  document.getElementById("demo").innerHTML = "Hello World";
}
function post_func() {
    var arr = [];
    var denem  = document.getElementById("input-text").value
    $.ajax({
    url: "/carrefoursa",
    data: {"product-name": denem},
    success: function(response) {
        for(var i in response){
            arr.push(["<img src="+response[i].resim+">",response[i].urun,response[i].fiyat,"<a href="+response[i].link +">Git</a>"])
        }
        $(document).ready(function() {
    $('#example').DataTable( {
        data: arr,
        columns: [
            { title: "resim" },
            { title: "urun" },
            { title: "fiyat" },
            { title: "link" },
        ]
    } );
    $('#example').width("%35")
} );
    },
    error: function(xhr) {
        document.getElementById("demo").innerHTML = "Error";
    }
});

}
