$(document).ready(function(){
    // Autocomplete functionality
    $("#searchInput").autocomplete({
        source: function(request, response) {
            $.getJSON("/autocomplete", { term: request.term }, function(data) {
                response(data);
            });
        },
        minLength: 1, // Minimum characters before suggestions appear
        select: function(event, ui) {
            $("#searchInput").val(ui.item.value);
            $("#searchForm").submit();
        }
    });

    // Refocus on the input field after page load
    $("#searchInput").focus();

    // Search form submission
    $("#searchForm").submit(function(event){
        event.preventDefault();  // Prevent default form submission
        let query = $("#searchInput").val().trim();  // Trim whitespace

        if (query === "") {
            // If the query is just whitespace, clear the input and keep focus
            $("#searchInput").val("").focus();
            return; // Stop execution, do not search
        }

        // Perform search if the query is valid
        window.location.href = "/search?q=" + encodeURIComponent(query);
    });
});

