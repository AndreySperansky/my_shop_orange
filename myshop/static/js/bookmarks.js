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
					$(`.messages`).append([
						'<div class="alert alert-success alert-dismissible fade show mt-3" role="alert">',
      			'<strong>Item Was Deleted From Favorits</strong>',
      			'<button type="button" class="close" data-dismiss="alert" aria-label="Close">',
        		'<span aria-hidden="true">&times;</span>',
      			'</button>',
						'</div>'].join(''))

				} else {
					$(`.icon${id}`).toggleClass('bi-heart-fill bi-heart')
					$(`.messages`).append(
						['<div class="alert alert-success alert-dismissible fade show mt-3" role="alert"> ',
						'	<strong>Item Was Added To Favorits</strong> ',
						'<button type="button" class="close" data-dismiss="alert" aria-label="Close">',
						'<span aria-hidden="true">&times;</span>',
						'</button> </div>',
						].join(''))
				}

			},

			error: function(response) {
				console.log('error', response)
			}
		})
		
		
		
	});
	
});

