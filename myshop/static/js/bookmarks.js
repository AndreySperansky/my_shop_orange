// Рабочий варант - заменяет текст внутри кнопки

console.log('Hello from Bookmarks!')


$(document).ready(function(){
	
	$('.add-wish-list').on('click', '#bookmark', function(e){
		e.preventDefault()
		console.log('works!')
		
		let current = $(this)
		const id = current.data('id')
		console.log(id)
		
		const icon = $(`.icon${id}`)
		console.log(icon)
		
		const cls = icon.attr('class')
		console.log(cls)
		
		// const url = $(this).attr('action')
		// console.log(url)
		
		
		
		$.ajax({
			// type: 'POST',
			url: "/bookmarks/add/" + id + "/",
			data: {
				// 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
				'pk': id,
			},

			success: function(response) {
				console.log('success', response)
				let res = response['res'];
				console.log(res)
				if(res === 'false') {
					$(`.icon${id}`).toggleClass('bi-heart bi-heart-fill')

				} else {
					$(`.icon${id}`).toggleClass('bi-heart-fill bi-heart')

				}

			},

			error: function(response) {
				console.log('error', response)
			}
		})
		
		
		
	});
	
});

