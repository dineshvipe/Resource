$(document).ready(function(){
    

        $("#drugs").autocomplete({
           source: "/signup/get_drugs",
            minLength: 1,
            appendTo: "#suggest",
            
            
        });

    
    });