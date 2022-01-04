$(function () {
	const IngredientItem = ({ id, name, amount, unit }) => `
		<tr>
			<td>
				<input type="hidden" name="ingredients" value='{"id":"${id}","amount":"${amount}","unit":"${unit}"}'>
				${name}
			</td>
			<td class="text-end">${amount}</td>
			<td>${unit}</td>
			<td class="text-end"><em>&ndash; save recipe to calculate &ndash;</em></td>
			<td class="text-end"><button type="button" class="js_remove_ingredient btn btn-danger btn-sm">x</button></td>
		</tr>
		`;

	$('#current_ingredients').on('click', 'button.js_remove_ingredient', function (event) {
		$(event.target).closest('tr').hide('fast').remove();
	});

	$('#js_add_ingredient').on('click', function (event) {
		let selected = $('#ingredients_input option:selected')
		let values = [{
			id: selected.data('id'),
			name: selected.data('name'),
			amount: $('#amount_input').val(),
			unit: $('#measurement_input').val(),
		}];

		$('#current_ingredients tbody').append(
			values.map(IngredientItem).join('')
		);
	});

});


