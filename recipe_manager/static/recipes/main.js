$(function () {
	const IngredientItem = ({ id, name, amount, unit }) => `
		<tr data-id="${id}">
			<td>
				<input type="hidden" name="ingredients" value='{"id":"${id}","amount":"${amount}","unit":"${unit}"}'>
				${name}
			</td>
			<td class="text-end">${amount} ${unit}</td>
			<td class="text-end"><small><em>save to calculate</em></small></td>
			<td class="text-end"><button type="button" class="js_remove_ingredient btn btn-danger btn-sm">x</button></td>
		</tr>`;

	function disableUsedIngredients() {
		$('#ingredients_input option[data-id]').attr('disabled', false);
		$('#current_ingredients tbody tr').each(function () {
			let optionElement = $('#ingredients_input option[data-id="' + $(this).data('id') + '"]');
			optionElement.attr('disabled', true);
		});
	}

	function resetAddIngredientForm() {
		$('#amount_input').val('');
		$('#ingredients_input').prop('selectedIndex', 0);
		$('#measurement_input').prop('selectedIndex', 0);
	}

	$('#current_ingredients').on('click', 'button.js_remove_ingredient', function (event) {
		$(event.target).closest('tr').hide('fast').remove();
		disableUsedIngredients();
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
		disableUsedIngredients();
		resetAddIngredientForm();
	});

	disableUsedIngredients();
});


