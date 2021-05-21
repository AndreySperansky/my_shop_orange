console.log('Hello from cart!')

window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (e) {
        var target_href = e.target;
        console.log('click!')

		if (target_href) {
			$.ajax({
	            url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

	            success: function (data) {
	                $('.basket_list').html(data.result);
	                console.log('ajax done')
	            },
	        });
		}
        e.preventDefault();
    });
}
