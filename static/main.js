function deneme() {
  document.getElementById("demo").innerHTML = "Hello World";
}
function post_func() {
    var arr = [];
    var product  = document.getElementById("input-text").value
    $.ajax({
    url: "/carrefoursa",
    data: {"product-name": product},
    success: function(response) {
        for(var i in response){
            arr.push(["<img height='100' width='100' src="+response[i].resim+" >",response[i].urun,response[i].fiyat+" TL","<a href="+response[i].link +">Git</a>"])
        }
        $(document).ready(function() {
    $('#example').DataTable( {
        destroy: true,
        data: arr,
        lengthChange: false,
        pageLength:5,
        columns: [
            { title: "resim" },
            { title: "urun"  },
            { title: "fiyat" },
            { title: "link" },
        ]
    } );
} );
    },
    error: function(xhr) {
        document.getElementById("demo").innerHTML = "Error";
    }
});
}
function post_func2() {
    var arr = [];
    var product  = document.getElementById("input-text").value
    $.ajax({
    url: "/migros",
    data: {"product-name": product},
    success: function(response) {
        for(var i in response){
            arr.push(["<img height='100' width='100' src="+response[i].resim+">",response[i].urun,response[i].fiyat+" TL","<a href="+response[i].link +">Git</a>"])
        }
        $(document).ready(function() {
    $('#example2').DataTable( {
        destroy: true,
        data: arr,
        pageLength:5,
        lengthChange: false,
        columns: [
            { title: "resim" },
            { title: "urun" },
            { title: "fiyat" },
            { title: "link" },
        ]
    } );
} );
    },
    error: function(xhr) {
        document.getElementById("demo").innerHTML = "Error";
    }
});
}
function button_post(){

    post_func();
    post_func2();
}